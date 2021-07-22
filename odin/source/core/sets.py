import os

from . import trees_path
from .create_tree import Tree
from ..common import make_dirs, concat


def create_set(root, project, set_name, asset_type="SET"):
    """

    Args:
        root (str): root path of the project without the slash at the end
        project (str): project
        set_name (str): asset name
        asset_type (str): SET by default

    Returns:
        bool: True if the project was created, False if it was not

    """
    set_path = concat(root, project, "DATA/LIB", asset_type.upper(), set_name, separator="/")
    set_tree = Tree.create_from_template(trees_path.set_tree(), set_path)

    asset_publish_path = concat(root, project, "DATA/LIB/PUBLISH", asset_type.upper(), set_name, separator="/")
    asset_publish_tree = Tree.create_from_template(trees_path.set_publish_tree(), asset_publish_path)

    asset_created = make_dirs(set_path)
    asset_publish_created = make_dirs(asset_publish_path)

    if asset_created and asset_publish_created:
        set_tree.create_on_disk()
        asset_publish_tree.create_on_disk()

        return True
    else:
        return False


def find_sets(root, project, type_="SET"):
    """

    Args:
        root (str):
        project (str):
        type_ (str): SET folder by default

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
