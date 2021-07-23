import os

from typing import Any, Dict


def concat(*args, **kwargs):
    # type: (Any, Dict[str, str]) -> str
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


def make_dirs(path):
    # type: (str) -> bool
    """
    Safe make dirs return bool if created of exists
    Args:
        path (str): directories to create

    Returns:
        bool: True if `path` is created, False if `path` exists

    """
    if path and not os.path.exists(path):
        os.makedirs(path)

        return True
    else:
        return False
