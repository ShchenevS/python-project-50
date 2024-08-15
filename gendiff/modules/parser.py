import json
import yaml


def parse(data, type_):
    with open(data) as f:
        if type_ == "json":
            dictionary = json.load(f)
        elif type_ == "yaml":
            dictionary = yaml.safe_load(f)
    return dictionary
