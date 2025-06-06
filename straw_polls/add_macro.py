import argparse
import yaml
from collections import *
from contextlib import contextmanager

def ordered_load(stream, Loader=yaml.Loader, object_pairs_hook=OrderedDict):
    class OrderedLoader(Loader):
        pass
    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))
    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_mapping)
    return yaml.load(stream, OrderedLoader)

def ordered_dump(data, stream=None, Dumper=yaml.Dumper, **kwds):
    class OrderedDumper(Dumper):
        pass
    def _dict_representer(dumper, data):
        return dumper.represent_mapping(
            yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
            data.items())
    OrderedDumper.add_representer(OrderedDict, _dict_representer)
    return yaml.dump(data, stream, OrderedDumper, **kwds)

yaml.Dumper.ignore_aliases = lambda *args: True

def sort_papers(papers):
    def key(paper):
        grp = {'N': 0, 'P': 1, 'L': 2, 'C': 2}[paper[0]]
        return (grp, paper)
    return sorted(set(papers), key=key)

class Document(object):
    def __init__(self, filename, value=None):
        self.filename = filename
        self.value = value
        self.doc = ordered_load(open(filename))

    @contextmanager
    def row_for(self, kind, name):
        specific = self.doc[kind]
        for row in specific:
            if row['name'] == name:
                yield row
                break
        specific.sort(key=lambda d: d['name'])

    def change(self, kind, name, args, issue):
        specific = self.doc[kind]
        for row in specific:
            if row['name'] == name:
                row.update(args)
                papers = row['rows'][-1]['papers'].split()
                papers.append(issue)
                row['rows'][-1]['papers'] = ' '.join(sort_papers(papers))
                break
        specific.sort(key=lambda d: d['name'])

    def remove(self, kind, name, papers, value=None):
        self.add(kind=kind, name=name, value=(value or self.value), papers=papers, _remove=True)

    def update(self, kind, name, papers, value=None, headers=None):
        self.add(kind=kind, name=name, value=(value or self.value), papers=papers, _update=True, headers=headers)

    def update_library(self, **kwargs): self.update(kind='library', **kwargs)
    def update_language(self, **kwargs): self.update(kind='language', **kwargs)

    def add_library(self, **kwargs): self.add(kind='library', **kwargs)
    def add_language(self, **kwargs): self.add(kind='language', **kwargs)

    def add(self, kind, name, papers, value=None, headers=None, _remove=False, _update=False):
        value = value or self.value

        def fixup(arg):
            if isinstance(arg, str):
                return sorted(arg.split())
            else:
                return arg

        papers = sort_papers(fixup(papers))
        headers = fixup(headers)

        values = [('value', value),
                  ('papers', ' '.join(papers))]
        if _remove:
            values.append(('removed', True))
        specific = self.doc[kind]
        for row in specific:
            if row['name'] == name:
                for entry in row['rows']:
                    if entry['value'] == value:
                        # just add this paper
                        assert (not _remove) or entry.get('removed')
                        old_papers = entry['papers'].split()
                        old_papers.extend(papers)
                        old_papers = sort_papers(old_papers)
                        entry['papers'] = ' '.join(old_papers)

                        if headers is not None and _update:
                            # updating headers?
                            row['header_list'] = ' '.join(sorted(set(row['header_list'].split() + headers)))
                        break
                else:
                    # add a new row
                    row['rows'].append(OrderedDict(values))
                    row['rows'].sort(key=lambda d: d['value'])
                break
        else:
            if _remove or _update:
                raise AssertionError(f"Unexpected remove/add for {name=} {papers=}")
            # assert not _remove and not _update
            # add a new macro
            items = [('name', name)]
            if kind == 'library':
                if not headers:
                    raise RuntimeError(f'new library macro {name} requires headers')
                items.append(('header_list', ' '.join(headers)))

            items.append(('rows', [OrderedDict(values)]))
            specific.append(OrderedDict(items))
        specific.sort(key=lambda d: d['name'])

    def dump(self):
        # https://stackoverflow.com/a/8661021/2069064
        represent_dict_order = lambda self, data:self.represent_mapping('tag:yaml.org,2002:map', data.items())
        yaml.add_representer(OrderedDict, represent_dict_order)
        yaml.dump(self.doc, open(self.filename, 'w'), default_flow_style=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=argparse.FileType("r"))
    args = parser.parse_args()

    contents = ordered_load(args.file)

    doc = Document("../macros.yaml", value=contents.pop("value"))
    for kind in contents:
        for entry in contents.get(kind, []):
            match entry:
                case {"add": name, **kwargs}:
                    doc.add(kind=kind, name=name, **kwargs)
                case {"update": name, **kwargs}:
                    doc.update(kind=kind, name=name, **kwargs)
    doc.dump()
