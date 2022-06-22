import os
import sys
from copy import deepcopy

if sys.version_info > (3,):

    import typing

    if typing.TYPE_CHECKING:
        from Odin import Project
        from typing import Dict, List, Optional

from ..common import concat
from ..globals import Keys
from ..globals import Logger as log
from . import trees_path
from .tree import Tree, path_from_tree
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

    def __init__(self, parent, name=None, asset_type=None, data=None):
        # type: (Project, Optional[str], Optional[str], Optional[Dict[str]]) -> None  # noqa: F821
        self._parent = parent
        self._name = name
        self._asset_type = asset_type
        self._data = data or dict()

    @property
    def name(self):
        # type: () -> str
        return self._name

    @property
    def parent(self):
        # type: () -> Project
        return self._parent

    @property
    def asset_type(self):
        # type: () -> str
        return self._asset_type

    @property
    def paths(self):
        # type: () -> dict
        return path_from_tree(self.parent.data, self.asset_type, self.parent.project_path)

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
    def load(cls, parent, name, asset_type):
        # type: (Project, str, str) -> Asset  # noqa: F821
        """Load an existing asset.

        Args:
            parent: Project that contain the asset
            name: Name of the asset to load
            asset_type: Type of the asset (Chara, props, set, fx)

        Returns:
            Asset object

        """
        _data = Parser.open(os.path.join(parent.project_path, parent.name, "odin.yaml")).data

        lib = deepcopy(_data[parent.name]["DATA"]["LIB"])
        if asset_type not in lib:
            raise KeyError(
                "{} is not a valid asset type." "Should be 'CHARA', 'PROPS', 'SETS' or 'FX'.".format(asset_type)
            )
        elif name not in lib[asset_type]:
            raise KeyError("{} not in database.".format(name))
        else:
            _data = _data[parent.name]["DATA"]["LIB"][asset_type][name]
            return cls(parent, name, asset_type, _data)

    @classmethod
    def new(cls, parent, name, asset_type):
        # type: (Project, str, str) -> Asset  # noqa: F821
        """Create a new sequence.

        Args:
            parent: Project to put the sequence in
            name: Name of the sequence
            asset_type: Type of the asset (Chara, props, set, fx)

        Returns:
            Asset object

        """
        _data = dict()
        _data_publish = dict()
        _data_in = dict()

        root_values = path_from_tree(parent.data, asset_type, parent.project_path)

        if asset_type in [Keys.CHARA, Keys.PROPS]:
            _data[name] = Parser.open(trees_path.asset_tree()).data
            _data_publish[name] = Parser.open(trees_path.asset_publish_tree()).data
        elif asset_type == Keys.SET:
            _data[name] = Parser.open(trees_path.set_tree()).data
            _data_publish[name] = Parser.open(trees_path.set_publish_tree()).data
        elif asset_type == Keys.FX:
            _data[name] = Parser.open(trees_path.fx_tree()).data
            _data_publish[name] = None

        _data_in[name] = Parser.open(trees_path.asset_in_tree()).data

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

        return cls(parent, name, asset_type, _data[name])
