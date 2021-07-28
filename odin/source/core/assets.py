import os

try:
    from typing import List
except ImportError:
    pass

from . import trees_path
from .tree import Tree, path_from_tree
from .yaml_parser import Parser
from ..common import make_dirs, concat


def create_asset(root, project, asset_name, asset_type):
    # type: (str, str, str, str) -> bool
    """
    Args:
        root (str): root path of the project without the slash at the end
        project (str): project
        asset_name (str): asset name
        asset_type (str): CHARA or PROPS

    Returns:
        bool: True if the project was created, False if it was not

    """
    asset_path = concat(root, project, "DATA/LIB", asset_type.upper(), asset_name, separator="/")
    asset_tree = Tree.create_from_template(trees_path.asset_tree(), asset_path)

    asset_publish_path = concat(root, project, "DATA/LIB/PUBLISH",
                                asset_type.upper(), asset_name, separator="/")
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
    # type: (str, str, str) -> List[str]
    """
    Args:
        root (str):
        project (str):
        type_ (str): CHARACTER, PROPS folder

    Returns:
        list (str): assets found in the folder

    """
    if project:
        path = concat(root, project, "DATA/LIB", type_, separator="\\")

        try:
            assets = next(os.walk(path))[1]

            return assets
        except StopIteration:
            return list()


class Asset(object):
    def __init__(self, parent, name=None, task=None, data=None):
        self._parent = parent
        self._name = name
        self._task = task
        self._data = data or dict()

    @staticmethod
    def list(parent, task):
        path = path_from_tree(parent.data, task, parent.root)["PATH"]
        assets = next(os.walk(path))[1]
        return assets

    @classmethod
    def load(cls, parent, name, task):
        _data = Parser.open(os.path.join(parent.root, parent.name, "odin.yaml")).data
        _data = _data["DATA"]["LIB"][task][name]

        return cls(parent, name, task, _data)

    @classmethod
    def new(cls, parent, name, task):
        _data = dict()
        _data_publish = dict()

        root_values = path_from_tree(parent.data, task, parent.root)

        if task in ["CHARA", "PROPS"]:
            _data[name] = Parser.open(trees_path.asset_tree()).data
            _data_publish[name] = Parser.open(trees_path.asset_publish_tree()).data
        elif task == "SET":
            _data[name] = Parser.open(trees_path.set_tree()).data
            _data_publish[name] = Parser.open(trees_path.set_publish_tree()).data
        elif task == "FX":
            _data[name] = Parser.open(trees_path.fx_tree()).data
            _data_publish[name] = None

        path = root_values["PATH"]
        tree = Tree(None, path)
        tree.create_tree(_data, tree)
        tree.create_on_disk()

        publish_path = root_values["PUBLISH"]
        publish_tree = Tree(None, publish_path)
        publish_tree.create_tree(_data_publish, publish_tree)
        publish_tree.create_on_disk()

        prj_parser = Parser.open(os.path.join(parent.root, parent.name, "odin.yaml"))
        prj_parser.data[parent.name]["DATA"]["LIB"][task] = _data
        prj_parser.data[parent.name]["DATA"]["LIB"]["PUBLISH"][task] = _data_publish

        prj_parser.write()

        return cls(parent, name, task, prj_parser.data)
