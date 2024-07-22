from gendiff.modules.gendiff import generate_diff
from tests.fixtures.correct_file_3n5step import result as result_3n5step
from tests.fixtures.correct_file_6step import result as result_6step


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


def test_gendiff_3step_complex_json_files():
    file1_path = './tests/fixtures/file1_3step.json'
    file2_path = './tests/fixtures/file2_3step.json'
    correct_file = result_3n5step
    assert generate_diff(file1_path, file2_path) == correct_file


def test_gendiff_5step_complex_yaml_files():
    file1_path = './tests/fixtures/file1_5step.yaml'
    file2_path = './tests/fixtures/file2_5step.yml'
    correct_file = result_3n5step
    assert generate_diff(file1_path, file2_path) == correct_file


def test_gendiff_6step_complex_json_files():
    file1_path = './tests/fixtures/file1_6step.json'
    file2_path = './tests/fixtures/file2_6step.json'
    correct_file = result_6step
    assert generate_diff(file1_path, file2_path) == correct_file


def test_gendiff_6step_complex_yaml_files():
    file1_path = './tests/fixtures/file1_6step.yml'
    file2_path = './tests/fixtures/file2_6step.yaml'
    correct_file = result_6step
    assert generate_diff(file1_path, file2_path) == correct_file
