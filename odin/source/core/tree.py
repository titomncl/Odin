import os

try:
    from typing import NoReturn, Dict, Union
except ImportError:
    pass

from ..globals import Logger as log
from ..common import concat


class Tree(object):
    """
    Create an object Tree based on a given template.

    Usage:
        t = Tree().create_from_template('template/file.yaml')\n
        t.create_on_disk()

    Parameters:
        parent (Tree):
        name (str): folder name given to the root of the tree

    """

    def __init__(self, parent, name):
        # type: (Union[Tree, None], str) -> Tree
        self._parent = parent
        self._name = name
        self._children = list()

    def create_child(self, name):
        # type: (str) -> Tree
        child = Tree(self, name)
        self._children.append(child)

        return child

    @property
    def full_name(self):
        # type: () -> str
        if self._parent:
            return concat(self._parent.full_name, self._name, separator="/")
        else:
            return self._name

    def create_on_disk(self):
        if not os.path.exists(self.full_name) and self._parent:
            log.info(concat("CREATE: ", self.full_name))
            os.mkdir(self.full_name)
        else:
            log.warning(concat(self.full_name, ": Folder exists"))

        for child in self._children:
            child.create_on_disk()

    def create_from_template(self, template_path, root_):
        # type: (str, str) -> Tree
        """

        Create a tree object with a yaml template file

        Args:
            template_path (str): path of the yaml template
            root_ (str): root for the new tree

        Returns:
            Tree: Tree object that contain the folders to create the tree

        """
        from .yaml_parser import Parser

        root = Tree(None, root_)

        template_file = Parser().open(template_path).data

        self.create_tree(template_file, root)
        return root

    def create_tree(self, data, tree):
        # type: (Dict[str: dict or None], Tree) -> NoReturn
        """
        Args:
            data ({str: {} or None}):
            tree (Tree):

        """
        for key, value in data.items():
            child = tree.create_child(key)
            if value:
                self.create_tree(value, child)
