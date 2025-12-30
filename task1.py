from pprint import pprint


def toml_parser(toml_file):
    parsed_data = {}
    current_section = None
    with open(toml_file, "r") as toml_file:
        for line in toml_file:
            cleaned_line = line.strip()
            if not cleaned_line or cleaned_line.startswith("#"):
                continue
            if cleaned_line.startswith("[") and cleaned_line.endswith("]"):
                current_section = cleaned_line[1:-1]
                parsed_data[current_section] = {}
            elif current_section and '=' in cleaned_line:
                key, value = cleaned_line.split("=", 1)
                parsed_data[current_section][key.strip()] = value.strip()[1:-1]
    return parsed_data


def serializer(binary_object):
    for section, keys_values in binary_object.items():
        print(f"{section}:")
        for key, vanlue in keys_values.items():
            print(f"      {key}: {vanlue}")




if __name__ == "__main__":
    binary_object = toml_parser('task1.toml')
    pprint(binary_object)
    serializer(binary_object)
