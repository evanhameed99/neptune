import os
import yaml


file_dir = os.path.dirname(os.path.abspath(__file__))


def load_yaml(file_path):
    with open(file_path, "r") as file:
        return yaml.safe_load(file)


def get_file_path(base_dir, file_name):
    return os.path.join(base_dir, file_name)


yaml_files = [
    get_file_path(file_dir, "config.yaml"),
]

config = {}
for file_path in yaml_files:
    config.update(load_yaml(file_path))
