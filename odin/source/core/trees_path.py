import os

from ...resources import trees

PATH = os.path.split(trees.__file__)[0]


def asset_tree():
    # type: () -> str
    return os.path.join(PATH, trees.ASSET_TREE)


def asset_publish_tree():
    # type: () -> str
    return os.path.join(PATH, trees.ASSET_PUBLISH_TREE)


def asset_in_tree():
    # typeL () -> str
    return os.path.join(PATH, trees.ASSET_TREE)


def set_tree():
    # type: () -> str
    return os.path.join(PATH, trees.SET_TREE)


def set_publish_tree():
    # type: () -> str
    return os.path.join(PATH, trees.SET_PUBLISH_TREE)


def fx_tree():
    # type: () -> str
    return os.path.join(PATH, trees.FX_TREE)


def shot_tree():
    # type: () -> str
    return os.path.join(PATH, trees.SHOT_TREE)


def shot_out_tree():
    # type: () -> str
    return os.path.join(PATH, trees.SHOT_OUT_TREE)


def take_tree():
    # type: () -> str
    return os.path.join(PATH, trees.TAKE_TREE)


def project_tree():
    # type: () -> str
    return os.path.join(PATH, trees.PROJECT_TREE)


def qcm_tree():
    # type: () -> str
    return os.path.join(PATH, trees.QCM_TREE)


def seq_tree():
    # type: () -> str
    return os.path.join(PATH, trees.SEQ_TREE)
