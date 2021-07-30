import os

try:
    from typing import List
except ImportError:
    pass

from . import trees_path
from .tree import Tree, path_from_tree
from .yaml_parser import Parser


class Asset(object):
    def __init__(self, parent, name=None, task=None, data=None):
        self._parent = parent
        self._name = name
        self._task = task
        self._data = data or dict()

    @property
    def name(self):
        return self._name

    @property
    def task(self):
        return self._task

    @staticmethod
    def list(parent, task):
        path = path_from_tree(parent.data, task, parent.root)["PATH"]
        assets = next(os.walk(path))[1]
        return assets

    @classmethod
    def load(cls, parent, name, task):
        _data = Parser.open(os.path.join(parent.root, parent.name, "odin.yaml")).data
        _data = _data[parent.name]["DATA"]["LIB"][task][name]

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

        asset_data = prj_parser.data[parent.name]["DATA"]["LIB"]
        asset_publish_data = prj_parser.data[parent.name]["DATA"]["LIB"]["PUBLISH"]

        if not asset_data[task] and not asset_publish_data[task]:
            asset_data[task] = dict()
            asset_publish_data[task] = dict()

        asset_data[task].update(_data)
        asset_publish_data[task].update(_data_publish)

        prj_parser.write()

        return cls(parent, name, task, _data[name])
