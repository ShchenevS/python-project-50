import pytest
from gendiff.modules.gendiff import get_file_type
from gendiff.modules.parser import parse


file_json = './tests/fixtures/file1.json'
file_yaml = './tests/fixtures/file1.yaml'
file_yml = './tests/fixtures/file1.yml'
correct_file = {"host": "hexlet.io"}
testdata1 = [
    (file_json, 'json'),
    (file_yaml, 'yaml'),
    (file_yml, 'yaml')
]
testdata2 = [
    (file_json, correct_file),
    (file_yaml, correct_file)
]


@pytest.mark.parametrize("link,expected", testdata1)
def test_get_file_type(link, expected):
    type_ = get_file_type(link)
    assert type_ == expected


@pytest.mark.parametrize("link,expected", testdata2)
def test_parse(link, expected):
    dictionary = parse(link, get_file_type(link))
    assert dictionary == expected
