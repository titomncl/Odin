import os

from Odin.source.core import trees_path
from Odin.source.core.create_tree import Tree
from Odin.source.common import concat, make_dirs


def create_asset(root, asset_name, asset_type):
    """

    Args:
        root (str): root path of the project without the slash at the end
        asset_name (str): asset name
        asset_type (str): CHARA or PROPS

    Returns:
        bool: True if the project was created, False if it was not

    """
    asset_path = concat(root, "DATA/LIB", asset_type.upper(), asset_name, separator="/")
    asset_tree = Tree.create_from_template(trees_path.asset_tree(), asset_path)

    asset_publish_path = concat(root, "DATA/LIB/PUBLISH", asset_type.upper(), asset_name, separator="/")
    asset_publish_tree = Tree.create_from_template(trees_path.asset_publish_tree(), asset_publish_path)

    asset_created = make_dirs(asset_path)
    asset_publish_created = make_dirs(asset_publish_path)

    if asset_created and asset_publish_created:
        asset_tree.create_on_disk()
        asset_publish_tree.create_on_disk()

        return True
    else:
        return False


def find_assets(root, project, type_):
    """

    Args:
        root (str):
        project (str):
        type_ (str): CHARACTER, PROPS folder

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
