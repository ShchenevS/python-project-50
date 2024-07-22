from gendiff.modules.get_dict import get_dict_from_link


def test_get_dict_from_link():
    json_file_path = './tests/fixtures/file1.json'
    json_file = get_dict_from_link(json_file_path)
    yml_file_path = './tests/fixtures/file1.yml'
    yml_file = get_dict_from_link(yml_file_path)
    yaml_file_path = './tests/fixtures/file1.yaml'
    yaml_file = get_dict_from_link(yaml_file_path)
    correct_file = {
        "host": "hexlet.io",
    }
    assert json_file == correct_file
    assert yml_file == correct_file
    assert yaml_file == correct_file
