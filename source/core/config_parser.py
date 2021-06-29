
def get_file():
    import os
    import Odin

    file = os.path.join(os.path.dirname(Odin.__file__), "config_file")

    return file


def parse_file():
    """

    Returns:
        dict (str: str):

    """
    import yaml

    config_file = get_file()

    content = yaml.load(open(config_file), Loader=yaml.Loader)

    return content


def get_value(key):
    return parse_file()[key]


def change_content(key, value):
    """

    Args:
        key (str):
        value (str):

    """
    import yaml

    data = parse_file()

    data[key] = value

    file = get_file()

    with open(file, 'w') as f:
        yaml.dump(data, f)

if __name__ == '__main__':
    print(get_value("ROOT_PATH"))
