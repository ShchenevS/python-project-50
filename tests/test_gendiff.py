import json
from gendiff.modules.gendiff import generate_diff
from gendiff.modules.gendiff import get_file_from_path


def test_get_file_from_path():
    file_path = './tests/fixtures/file1.json'
    file = get_file_from_path(file_path)
    correct_file = {
        "host": "hexlet.io",
    }
    assert file == correct_file


def test_generate_diff_no_change():
    file1_path = './tests/fixtures/file1.json'
    file2_path = './tests/fixtures/file2.json'
    correct_file = "{\n    host: hexlet.io\n}"
    assert generate_diff(file1_path, file2_path) == correct_file


def test_generate_diff_delete():
    file1_path = './tests/fixtures/file1.json'
    file3_path = './tests/fixtures/file3.json'
    correct_file = "{\n  - host: hexlet.io\n}"
    assert generate_diff(file1_path, file3_path) == correct_file


def test_generate_diff_add():
    file1_path = './tests/fixtures/file1.json'
    file4_path = './tests/fixtures/file4.json'
    correct_file = "{\n    host: hexlet.io\n  + timeout: 50\n}"
    assert generate_diff(file1_path, file4_path) == correct_file


def test_generate_diff_change():
    file1_path = './tests/fixtures/file1.json'
    file5_path = './tests/fixtures/file5.json'
    correct_file = "{\n  - host: hexlet.io\n  + host: hexlet1.io\n}"
    assert generate_diff(file1_path, file5_path) == correct_file
