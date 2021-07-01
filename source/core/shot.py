import trees_path

from Odin.source.core.create_tree import Tree
from Odin.source.common import concat, make_dirs


def create_shot(root, seq, shot):
    """

    Args:
        root (str): root path of the project without the slash at the end
        sequence (str): sequence name
        shot (str): shot name

    Returns:
        bool: True if the project was created, False if it was not

    """
    shot_path = concat(root, "DATA/FILM", seq, shot, separator="/")
    shot_tree = Tree.create_from_template(trees_path.shot_tree(), shot_path)

    seq_created = make_dirs(shot_path)

    if seq_created:
        shot_tree.create_on_disk()

        return True
    else:
        return False
