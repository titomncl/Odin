import os
import sys

if sys.version_info > (3, ):

    import typing

    if typing.TYPE_CHECKING:
        from Odin import Sequence

        from typing import Dict, List, Optional


from ..common import concat
from ..globals import Logger as log
from . import trees_path
from .tree import Tree, path_from_tree
from .yaml_parser import Parser


class Shot(object):
    """Shot object.

    Usage:
        shot = Shot.new(Sequence, 'NAME')\n
        shot = Shot.load(Sequence, 'NAME')\n

    Parameters:
        name (str): name of the loaded shot

    """

    def __init__(self, parent, name=None, data=None):
        # type: (Sequence, Optional[str], Optional[Dict[str]]) -> None  # noqa: F821
        self._parent = parent
        self._name = name
        self._data = data

    @property
    def name(self):
        # type: () -> str
        return self._name

    @staticmethod
    def list(parent):
        # type: (Sequence) -> List[str]  # noqa: F821
        """List the shots found in the given sequence.

        Args:
            parent: Sequence object

        Returns:
            List of the shots

        """
        path = path_from_tree(parent.parent.data, parent.name, parent.parent.root)["PATH"]
        seq = next(os.walk(path))[1]
        return seq

    @classmethod
    def load(cls, parent, name):
        # type: (Sequence, str) -> Shot  # noqa: F821
        """Load an existing shot.

        Args:
            parent: Sequence that contain the shot
            name: Name of the shot to load

        Returns:
            Shot object

        """
        _data = Parser.open(os.path.join(parent.parent.root, parent.parent.name, "odin.yaml")).data
        _data = _data[parent.parent.name]["DATA"]["FILM"]["SEQ"][parent.name][name]

        return cls(parent, name, _data)

    @classmethod
    def new(cls, parent, name):
        # type: (Sequence, str) -> Shot  # noqa: F821
        """Create a new shot.

        Args:
            parent: Sequence to put the shot in
            name: Name of the shot

        Returns:
            Shot object

        """
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

        shot_data = prj_parser.data[parent.parent.name]["DATA"]["FILM"][Keys.SEQ]
        shot_out_data = prj_parser.data[parent.parent.name][Keys.OUT][Keys.SEQ]

        if not shot_data[parent.name]:
            shot_data[parent.name] = dict()
        if not shot_out_data[parent.name]:
            shot_out_data[parent.name] = dict()

        shot_data[parent.name].update(_data)
        shot_out_data[parent.name].update(_data_out)

        prj_parser.write()

        log.info(concat("Shot '", name, "' was created."))

        return cls(parent, name, _data[name])
