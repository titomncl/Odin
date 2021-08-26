import os

from copy import deepcopy

try:
    from typing import List, Dict, Optional
except ImportError:
    pass

from . import trees_path
from .tree import Tree, path_from_tree
from .yaml_parser import Parser
from ..globals import Logger as log
from ..common import concat


class Asset(object):
    """Asset object.
    Each asset has a type: CHARA, PROPS, SET or FX.

    Usage:
        asset = Asset.new(Project, 'asset_name', 'ASSET_TYPE. )
        asset = Asset.load(Project, 'asset_name', 'ASSET_TYPE')

    Parameters:
        name (str): name of the loaded asset

    """

    def __init__(self, parent, name=None, asset_type=None, data=None):
        # type: ("odin.source.core.project.Project", Optional[str], Optional[str], Optional[Dict[str]]) -> None
        self._parent = parent
        self._name = name
        self._asset_type = asset_type
        self._data = data or dict()

    @property
    def name(self):
        # type: () -> str
        return self._name

    @property
    def asset_type(self):
        # type: () -> str
        return self._asset_type

    @staticmethod
    def list(parent, asset_type):
        # type: ("odin.source.core.project.Project", str) -> List[str]
        """List the assets found in the given project.

        Args:
            parent: Project object
            asset_type: Type of the assets to list

        Returns:
            List of the assets

        """
        path = path_from_tree(parent.data, asset_type, parent.root)["PATH"]
        assets = next(os.walk(path))[1]
        return assets

    @classmethod
    def load(cls, parent, name, asset_type):
        # type: ("odin.source.core.project.Project", str, str) -> Asset
        """Load an existing asset.

        Args:
            parent: Project that contain the asset
            name: Name of the asset to load
            asset_type: Type of the asset (Chara, props, set, fx)

        Returns:
            Asset object

        """
        _data = Parser.open(os.path.join(parent.root, parent.name, "odin.yaml")).data

        lib = deepcopy(_data[parent.name]["DATA"]["LIB"])
        if asset_type not in lib:
            raise KeyError(
                "{} is not a valid asset type." "Should be 'CHARA', 'PROPS', 'SETS' or 'FX' instead.".format(asset_type)
            )
        elif name not in lib[asset_type]:
            raise KeyError("{} not in database.")
        else:
            _data = _data[parent.name]["DATA"]["LIB"][asset_type][name]
            return cls(parent, name, asset_type, _data)

    @classmethod
    def new(cls, parent, name, asset_type):
        # type: ("odin.source.core.project.Project", str, str) -> Asset
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

        root_values = path_from_tree(parent.data, asset_type, parent.root)

        if asset_type in ["CHARA", "PROPS"]:
            _data[name] = Parser.open(trees_path.asset_tree()).data
            _data_publish[name] = Parser.open(trees_path.asset_publish_tree()).data
        elif asset_type == "SET":
            _data[name] = Parser.open(trees_path.set_tree()).data
            _data_publish[name] = Parser.open(trees_path.set_publish_tree()).data
        elif asset_type == "FX":
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

        asset_data = prj_parser.data[parent.name]["DATA"]["LIB"]
        asset_publish_data = prj_parser.data[parent.name]["DATA"]["LIB"]["PUBLISH"]

        if not asset_data[asset_type]:
            asset_data[asset_type] = dict()
        if not asset_publish_data[asset_type]:
            asset_publish_data[asset_type] = dict()

        asset_data[asset_type].update(_data)
        asset_publish_data[asset_type].update(_data_publish)

        prj_parser.write()

        log.info(concat("Asset '", name, "' was created in '", asset_type, "'"))

        return cls(parent, name, asset_type, _data[name])
