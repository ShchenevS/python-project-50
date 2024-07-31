from gendiff.modules.constant import BEGIN_FOR_PLAIN


def get_value_for_plain(node, value):
    match node.get(value):
        case None:
            return 'null'
        case True:
            return 'true'
        case False:
            return 'false'
        case _:
            if type(node.get(value)) is list:
                return '[complex value]'
            elif type(node.get(value)) is str:
                return f"'{str(node.get(value))}'"
            else:
                return str(node.get(value))


def get_spec_symbol(node):
    value_1 = get_value_for_plain(node, 'value1')
    value_2 = get_value_for_plain(node, 'value2')
    match node.get('status1'):
        case None:
            return (" was added with value: " + value_2)
        case "deleted":
            return " was removed"
        case "changed":
            return (" was updated. From " + value_1 + " to " + value_2)
        case "unchanged":
            return ""


def make_a_string(node, path):
    if not node.get('status1') == "unchanged":
        return (f"{BEGIN_FOR_PLAIN}'{path[:-1]}'{get_spec_symbol(node)}\n")
    else:
        return ""


def show_the_difference(tree):
    def inner(node, path):
        path += node.get('name') + "."
        if node.get('type1') == 'directory':
            children = node.get('value1')
        elif (not node.get('type1') == 'directory'
                and node.get('type2') == 'directory'):
            children = node.get('value2')
        else:
            children = None
        if children:
            return (make_a_string(node, path) + "".join(list(
                map(lambda node: inner(node, path), children))))
        else:
            return make_a_string(node, path)

    path = ""
    result = ("".join(list(map(lambda node: inner(node, path), tree))))[:-1]
    return result
