from gendiff.modules.constant import SPACES_PER_DEPTH_LEVEL
from gendiff.modules.constant import SPACES_FOR_LEFT_SHIFT


def transform_bool_back(node, value):
    match node.get(value):
        case None:
            return 'null'
        case True:
            return 'true'
        case False:
            return 'false'
        case _:
            return str(node.get(value))


def get_spec_symbol(node, status, value):
    match node.get(status):
        case "added":
            return "+ "
        case "deleted":
            return "- "
        case "unchanged":
            return "  "
        case "changed":
            if value == 'value2':
                return "+ "
            else:
                return "- "


def make_a_string(node, position):
    num_of_spaces = node.get('depth') * SPACES_PER_DEPTH_LEVEL
    space = " " * num_of_spaces
    space_w_shift = " " * (num_of_spaces - SPACES_FOR_LEFT_SHIFT)
    if position == 1:
        status = 'status1'
        value = 'value1'
        type_ = 'type1'
    else:
        status = 'status2'
        value = 'value2'
        type_ = 'type2'
    common_part = space_w_shift + get_spec_symbol(node, status, value) + \
        node.get('name') + ": "
    if node.get(type_) == 'file':
        different_part = transform_bool_back(node, value) + "\n"
    else:
        different_part = "{\n" + show_the_difference(node.get(value)) + \
            space + "}\n"
    result = common_part + different_part
    return result


def show_the_difference(tree):
    def inner(node):
        if (node.get('status1') == 'deleted' and not node.get('status2')
                or node.get('type1') == node.get('type2')
                and node.get('status1') == 'unchanged'):
            return make_a_string(node, 1)
        if node.get('status2') == 'added' and not node.get('status1'):
            return make_a_string(node, 2)
        else:
            return (make_a_string(node, 1) + make_a_string(node, 2))

    if tree[0].get('depth') == 1:
        result = "{\n" + "".join(list(map(inner, tree))) + "}"
    else:
        result = "".join(list(map(inner, tree)))
    return result
