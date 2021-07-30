import os

try:
    from typing import List
except ImportError:
    pass

from . import trees_path
from .tree import Tree, path_from_tree
from .yaml_parser import Parser
from .shot import Shot
from ..common import make_dirs, concat


def create_sequences(root, project, sequence):
    # type: (str, str, str) -> bool
    """
    Args:
        root (str): root path of the project without the slash at the end
        project (str): project
        sequence (str): sequence name

    Returns:
        bool: True if the project was created, False if it was not

    """
    seq_path = concat(root, project, "DATA/FILM", sequence, separator="/")
    seq_tree = Tree.create_from_template(trees_path.seq_tree(), seq_path)

    seq_created = make_dirs(seq_path)

    if seq_created:
        seq_tree.create_on_disk()

        return True
    else:
        return False


def find_sequences(root, project):
    # type: (str, str) -> List[str]
    """
    Args:
        root (str):
        project (str):

    Returns:
        list (str): sequences found in the folder

    """

    if project:
        path = concat(root, project, "DATA/FILM", separator="\\")

        try:
            seq = next(os.walk(path))[1]
            seq.sort()

            return seq
        except StopIteration:
            return list()


class Sequence(object):

    def __init__(self, parent, name=None, data=None):
        self.parent = parent
        self._name = name
        self._data = data

    @property
    def name(self):
        return self._name

    def get_shots(self):
        return Shot.list(self)

    def new_shot(self, name):
        return Shot.new(self, name)

    @staticmethod
    def list(parent):
        path = path_from_tree(parent.data, "SEQ", parent.root)["PATH"]
        seq = next(os.walk(path))[1]
        return seq

    @classmethod
    def load(cls, parent, name):
        _data = Parser.open(os.path.join(parent.root, parent.name, "odin.yaml")).data
        _data = _data[parent.name]["DATA"]["FILM"]["SEQ"][name]

        return cls(parent, name, _data)

    @classmethod
    def new(cls, parent, name):
        _data = dict()
        _data_out = dict()

        root_values = path_from_tree(parent.data, "SEQ", parent.root)
        path = root_values["PATH"]
        out_path = root_values["OUT"]

        if path:
            _data[name] = Parser.open(trees_path.seq_tree()).data
            _data_out[name] = None

            tree = Tree(None, path)
            tree.create_tree(_data, tree)
            tree.create_on_disk()

            out_tree = Tree(None, out_path)
            out_tree.create_tree(_data_out, out_tree)
            out_tree.create_on_disk()

            prj_parser = Parser.open(os.path.join(parent.root, parent.name, "odin.yaml"))

            seq_data = prj_parser.data[parent.name]["DATA"]["FILM"]
            seq_out_data = prj_parser.data[parent.name]["OUT"]

            if not seq_data["SEQ"] and not seq_out_data["SEQ"]:
                seq_data["SEQ"] = dict()
                seq_out_data["SEQ"] = dict()

            seq_data["SEQ"].update(_data)
            seq_out_data["SEQ"].update(_data_out)

            prj_parser.write()

            return cls(parent, name, _data[name])
        else:
            raise RuntimeError("No folder 'SEQ' found.")
