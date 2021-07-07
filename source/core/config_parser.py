

def get_file(r_w="r"):

    config_file = open("./config/config_file.yaml", r_w)

    return config_file


def create_file(data):
    import yaml
    from Odin.source.common import make_dirs

    make_dirs("./config/")

    content = yaml.safe_dump(data)

    with open("./config/config_file.yaml", 'w') as file_:
        file_.write(content)


def parse_file():
    """

    Returns:
        dict (str: str):

    """
    import yaml

    config_file = get_file()

    content = yaml.load(config_file, Loader=yaml.Loader)

    return content


def get_value(key):
    try:
        return parse_file()[key]
    except IOError and KeyError:
        return None


def change_content(key, value):
    """

    Args:
        key (str):
        value (str):

    """
    import yaml

    try:
        data = parse_file()

        data[key] = value

        with get_file('w') as file:
            yaml.dump(data, file)
    except IOError:
        data = dict()
        data[key] = value

        create_file(data)


if __name__ == '__main__':
    print(get_value("ROOT_PATH"))
