import os

from Odin.source.core import trees_path
from Odin.source.core.create_tree import Tree
from Odin.source.common import concat, make_dirs


def create_fx(root, fx_name, asset_type="FX"):
    """

    Args:
        root (str): root path of the project without the slash at the end
        set_name (str): asset name
        asset_type (str): FX by default

    Returns:
        bool: True if the project was created, False if it was not

    """
    set_path = concat(root, "DATA/LIB", asset_type.upper(), fx_name, separator="/")
    set_tree = Tree.create_from_template(trees_path.fx_tree(), set_path)

    asset_created = make_dirs(set_path)

    if asset_created:
        set_tree.create_on_disk()

        return True
    else:
        return False


def find_fx(root, project, type_="FX"):
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

        assets = next(os.walk(path))[1]

        return assets
