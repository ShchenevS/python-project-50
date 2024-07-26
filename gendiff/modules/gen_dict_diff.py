import copy


def make_dict(name, status1, status2, type1, type2, value1, value2):
    return {'name': name, 'status1': status1, 'status2': status2,
            'type1': type1, 'type2': type2, 'value1': value1, 'value2': value2}


def get_items(file, key):
    value = file.get(key)
    type_ = type(value)
    if type_ is dict:
        return ('directory', value)
    else:
        if key not in file:
            return (None, value)
        else:
            return ('file', value)


def get_status(file1, file2, key, type1, type2):
    if key not in file1:
        return (None, 'added')
    if key not in file2:
        return ('deleted', None)
    if type1 == type2 and (type1 == 'directory' or type1 == 'file'
                           and file1.get(key) == file2.get(key)):
        return ('unchanged', 'unchanged')
    else:
        return ('changed', 'changed')


def gen_dict_diff(file1, file2):
    key_set = sorted(set(file1).union(set(file2)))

    def inner(key):
        type1, value1 = get_items(file1, key)
        type2, value2 = get_items(file2, key)
        status1, status2 = get_status(file1, file2, key, type1, type2)
        if type1 == 'directory' and type2 == 'directory':
            return make_dict(key, status1, status2, type1, type2,
                             gen_dict_diff(value1, value2), None)
        if type1 == 'directory' and not type2 == 'directory':
            return make_dict(key, status1, status2, type1, type2,
                             gen_dict_diff(value1, value1), value2)
        if not type1 == 'directory' and type2 == 'directory':
            return make_dict(key, status1, status2, type1, type2,
                             value1, gen_dict_diff(value2, value2))
        else:
            return make_dict(key, status1, status2, type1, type2,
                             value1, value2)
    result = list(map(inner, key_set))
    return result


def add_depth(tree):
    def inner(node, depth):
        depth += 1
        node.update({'depth': depth})
        if node.get('type1') == 'directory':
            children = node.get('value1')
        elif (not node.get('type1') == 'directory'
                and node.get('type2') == 'directory'):
            children = node.get('value2')
        else:
            children = None
        if children:
            for child in children:
                inner(child, depth)
        return node
    depth = 0
    new_tree = copy.deepcopy(tree)
    new_tree = list(map(lambda node: inner(node, depth), new_tree))
    return new_tree
