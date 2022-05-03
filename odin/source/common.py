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
    try:
        os.makedirs(path)

        return True
    except OSError:
        return False


def camelize(text):
    # type: (str) -> str
    text_split = re.split('[_ -]', text)

    camelize_text = list(map(str.title, text_split))
    camelize_text[0] = camelize_text[0].lower()

    return "".join(camelize_text)


def decamelize(text):
    # type: (str) -> str
    decamelize_text = ""

    for letter in text:
        if letter.isupper():
            decamelize_text += "_"
        decamelize_text += letter.lower()

    return decamelize_text