import os

from typing import Optional, List

from . import trees_path
from .create_tree import Tree
from ..common import make_dirs, concat


def create_fx(root, project, fx_name, asset_type="FX"):
    # type: (str, str, str, Optional[str]) -> bool
    """
    Args:
        root (str): root path of the project without the slash at the end
        project (str): project
        set_name (str): asset name
        asset_type (str): FX by default

    Returns:
        bool: True if the project was created, False if it was not

    """
    set_path = concat(root, project, "DATA/LIB", asset_type.upper(), fx_name, separator="/")
    set_tree = Tree.create_from_template(trees_path.fx_tree(), set_path)

    asset_created = make_dirs(set_path)

    if asset_created:
        set_tree.create_on_disk()

        return True
    else:
        return False


def find_fx(root, project, type_="FX"):
    # type: (str, str, Optional[str]) -> List[str]
    """
    Args:
        root (str):
        project (str):
        type_ (str): FX folder by default

    Returns:
        list(str): assets found in the folder

    """
    if project:
        path = concat(root, project, "DATA/LIB", type_, separator="\\")

        try:
            assets = next(os.walk(path))[1]

            return assets
        except StopIteration:
            return list()
