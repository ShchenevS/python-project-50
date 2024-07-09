import json
import yaml


def get_file_from_path(file_path):
    with open(file_path) as f:
        if file_path[-5:] == ".json":
            file = json.load(f)
        elif file_path[-5:] == ".yaml" or file_path[-4:] == ".yml":
            file = yaml.safe_load(f)
    return file


def make_dict_diff(file1, file2):
    key_set = sorted(set(file1).union(set(file2)))

    def inner(key):
        value1 = file1.get(key)
        value2 = file2.get(key)
        if key in file1 and key in file2:
            if value1 == value2:
                status = "unchanged"
            else:
                status = "changed"
        else:
            if key in file1:
                status = "deleted"
            else:
                status = "added"
        return {
            'key': key,
            'old_value': value1,
            'new_value': value2,
            'status': status}
    result = list(map(inner, key_set))
    return result


def make_string_diff(dict_of_differencies):
    result = "{\n"
    for diff in dict_of_differencies:
        if diff.get('status') == 'unchanged':
            result += f"    {diff.get('key')}: {diff.get('old_value')}\n"
        elif diff.get('status') == 'deleted':
            result += f"  - {diff.get('key')}: {diff.get('old_value')}\n"
        elif diff.get('status') == 'added':
            result += f"  + {diff.get('key')}: {diff.get('new_value')}\n"
        elif diff.get('status') == 'changed':
            result += f"  - {diff.get('key')}: {diff.get('old_value')}\n"
            result += f"  + {diff.get('key')}: {diff.get('new_value')}\n"
    result += "}"
    return result


def generate_diff(file_path1, file_path2):
    dict_file1 = get_file_from_path(file_path1)
    dict_file2 = get_file_from_path(file_path2)
    dict_of_differencies = make_dict_diff(dict_file1, dict_file2)
    string_of_differencies = make_string_diff(dict_of_differencies)
    return string_of_differencies
