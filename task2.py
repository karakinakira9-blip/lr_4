from pprint import pprint

import toml
import yaml


def toml_parser(toml_file):
    with open(toml_file, "r", encoding="utf-8") as file:
        return toml.load(file)


def serializer(binary_object):
    yaml_output = yaml.dump(binary_object, allow_unicode=True, sort_keys=False)
    print(yaml_output)
    return binary_object


if __name__ == "__main__":
    binary_object = toml_parser('task1.toml')
    pprint(binary_object)
    serializer(binary_object)
