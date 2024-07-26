add_depth_result = [
    {'name': 'folder1', 'status1': 'deleted', 'status2': None,
     'type1': 'directory', 'type2': None,
     'value1': [{'name': 'nothing', 'status1': 'unchanged',
                 'status2': 'unchanged', 'type1': 'file', 'type2': 'file',
                 'value1': 'old', 'value2': 'old', 'depth': 2}],
     'value2': None, 'depth': 1},
    {'name': 'folder2', 'status1': None, 'status2': 'added', 'type1': None,
     'type2': 'directory', 'value1': None,
     'value2': [{'name': 'something', 'status1': 'unchanged',
                 'status2': 'unchanged', 'type1': 'file', 'type2': 'file',
                 'value1': 'new', 'value2': 'new', 'depth': 2}],
     'depth': 1},
    {'name': 'follow', 'status1': 'deleted', 'status2': None, 'type1': 'file',
     'type2': None, 'value1': False, 'value2': None, 'depth': 1},
    {'name': 'host', 'status1': 'unchanged', 'status2': 'unchanged',
     'type1': 'file', 'type2': 'file', 'value1': 'hexlet.io',
     'value2': 'hexlet.io', 'depth': 1},
    {'name': 'newdir', 'status1': 'unchanged', 'status2': 'unchanged',
     'type1': 'directory', 'type2': 'directory',
     'value1': [{'name': 'firstitem', 'status1': 'changed', 'status2': 'changed',
                 'type1': 'file', 'type2': 'directory', 'value1': 'something',
                 'value2': [{'name': 'nothing', 'status1': 'unchanged',
                             'status2': 'unchanged', 'type1': 'file',
                             'type2': 'file', 'value1': 'here',
                             'value2': 'here', 'depth': 3}],
                 'depth': 2},
                {'name': 'seconditem', 'status1': 'changed',
                 'status2': 'changed', 'type1': 'directory', 'type2': 'file',
                 'value1': [{'name': 'nothing', 'status1': 'unchanged',
                             'status2': 'unchanged', 'type1': 'file',
                             'type2': 'file', 'value1': 'here',
                             'value2': 'here', 'depth': 3}],
                 'value2': 'something', 'depth': 2}],
     'value2': None, 'depth': 1},
    {'name': 'proxy', 'status1': 'deleted', 'status2': None,
     'type1': 'file', 'type2': None, 'value1': '123.234.53.22',
     'value2': None, 'depth': 1},
    {'name': 'timeout', 'status1': 'changed', 'status2': 'changed',
     'type1': 'file', 'type2': 'file', 'value1': 50, 'value2': 20, 'depth': 1},
    {'name': 'verbose', 'status1': None, 'status2': 'added', 'type1': None,
     'type2': 'file', 'value1': None, 'value2': True, 'depth': 1}]
