import json
import yaml

def refs_to_dict(filename):
    data = yaml.load(open(filename), Loader=yaml.CLoader)
    return {elem['id']: elem['title'] for elem in data.get('references', [])}

refs = {elem['id']: elem['title'] for elem in json.load(open('wg21/data/csl.json'))}
refs.update(refs_to_dict('md/wg21_fmt.yaml'))
refs.update(refs_to_dict('md/early.yaml'))

print(json.dumps(refs, indent=4))
