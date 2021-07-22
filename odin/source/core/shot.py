import os

from . import trees_path
from .create_tree import Tree
from ..common import make_dirs, concat


def create_shot(root, project, seq, shot):
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

    if seq:
        path = concat(root, project, "DATA/FILM", seq, separator="\\")

        try:
            shots = next(os.walk(path))[1]
            shots.sort()

            return shots
        except StopIteration:
            return list()
