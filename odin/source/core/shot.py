import os

try:
    from typing import List
except ImportError:
    pass

from . import trees_path
from .tree import Tree, path_from_tree
from .yaml_parser import Parser
from ..common import make_dirs, concat


def create_shot(root, project, seq, shot):
    # type: (str, str, str, str) -> bool
    """
    Args:
        root (str): root path of the project without the slash at the end
        project (str): project
        sequence (str): sequence name
        shot (str): shot name

    Returns:
        bool: True if the project was created, False if it was not

    """
    shot_path = concat(root, project, "DATA/FILM", seq, shot, separator="/")
    shot_tree = Tree.create_from_template(trees_path.shot_tree(), shot_path)

    seq_created = make_dirs(shot_path)

    if seq_created:
        shot_tree.create_on_disk()

        return True
    else:
        return False

def find_shots(root, project, seq):
    # type: (str, str, str) -> List[str]
    """
    Args:
        root (str):
        project (str):
        seq (str):

    Returns:
        list (str): shots found in the folder

    """

    if seq:
        path = concat(root, project, "DATA/FILM", seq, separator="\\")

        try:
            shots = next(os.walk(path))[1]
            shots.sort()

            return shots
        except StopIteration:
            return list()


class Shot(object):

    def __init__(self, parent, name=None, data=None):
        self._parent = parent
        self._name = name
        self._data = data

    @property
    def name(self):
        return self._name

    @staticmethod
    def list(parent):
        path = path_from_tree(parent.parent.data, parent.name, parent.parent.root)["PATH"]
        seq = next(os.walk(path))[1]
        return seq

    @classmethod
    def load(cls, parent, name):
        _data = Parser.open(os.path.join(parent.parent.root, parent.parent.name, "odin.yaml")).data
        _data = _data[parent.parent.name]["DATA"]["FILM"]["SEQ"][parent.name][name]

        return cls(parent, name, _data)

    @classmethod
    def new(cls, parent, name):
        _data = dict()
        _data_out = dict()

        root_values = path_from_tree(parent.parent.data, parent.name, parent.parent.root)
        path = root_values["PATH"]
        out_path = root_values["OUT"]

        _data[name] = Parser.open(trees_path.shot_tree()).data
        _data_out[name] = Parser.open(trees_path.shot_out_tree()).data

        tree = Tree(None, path)
        tree.create_tree(_data, tree)
        tree.create_on_disk()

        out_tree = Tree(None, out_path)
        out_tree.create_tree(_data_out, out_tree)
        out_tree.create_on_disk()

        prj_parser = Parser.open(os.path.join(parent.parent.root, parent.parent.name, "odin.yaml"))

        shot_data = prj_parser.data[parent.name]["DATA"]["FILM"]["SEQ"]
        shot_out_data = prj_parser.data[parent.name]["OUT"]["SEQ"]

        if not shot_data[parent.name] and not shot_out_data[parent.name]:
            shot_data[parent.name] = dict()
            shot_out_data[parent.name] = dict()

        shot_data[parent.name].update(_data)
        shot_out_data[parent.name].update(_data_out)

        prj_parser.write()

        return cls(parent, name, _data[name])
