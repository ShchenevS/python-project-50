from gendiff.modules.get_dict import get_dict_from_link
from gendiff.modules.gen_dict_diff import gen_dict_diff
from gendiff.modules.gen_dict_diff import add_depth
from gendiff.modules.formatters import stylish
from gendiff.modules.formatters import plain
from gendiff.modules.formatters import json_f


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


def generate_diff(file_path1, file_path2, format='stylish'):
    dict1 = get_dict_from_link(file_path1)
    dict2 = get_dict_from_link(file_path2)
    dict_of_diff = gen_dict_diff(dict1, dict2)
    dict_of_diff_with_depth = add_depth(dict_of_diff)
    if format == 'stylish':
        string_of_diff = stylish.show_the_difference(dict_of_diff_with_depth)
    if format == 'plain':
        string_of_diff = plain.show_the_difference(dict_of_diff_with_depth)
    if format == 'json':
        string_of_diff = json_f.show_the_difference(dict_of_diff_with_depth)
    return string_of_diff
