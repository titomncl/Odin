import trees_path

from Odin.source.core.create_tree import Tree
from Odin.source.common import concat, make_dirs


def create_sequences(root, sequence):
    """

    Args:
        root (str): root path of the project without the slash at the end
        sequence (str): sequence name

    Returns:
        bool: True if the project was created, False if it was not

    """
    seq_path = concat(root, "DATA/FILM", sequence, separator="/")
    seq_tree = Tree.create_from_template(trees_path.seq_tree(), seq_path)

    seq_created = make_dirs(seq_path)

    if seq_created:
        seq_tree.create_on_disk()

        return True
    else:
        return False
