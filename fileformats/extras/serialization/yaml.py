import yaml
from fileformats.serialization import DataSerialization, Yaml


@DataSerialization.load.register
def yaml_load(yml: Yaml):
    with open(yml.fspath) as f:
        data = yml.load(f, Loader=yaml.Loader)
    return data


@DataSerialization.save.register
def yaml_save(yml: Yaml, data):
    with open(yml.fspath, "w") as f:
        yaml.dump(data, f)
