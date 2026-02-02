import argparse

from straw_polls.add_macro import ordered_load, Document

parser = argparse.ArgumentParser()
parser.add_argument("file", type=argparse.FileType("r"))
args = parser.parse_args()

contents = ordered_load(args.file)

doc = Document("macros.yaml", value=contents.pop("value"))
for kind in contents:
    for entry in contents.get(kind, []):
        match entry:
            case {"add": name, **kwargs}:
                doc.add(kind=kind, name=name, **kwargs)
            case {"update": name, **kwargs}:
                doc.update(kind=kind, name=name, **kwargs)
doc.dump()
