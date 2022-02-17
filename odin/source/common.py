import os
import re

try:
    from typing import Any, Dict
except ImportError:
    pass


def concat(*args, **kwargs):
    # type: (Any, Dict[str, str]) -> str
    """Safe string concatenation. Do not accept None for the moment.

    Args:
        *args: multiple input except None
        **kwargs=separator: only accept separator input

    Returns:
        concatenated text

    """
    separator = kwargs.get("separator", "")

    str_args = [str(arg) for arg in args]
    concat_str = separator.join(str_args)

    return concat_str


def make_dirs(path):
    # type: (str) -> bool
    """Safe make dirs return bool if created of exists.

    Args:
        path: directories to create

    Returns:
        True if `path` is created, False if `path` exists

    """
    if path and not os.path.exists(path):
        os.makedirs(path)

        return True
    else:
        return False


def camelize(text):
    text_split = re.split('[_ -]', text)

    camelize_text = ""
    for text_part in text_split:
        text_part = text_part.lower()
        if camelize_text:
            text_part = text_part.capitalize()
        camelize_text += text_part

    return camelize_text
