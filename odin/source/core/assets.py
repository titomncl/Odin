import os

try:
    from typing import List
except ImportError:
    pass

from . import trees_path
from .create_tree import Tree
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
    def __init__(self, parent, name=None, task=None):
        self._parent = parent
        self._name = name
        self._task = task
        self._data = dict()

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, value):
        self._root = value

    def new(self, name=None):
        self._name = name or self._name

        self._data[name] = Parser.open(trees_path.project_tree()).data

        root = Tree(None, self._root)
        root.create_tree(self._data, root)

        root.create_on_disk()

        prj_parser = Parser.open(concat(self._root, self._name, "/odin.yaml"))
        prj_parser.write(self._data)

    def list(self, root=None):
        self._root = root or self._root

        projects = glob.glob(self._root + "\\*\\odin.yaml")

        projects_name = list()

        for prj in projects:
            project = prj.replace("\\", "/")
            project = project.replace(self._root + "/", "")

            project_name = project.split("/")[0]

            projects_name.append(project_name)

        return projects_name

    # def get_assets(self):
    #

    @classmethod
    def load(cls, root, name):
        return cls(root, name)
