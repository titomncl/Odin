import glob

try:
    from typing import List
except ImportError:
    pass

from . import trees_path
from .create_tree import Tree
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

    def __init__(self, root, name=None):
        self._root = root
        self._name = name
        self._data = dict()

    @property
    def root(self):
        return self._root

    @property
    def data(self):
        return self._data

    def print(self, name=None):
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