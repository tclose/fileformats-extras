import yaml
from fileformats.application import DataSerialization, Yaml


@DataSerialization.load.register
def yaml_load(yml: Yaml):
    with open(yml.fspath) as f:
        data = yaml.load(f, Loader=yaml.Loader)
    return data


@DataSerialization.save.register
def yaml_save(yml: Yaml, data):
    with open(yml.fspath, "w") as f:
        yaml.dump(data, f)
