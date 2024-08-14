import pytest
from gendiff.modules.gendiff import generate_diff
from tests.fixtures.correct_file_3n5step import result as result_3n5step
from tests.fixtures.correct_file_6step import result as result_6step
from tests.fixtures.correct_file_7step import result as result_7step
from tests.fixtures.correct_file_8step import result as result_8step


f1_json = './tests/fixtures/file1.json'
f2_json = './tests/fixtures/file2.json'
f3_json = './tests/fixtures/file3.json'
f4_json = './tests/fixtures/file4.json'
f5_json = './tests/fixtures/file5.json'
f1_3s_json = './tests/fixtures/file1_3step.json'
f2_3s_json = './tests/fixtures/file2_3step.json'
f1_5s_yaml = './tests/fixtures/file1_5step.yaml'
f2_5s_yaml = './tests/fixtures/file2_5step.yml'
f1_6s_json = './tests/fixtures/file1_6step.json'
f2_6s_json = './tests/fixtures/file2_6step.json'
f1_6s_yaml = './tests/fixtures/file1_6step.yml'
f2_6s_yaml = './tests/fixtures/file2_6step.yaml'
testdata = [
    (f1_json, f2_json, "{\n    host: hexlet.io\n}", "stylish"),
    (f1_json, f3_json, "{\n  - host: hexlet.io\n}", "stylish"),
    (f1_json, f4_json, "{\n    host: hexlet.io\n  + timeout: 50\n}", "stylish"),
    (f1_json, f5_json, "{\n  - host: hexlet.io\n  + host: hexlet1.io\n}", "stylish"),
    (f1_3s_json, f2_3s_json, result_3n5step, "stylish"),
    (f1_5s_yaml, f2_5s_yaml, result_3n5step, "stylish"),
    (f1_6s_json, f2_6s_json, result_6step, "stylish"),
    (f1_6s_yaml, f2_6s_yaml, result_6step, "stylish"),
    (f1_6s_json, f2_6s_json, result_7step, "plain"),
    (f1_6s_json, f2_6s_json, result_8step, "json")
]


@pytest.mark.parametrize("link1,link2,expected,format", testdata)
def test_generate_diff(link1, link2, expected, format):
    diff = generate_diff(link1, link2, format)
    assert diff == expected
