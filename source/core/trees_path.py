import os

import trees

def asset_tree():
    return os.path.join(os.path.dirname(trees.__file__), trees.ASSET_TREE)

def asset_publish_tree():
    return os.path.join(os.path.dirname(trees.__file__), trees.ASSET_PUBLISH_TREE)

def place_tree():
    return os.path.join(os.path.dirname(trees.__file__), trees.PLACE_TREE)

def shot_tree():
    return os.path.join(os.path.dirname(trees.__file__), trees.SHOT_TREE)

def take_tree():
    return os.path.join(os.path.dirname(trees.__file__), trees.TAKE_TREE)

def project_tree():
    return os.path.join(os.path.dirname(trees.__file__), trees.PROJECT_TREE)

def qcm_tree():
    return os.path.join(os.path.dirname(trees.__file__), trees.QCM_TREE)

def seq_tree():
    return os.path.join(os.path.dirname(trees.__file__), trees.SEQ_TREE)
