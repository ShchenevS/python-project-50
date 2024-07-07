import json


def return_diff(file1, file2):
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
        return {'key': key, 'old_value': value1, 'new_value': value2, 'status': status}
    result = list(map(inner, key_set))
    return result


def get_file_from_path(file_path):
    with open(file_path) as f:
        file = json.load(f)
    return file


def generate_diff(file_path1, file_path2):
    file1 = get_file_from_path(file_path1)
    file2 = get_file_from_path(file_path2)
    list_of_differencies = return_diff(file1, file2)
    result = "{\n"
    for difference in list_of_differencies:
        if difference.get('status') == 'unchanged':
            result += f"    {difference.get('key')}: {difference.get('old_value')}\n"
        elif difference.get('status') == 'deleted':
            result += f"  - {difference.get('key')}: {difference.get('old_value')}\n"
        elif difference.get('status') == 'added':
            result += f"  + {difference.get('key')}: {difference.get('new_value')}\n"
        elif difference.get('status') == 'changed':
            result += f"  - {difference.get('key')}: {difference.get('old_value')}\n"
            result += f"  + {difference.get('key')}: {difference.get('new_value')}\n"
    result += "}"
    return result
