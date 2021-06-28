import os

def make_dirs(path):
    if path and not os.path.exists(path):
        os.mkdir(path)

        return True
    else:
        print("Can't create directory ", path)
        return False


def concat(*args, **kwargs):
    """

    Safe string concatenation. Do not accept None for the moment.

    Args:
        *args: multiple input except None
        **kwargs=separator: only accept separator input

    Returns:
        str : concatenated text

    """
    separator = kwargs.get("separator", "")

    str_args = [str(arg) for arg in args]
    concat_str = separator.join(str_args)

    return concat_str
