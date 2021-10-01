import glob
import os
import sys

if sys.version_info > (3, ):

    import typing

    if typing.TYPE_CHECKING:
        from typing import Dict, List, Optional

from ..common import concat
from ..globals import Logger as log
from . import trees_path
from .assets import Asset
from .sequence import Sequence
from .tree import Tree
from .yaml_parser import Parser


class Project(object):
    """Project object.

    Usage:
        project = Project.new('root/path', 'NAME')\n
        project = Project.load('root/path', 'NAME')\n
        project.new_asset("asset_name", "ASSET_TYPE"): CHARA, PROPS, SET or FX\n
        assets = project.get_assets("ASSET_TYPE"): List of created assets\n

    Parameters:
        name (str): name of the loaded project
        root (str): path of the loaded project
        data (str): dictionary containing data of the loaded project

    """

    def __init__(self, root=None, name=None, data=None):
        # type: (Optional[str], Optional[str], Optional[Dict[str]]) -> None
        self._prj_path = root
        self._name = name
        self._data = data or dict()
        self._assets = None

    @property
    def name(self):
        # type: () -> str
        return self._name

    @property
    def project_path(self):
        # type: () -> str
        return self._prj_path

    @property
    def data(self):
        # type: () -> Dict[str]
        return Parser.open(os.path.join(self.project_path, self.name, "odin.yaml")).data

    @staticmethod
    def list(root=None):
        # type: (Optional[str]) -> List[str]
        """List the projects found in the given root path.

        Args:
            root: folder path that contain the projects

        Returns:
            List of projects names

        """
        root = root or os.path.expanduser("~")
        projects = glob.glob(root + "\\*\\odin.yaml")

        projects_name = list()

        for prj in projects:
            project = prj.replace("\\", "/")
            project = project.replace(root + "/", "")

            project_name = project.split("/")[0]

            projects_name.append(project_name)

        return projects_name

    def get_assets(self, asset_type):
        # type: (str) -> List[str]
        return Asset.list(self, asset_type)

    def new_asset(self, name, asset_type):
        # type: (str, str) -> Asset
        return Asset.new(self, name, asset_type)

    def get_sequences(self):
        # type: () -> List[str]
        return Sequence.list(self)

    def new_sequence(self, name):
        # type: (str) -> Sequence
        return Sequence.new(self, name)

    @classmethod
    def load(cls, root, name):
        # type: (str, str) -> Project
        """Load an existing project.

        Args:
            root: Path where the project is
            name: Name of the project to load

        Returns:
            Project object

        Raises:
            RuntimeError: if the project does not exist

        """
        _file = Parser.open(os.path.join(root, name, "odin.yaml"))

        if not _file:
            raise RuntimeError("No project '{}' created in '{}'.".format(name, root))

        return cls(root, name, _file.data)

    @classmethod
    def new(cls, root, name):
        # type: (str, str) -> Project
        """Create a new project.

        Args:
            root: Path to put the project in
            name: Name of the project

        Returns:
            Project object

        """
        _data = dict()
        _data[name] = Parser.open(trees_path.project_tree()).data

        tree = Tree(None, root)
        tree.create_tree(_data, tree)

        tree.create_on_disk()

        Parser.new(os.path.join(root, name, "odin.yaml"), _data).write()

        log.info(concat("Project '", name, "' was created."))

        return cls(root, name, _data)
