import os
import typing


if typing.TYPE_CHECKING:
    from Odin import Project
    from typing import Dict, List, Optional

from ..common import concat
from ..globals import Keys
from ..globals import Logger as log
from .tasks import Task
from .tree import Tree, path_from_tree, tree_from_path
from .yaml_parser import Parser


class Asset(object):
    """Asset object.
    Each asset has a type: CHARA, PROPS, SET or FX.

    Usage:
        foo = Asset.new(Project, 'asset_name', 'ASSET_TYPE')\n
        foo = Asset.load(Project, 'asset_name')\n

    Parameters:
        name (str): name of the loaded asset

    """

    def __init__(self, parent, name=None, data=None):
        # type: (Project, Optional[str], Optional[Dict[str]]) -> None  # noqa: F821
        self._parent = parent
        self._name = name
        self._data = data or dict()
        self.get_asset_type()

    @property
    def name(self):
        # type: () -> str
        return self._name

    @property
    def parent(self):
        # type: () -> Project
        return self._parent

    @property
    def data(self):
        self._data[self.name] = tree_from_path(self.parent.data, self.paths[Keys.PATH], self.parent.project_path)
        return self._data

    @property
    def asset_type(self):
        # type: () -> str
        return self._asset_type

    @property
    def paths(self):
        # type: () -> dict
        return path_from_tree(self.parent.data, self.asset_type, self.parent.project_path)

    @property
    def available_tasks(self):
        return Task.ASSET_TASKS
    
    def get_asset_type(self):
        """This method should not exist, but for now I don't have choice."""
        path = self.paths[Keys.PATH]
        self._asset_type = path.split("/")[-2]

    @staticmethod
    def list(parent, asset_type):
        # type: (Project, str) -> List[str]  # noqa: F821
        """List the assets found in the given project.

        Args:
            parent: Project object
            asset_type: Type of the assets to list

        Returns:
            List of the assets

        """
        path = path_from_tree(parent.data, asset_type, parent.project_path)[Keys.PATH]
        assets = next(os.walk(path))[1]
        return assets

    @classmethod
    def load(cls, parent, name):
        # type: (Project, str) -> Asset  # noqa: F821
        """Load an existing asset.

        Args:
            parent: Project that contain the asset
            name: Name of the asset to load

        Returns:
            Asset object

        """
        _data = Parser.open(os.path.join(parent.project_path, parent.name, "odin.yaml")).data

        if not path_from_tree(parent.data, name, parent.project_path):
            raise KeyError(f"{name} not in database.")
        else:
            _data = tree_from_path(
                parent.data,
                path_from_tree(parent.data, name, parent.project_path)[Keys.PATH],
                parent.project_path)
            return cls(parent, name, _data)

    @classmethod
    def new(cls, parent, name, asset_type):
        # type: (Project, str, str) -> Asset  # noqa: F821
        """Create a new sequence.

        Args:
            parent: Project to put the sequence in
            name: Name of the sequence
            asset_type: Type of the asset (CHARA, PROPS, SET, FX)

        Returns:
            Asset object

        """
        _data = dict()
        _data_publish = dict()
        _data_in = dict()

        if path_from_tree(parent.data, name, parent.project_path):
            log.error(f"{name} already exists.")
            return

        root_values = path_from_tree(parent.data, asset_type, parent.project_path)

        _data[name] = dict()
        _data_publish[name] = dict()
        _data_in[name] = dict()

        path = root_values[Keys.PATH]
        tree = Tree(None, path)
        tree.create_tree(_data, tree)
        tree.create_on_disk()

        publish_path = root_values[Keys.PUBLISH]
        publish_tree = Tree(None, publish_path)
        publish_tree.create_tree(_data_publish, publish_tree)
        publish_tree.create_on_disk()

        in_path = root_values[Keys.IN]
        in_tree = Tree(None, in_path)
        in_tree.create_tree(_data_in, in_tree)
        in_tree.create_on_disk()

        prj_parser = Parser.open(os.path.join(parent.project_path, parent.name, "odin.yaml"))

        asset_data = prj_parser.data[parent.name]["DATA"]["LIB"]
        asset_publish_data = prj_parser.data[parent.name]["DATA"]["LIB"][Keys.PUBLISH]
        asset_in_data = prj_parser.data[parent.name][Keys.IN]["LIB"]

        if not asset_data[asset_type]:
            asset_data[asset_type] = dict()
        if not asset_publish_data[asset_type]:
            asset_publish_data[asset_type] = dict()
        if not asset_in_data[asset_type]:
            asset_in_data[asset_type] = dict()

        asset_data[asset_type].update(_data)
        asset_publish_data[asset_type].update(_data_publish)
        asset_in_data[asset_type].update(_data_in)

        prj_parser.write()

        log.info(concat("Asset '", name, "' was created in '", asset_type, "'"))

        return cls(parent, name, _data[name])
