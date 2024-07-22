import json
import yaml


def get_dict_from_link(file_path):
    with open(file_path) as f:
        if file_path[-5:] == ".json":
            file = json.load(f)
        elif file_path[-5:] == ".yaml" or file_path[-4:] == ".yml":
            file = yaml.safe_load(f)
    return file
