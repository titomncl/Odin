import glob
import os

try:
    from typing import List
except ImportError:
    pass

from . import trees_path
from .assets import Asset
from .sequence import Sequence
from .tree import Tree
from .yaml_parser import Parser
from ..common import make_dirs, concat


def create_project(root, project):
    # type: (str, str) -> bool
    """

    Args:
        root (str): root path of the project without the slash at the end
        project (str): project name

    Returns:
        bool: True if the project was created, False if it was not

    """
    project_path = concat(root, project, separator="/")
    project_tree = Tree.create_from_template(trees_path.project_tree(), project_path)

    project_created = make_dirs(project_path)

    if project_created:
        project_tree.create_on_disk()

        return True
    else:
        return False


def find_project(root):
    # type: (str) -> List[str]
    """
    Get the projects available in the root path

    Args:
        root (str): root path

    Returns:
        list (str): return all projects found

    """
    projects = glob.glob(root + "\\*\\DATA\\LIB")

    projects_name = list()

    for prj in projects:
        project = prj.replace("\\", "/")
        project = project.replace(root + "/", "")

        project_name = project.split("/")[0]

        projects_name.append(project_name)

    return projects_name


class Project(object):

    def __init__(self, root=None, name=None, data=None):
        self._root = root
        self._name = name
        self._data = data or dict()
        self._assets = None

    @property
    def name(self):
        return self._name

    @property
    def root(self):
        return self._root

    @property
    def data(self):
        return Parser.open(os.path.join(self.root, self.name, "odin.yaml")).data

    @staticmethod
    def list(root=None):
        root = root or os.path.expanduser("~")
        projects = glob.glob(root + "\\*\\odin.yaml")

        projects_name = list()

        for prj in projects:
            project = prj.replace("\\", "/")
            project = project.replace(root + "/", "")

            project_name = project.split("/")[0]

            projects_name.append(project_name)

        return projects_name

    def get_assets(self, task):
        return Asset.list(self, task)

    def new_asset(self, name, task):
        return Asset.new(self, name, task)

    def get_sequences(self):
        return Sequence.list(self)

    def new_sequence(self, name):
        return Sequence.new(self, name)

    @classmethod
    def load(cls, root, name):
        _data = Parser.open(os.path.join(root, name, "odin.yaml")).data

        return cls(root, name, _data)

    @classmethod
    def new(cls, root, name):

        _data = dict()
        _data[name] = Parser.open(trees_path.project_tree()).data

        tree = Tree(None, root)
        tree.create_tree(_data, tree)

        tree.create_on_disk()

        prj_parser = Parser.open(os.path.join(root, name, "odin.yaml"))
        prj_parser.write(_data)

        return cls(root, name, _data)
