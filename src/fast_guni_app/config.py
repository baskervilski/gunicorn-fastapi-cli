import yaml


def load_config(filename):
    with open(filename) as cfg_file:
        return yaml.safe_load(cfg_file)
