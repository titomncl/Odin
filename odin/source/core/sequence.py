import os
import sys

if sys.version_info > (3,):

    import typing

    if typing.TYPE_CHECKING:
        from Odin import Project
        from typing import Dict, List, Optional

from ..common import concat
from ..globals import Keys
from ..globals import Logger as log
from . import trees_path
from .shot import Shot
from .tree import Tree, path_from_tree
from .yaml_parser import Parser


class Sequence(object):
    """Sequence object.

    Usage:
        sequence = Sequence.new(Project, 'NAME')\n
        sequence = Sequence.load(Project, 'NAME')\n
        sequence.new_shot("NAME")\n
        assets = project.get_shots(): List of created shots\n

    Parameters:
        name (str): name of the loaded sequence

    """

    def __init__(self, parent, name=None, data=None):
        # type: (Project, Optional[str], Optional[Dict[str]]) -> None  # noqa: F821
        self._parent = parent
        self._name = name
        self._data = data

    @property
    def name(self):
        # type: () -> str
        return self._name

    @property
    def parent(self):
        # type: () -> Project
        return self._parent

    @property
    def seq_paths(self):
        # type: () -> dict
        return path_from_tree(self.parent.data, Keys.SEQ, self.parent.project_path)

    def get_shots(self):
        # type: () -> List[str]
        return Shot.list(self)

    def new_shot(self, name):
        # type: (str) -> Shot
        return Shot.new(self, name)

    @staticmethod
    def list(parent):
        # type: (Project) -> List[str]  # noqa: F821
        """List the sequences found in the given project.

        Args:
            parent: Project object

        Returns:
            List of the sequences

        """
        path = path_from_tree(parent.data, Keys.SEQ, parent.project_path)[Keys.PATH]
        seq = next(os.walk(path))[1]
        return seq

    @classmethod
    def load(cls, parent, name):
        # type: (Project, str) -> Sequence  # noqa: F821
        """Load an existing sequence.

        Args:
            parent: Project that contain the sequence
            name: Name of the sequence to load

        Returns:
            Sequence object

        """
        _data = Parser.open(os.path.join(parent.project_path, parent.name, "odin.yaml")).data
        _data = _data[parent.name]["DATA"]["FILM"][Keys.SEQ][name]

        return cls(parent, name, _data)

    @classmethod
    def new(cls, parent, name):
        # type: (Project, str) -> Sequence  # noqa: F821
        """Create a new sequence.

        Args:
            parent: Project to put the sequence in
            name: Name of the sequence

        Returns:
            Sequence object

        """
        _data = dict()
        _data_out = dict()

        root_values = path_from_tree(parent.data, Keys.SEQ, parent.project_path)
        path = root_values[Keys.PATH]
        out_path = root_values[Keys.OUT]

        if path:
            _data[name] = Parser.open(trees_path.seq_tree()).data
            _data_out[name] = None

            tree = Tree(None, path)
            tree.create_tree(_data, tree)
            tree.create_on_disk()

            out_tree = Tree(None, out_path)
            out_tree.create_tree(_data_out, out_tree)
            out_tree.create_on_disk()

            prj_parser = Parser.open(os.path.join(parent.project_path, parent.name, "odin.yaml"))

            seq_data = prj_parser.data[parent.name]["DATA"]["FILM"]
            seq_out_data = prj_parser.data[parent.name][Keys.OUT]

            if not seq_data[Keys.SEQ]:
                seq_data[Keys.SEQ] = dict()
            if not seq_out_data[Keys.SEQ]:
                seq_out_data[Keys.SEQ] = dict()

            seq_data[Keys.SEQ].update(_data)
            seq_out_data[Keys.SEQ].update(_data_out)

            prj_parser.write()

            log.info(concat("Sequence '", name, "' was created."))

            return cls(parent, name, _data[name])
        else:
            raise RuntimeError("No folder 'SEQ' found.")
