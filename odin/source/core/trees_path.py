import os

from ...resources import trees

PATH = os.path.split(trees.__file__)[0]


def asset_tree():
    return os.path.join(PATH, trees.ASSET_TREE)


def asset_publish_tree():
    return os.path.join(PATH, trees.ASSET_PUBLISH_TREE)


def set_tree():
    return os.path.join(PATH, trees.SET_TREE)


def set_publish_tree():
    return os.path.join(PATH, trees.SET_PUBLISH_TREE)


def fx_tree():
    return os.path.join(PATH, trees.FX_TREE)


def shot_tree():
    return os.path.join(PATH, trees.SHOT_TREE)


def shot_out_tree():
    return os.path.join(PATH, trees.SHOT_OUT_TREE)


def take_tree():
    return os.path.join(PATH, trees.TAKE_TREE)


def project_tree():
    return os.path.join(PATH, trees.PROJECT_TREE)


def qcm_tree():
    return os.path.join(PATH, trees.QCM_TREE)


def seq_tree():
    return os.path.join(PATH, trees.SEQ_TREE)


def test():
    print(os.path.split(trees.__file__)[0])