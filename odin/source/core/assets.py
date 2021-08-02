import os

try:
    from typing import List, Dict, NoReturn, Optional
except ImportError:
    pass

from . import trees_path
from .tree import Tree, path_from_tree
from .yaml_parser import Parser
from ..globals import Logger as log
from ..common import concat


class Asset(object):
    def __init__(self, parent, name=None, task=None, data=None):
        # type: (Project, Optional[str], Optional[str], Optional[Dict[str]]) -> Asset
        self._parent = parent
        self._name = name
        self._task = task
        self._data = data or dict()

    @property
    def name(self):
        # type: () -> str
        return self._name

    @property
    def task(self):
        # type: () -> str
        return self._task

    @staticmethod
    def list(parent, task):
        # type: (Project, str) -> List[str]
        """

        Args:
            parent (Project): Project object
            task (str):

        Returns:
            list(str): List of the assets

        """
        path = path_from_tree(parent.data, task, parent.root)["PATH"]
        assets = next(os.walk(path))[1]
        return assets

    @classmethod
    def load(cls, parent, name, task):
        # type: (Project, str, str) -> Asset
        """
        Load an existing sequence

        Args:
            parent (Project): Project that contain the sequence
            name (str): Name of the sequence to load
            task (str): Name of the task

        Returns:
            Asset: Asset object

        """
        _data = Parser.open(os.path.join(parent.root, parent.name, "odin.yaml")).data
        _data = _data[parent.name]["DATA"]["LIB"][task][name]

        return cls(parent, name, task, _data)

    @classmethod
    def new(cls, parent, name, task):
        # type: (Project, str, str) -> Asset
        """
        Create a new sequence

        Args:
            parent (Project): Project to put the sequence in
            name (str): Name of the sequence
            task (str): Name of the task

        Returns:
            Asset: Asset object

        """
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

        asset_data = prj_parser.data[parent.name]["DATA"]["LIB"]
        asset_publish_data = prj_parser.data[parent.name]["DATA"]["LIB"]["PUBLISH"]

        if not asset_data[task]:
            asset_data[task] = dict()
        if not asset_publish_data[task]:
            asset_publish_data[task] = dict()

        asset_data[task].update(_data)
        asset_publish_data[task].update(_data_publish)

        prj_parser.write()

        log.info(concat("Asset '", name, "' was created in '", task, "'"))

        return cls(parent, name, task, _data[name])
