import os

try:
    from typing import List
except ImportError:
    pass

from . import trees_path
from .tree import Tree
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
