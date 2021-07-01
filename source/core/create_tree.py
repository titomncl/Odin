import os

from Odin.source.common import concat


class Tree(object):
    """
    Create an object Tree based on a given template.

    """
    def __init__(self, parent, name):

        self._parent = parent
        self._name = name
        self._children = list()

    def get_parent(self, index=0):
        """

        Args:
            index:

        Returns:

        """
        if not index:
            return self._parent
        else:
            return self._parent.get_parent(index-1)

    def get_depth(self):
        """

        Returns:

        """
        if self._parent:
            return self._parent.get_depth() + 1
        else:
            return -1

    def get_hierarchy(self):
        hierarchy = ""

        for depth in range(self.get_depth()):
            hierarchy += " "

        hierarchy += "/" + self._name + "\\n"

        for child in self._children:
            hierarchy += child.get_hierarchy()

        return hierarchy

    def sort(self):

        self._children.sort(key=lambda x: x.name)

        for child in self._children:
            child.sort()

    def create_child(self, name):
        child = Tree(self, name)
        self._children.append(child)

        return child

    @property
    def full_name(self):
        if self._parent:
            return concat(self._parent.full_name, self._name, separator="/")
        else:
            return self._name

    @property
    def name(self):
        return self._name

    def create_on_disk(self):

        if not os.path.exists(self.full_name) and self._parent:
            print(concat("CREATE: ", self.full_name))
            # pass
            os.mkdir(self.full_name)
        else:
            print(concat(self.full_name, ": Folder is exists"))

        for child in self._children:
            child.create_on_disk()

    @staticmethod
    def create_from_template(template_path, root_):
        """

        Args:
            template_path (str): path of the yaml template
            root_ (str): root for the new tree

        Returns:
            Tree:

        """
        import yaml

        root = Tree(None, root_)

        template_file = yaml.load(open(template_path), Loader=yaml.Loader)

        create_tree(template_file, root)
        return root


def create_tree(tree, root):
    """
    Args:
        tree ({str: {} or None}):
        root (Tree):

    """
    for key, value in tree.items():
        child = root.create_child(key)
        if value:
            create_tree(value, child)
