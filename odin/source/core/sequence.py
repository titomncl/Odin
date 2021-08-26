import os

try:
    from typing import Dict, List, Optional
except ImportError:
    pass

from ..common import concat
from ..globals import Logger as log
from . import project, trees_path
from .shot import Shot
from .tree import Tree, path_from_tree
from .yaml_parser import Parser


class Sequence(object):
    """Sequence object.

    Usage:
        sequence = Sequence.new(Project, 'NAME')
        sequence = Sequence.load(Project, 'NAME')
        sequence.new_shot("NAME")
        assets = project.get_shots(): List of created shots

    Parameters:
        name (str): name of the loaded sequence

    """

    def __init__(self, parent, name=None, data=None):
        # type: (project.Project, Optional[str], Optional[Dict[str]]) -> None
        self.parent = parent
        self._name = name
        self._data = data

    @property
    def name(self):
        # type: () -> str
        return self._name

    def get_shots(self):
        # type: () -> List[str]
        return Shot.list(self)

    def new_shot(self, name):
        # type: (str) -> Shot
        return Shot.new(self, name)

    @staticmethod
    def list(parent):
        # type: (project.Project) -> List[str]
        """List the sequences found in the given project.

        Args:
            parent: Project object

        Returns:
            List of the sequences

        """
        path = path_from_tree(parent.data, "SEQ", parent.root)["PATH"]
        seq = next(os.walk(path))[1]
        return seq

    @classmethod
    def load(cls, parent, name):
        # type: (project.Project, str) -> Sequence
        """Load an existing sequence.

        Args:
            parent: Project that contain the sequence
            name: Name of the sequence to load

        Returns:
            Sequence object

        """
        _data = Parser.open(os.path.join(parent.root, parent.name, "odin.yaml")).data
        _data = _data[parent.name]["DATA"]["FILM"]["SEQ"][name]

        return cls(parent, name, _data)

    @classmethod
    def new(cls, parent, name):
        # type: (project.Project, str) -> Sequence
        """Create a new sequence.

        Args:
            parent: Project to put the sequence in
            name: Name of the sequence

        Returns:
            Sequence object

        """
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

            if not seq_data["SEQ"]:
                seq_data["SEQ"] = dict()
            if not seq_out_data["SEQ"]:
                seq_out_data["SEQ"] = dict()

            seq_data["SEQ"].update(_data)
            seq_out_data["SEQ"].update(_data_out)

            prj_parser.write()

            log.info(concat("Sequence '", name, "' was created."))

            return cls(parent, name, _data[name])
        else:
            raise RuntimeError("No folder 'SEQ' found.")
