import os

from ...resources import trees


def asset_tree():
    return os.path.join("./odin/resources/trees", trees.ASSET_TREE)

def asset_publish_tree():
    return os.path.join("./odin/resources/trees", trees.ASSET_PUBLISH_TREE)

def set_tree():
    return os.path.join("./odin/resources/trees", trees.SET_TREE)

def set_publish_tree():
    return os.path.join("./odin/resources/trees", trees.SET_PUBLISH_TREE)

def fx_tree():
    return os.path.join("./odin/resources/trees", trees.FX_TREE)

def shot_tree():
    return os.path.join("./odin/resources/trees", trees.SHOT_TREE)

def shot_out_tree():
    return os.path.join("./odin/resources/trees", trees.SHOT_OUT_TREE)

def take_tree():
    return os.path.join("./odin/resources/trees", trees.TAKE_TREE)

def project_tree():
    return os.path.join("./odin/resources/trees", trees.PROJECT_TREE)

def qcm_tree():
    return os.path.join("./odin/resources/trees", trees.QCM_TREE)

def seq_tree():
    return os.path.join("./odin/resources/trees", trees.SEQ_TREE)
