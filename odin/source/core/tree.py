import os
import sys


if sys.version_info > (3, ):
    import typing

    if typing.TYPE_CHECKING:
        from typing import Dict, Optional, Union

from ..common import concat
from ..globals import Logger as log


class Tree(object):
    """Create an object Tree based on a given template.

    Usage:
        t = Tree().create_from_template('template/file.yaml')\n
        t.create_on_disk()

    Parameters:
        parent (Tree):
        name (str): folder name given to the root of the tree

    """

    def __init__(self, parent, name):
        # type: (Union[Tree, None], str) -> None
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
            os.mkdir(self.full_name)
        else:
            log.warning(concat(self.full_name, ": Folder exists"))

        for child in self._children:
            child.create_on_disk()

    def create_from_template(self, template_path, path):
        # type: (str, str) -> Tree
        """Create a tree object with a yaml template file.

        Args:
            template_path: path of the yaml template
            path: root path for the new tree

        Returns:
            Tree object that contain the folders to create the tree

        """
        from .yaml_parser import Parser

        root = Tree(None, path)

        template_file = Parser().open(template_path).data

        self.create_tree(template_file, root)
        return root

    def create_tree(self, data, tree):
        # type: (Dict[str], Tree) -> None
        for key, value in data.items():
            child = tree.create_child(key)
            if value:
                self.create_tree(value, child)


def path_from_tree(data, word, path="", values=None):
    # type: (Dict[str], str, Optional[str], Optional[Dict[str]]) -> Dict[str]
    _path = path
    _values = values or dict()

    for key, value in data.items():
        if value:
            _path = os.path.join(path, key)
            try:
                if word in value:
                    if "PUBLISH" in _path:
                        _values["PUBLISH"] = os.path.join(_path, word)
                    elif "OUT" in _path:
                        _values["OUT"] = os.path.join(_path, word)
                    else:
                        _values["PATH"] = os.path.join(_path, word)
            except KeyError:
                pass

            _values = path_from_tree(value, word, _path, _values)

    return _values
