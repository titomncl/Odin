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
from ..globals import Logger as log
from ..common import concat


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

        log.info(concat("Project '", name, "' was created."))

        return cls(root, name, _data)
