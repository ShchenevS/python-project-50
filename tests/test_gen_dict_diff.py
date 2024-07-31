from gendiff.modules.get_dict import get_dict_from_link
from gendiff.modules.gen_dict_diff import make_dict
from gendiff.modules.gen_dict_diff import get_items
from gendiff.modules.gen_dict_diff import get_status
from gendiff.modules.gen_dict_diff import gen_dict_diff
from gendiff.modules.gen_dict_diff import add_depth
from tests.fixtures.correct_file_for_test_gen_diff import gen_diff_result
from tests.fixtures.correct_file_for_test_add_depth import add_depth_result


def test_make_dict():
    dict1 = make_dict("test_dictionary", "old", "new",
                      None, 'strange', None, 10)
    dict2 = {'name': 'test_dictionary', 'status1': 'old', 'status2': 'new',
             'type1': None, 'type2': 'strange', 'value1': None, 'value2': 10}
    assert dict1 == dict2


def test_get_items():
    dict_ = {'first': [1, 2, 3], 'second': 222, 'third': {'dict': 'the only'}}
    assert get_items(dict_, 'zero') == (None, None)
    assert get_items(dict_, 'first') == ('file', [1, 2, 3])
    assert get_items(dict_, 'second') == ('file', 222)
    assert get_items(dict_, 'third') == ('directory', {'dict': 'the only'})


def test_get_status():
    file1_path = './tests/fixtures/file1_6step.json'
    file1 = get_dict_from_link(file1_path)
    file2_path = './tests/fixtures/file2_6step.json'
    file2 = get_dict_from_link(file2_path)
    assert get_status(file1, file2, 'group3',
                      'nevermind', 'directory') == (None, 'added')
    assert get_status(file1, file2, 'group2',
                      'directory', 'nevermind') == ('deleted', None)
    assert get_status(file1['group1'], file2['group1'], 'nest',
                      'directory', 'file') == ('changed', 'changed')
    assert get_status(file1['common'], file2['common'], 'setting1',
                      'file', 'file') == ('unchanged', 'unchanged')
    assert get_status(file1['common'], file2['common'], 'setting3',
                      'file', 'file') == ('changed', 'changed')
    assert get_status(file1['common'], file2['common'], 'setting6',
                      'directory', 'directory') == ('unchanged', 'unchanged')


def test_gen_dict_diff():
    file1_path = './tests/fixtures/file1_for_test_gen_diff.json'
    file1 = get_dict_from_link(file1_path)
    file2_path = './tests/fixtures/file2_for_test_gen_diff.json'
    file2 = get_dict_from_link(file2_path)
    assert gen_dict_diff(file1, file2) == gen_diff_result


def test_add_depth():
    assert add_depth(gen_diff_result) == add_depth_result
