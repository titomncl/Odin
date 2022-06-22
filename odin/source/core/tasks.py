import os
from dataclasses import dataclass
from enum import Enum

from Odin import *
from odin.source.core import trees_path
from odin.source.core.tree import path_from_tree, Tree, tree_from_path
from odin.source.core.yaml_parser import Parser
from odin.source.globals import Keys


class TaskType(Enum):
    MODELING = "modeling"
    RIGGING = "rigging"
    SHADING = "shading"
    LOOKDEV = "lookdev"
    LAYOUT = "layout"
    ANIMATION = "animation"
    LIGHTING = "lighting"
    ASSEMBLY = "assembly"
    COMPOSITING = "compositing"
    FX = "fx"
    EDITING = "editing"

    @classmethod
    def names(cls):
        return [attr for attr in dir(cls) if not callable(getattr(cls, attr)) and not attr.startswith("_")]


@dataclass
class Task(object):
    """Task object.

    Usage:
        task = Task.new(Asset, type=TaskType)\n
        task = Task.load(Asset, type=TaskType)\n

    Parameters:
        parent Asset: asset to add the task to
        type TaskType: task type to load

    """
    type: TaskType
    parent: Asset
    data: dict

    def __init__(self, parent: Asset, type: TaskType, data: dict=None):
        self._parent = parent
        self._type = type
        self._data = data

    @property
    def name(self):
        return self._type.value

    @property
    def parent(self):
        return self._parent

    @property
    def data(self):
        return self._data

    def __path(self, key):
        return os.path.join(self.parent.paths[key], self.name).replace("\\", "/")

    @property
    def version_path(self):
        return path_from_tree(self.data, "VERSION", self.__path(Keys.PATH))["PATH"]

    @property
    def publish_path(self):
        return path_from_tree(self.data, "PUBLISH", self.__path(Keys.PATH))["PATH"]

    @property
    def export_path(self):
        return self.__path(Keys.PUBLISH)

    @classmethod
    def load(cls, parent, type):
        # type: (Asset, TaskType) -> Task

        if not path_from_tree(parent.parent.data, type.value, parent.parent.project_path):
            raise KeyError(f"{type.value} not in database.")
        else:
            _data = tree_from_path(parent.parent.data,
                                   path_from_tree(parent.parent.data,
                                                  type.value,
                                                  parent.paths[Keys.PATH]
                                                  )[Keys.PATH],
                                   parent.paths[Keys.PATH])
            return cls(parent, type, _data)

    @classmethod
    def new(cls, parent: Asset, type: TaskType):
        """Create a new task.

        Args:
            parent: Asset to give a Task
            type: Type of the task

        Returns:
            Task object

        """
        root_values = path_from_tree(parent.parent.data, parent.name, parent.parent.project_path)
        path = root_values[Keys.PATH]

        _data = dict()
        _data[type.value] = Parser.open(trees_path.task_tree()).data

        tree = Tree(None, path)
        tree.create_tree(_data, tree)
        tree.create_on_disk()

        prj_parser = Parser.open(os.path.join(parent.parent.project_path, parent.parent.name, "odin.yaml"))

        task_data = prj_parser.data[parent.parent.name]["DATA"]["LIB"][parent.asset_type]

        task_data[parent.name].update(_data)

        prj_parser.write()

        return cls(parent, type, _data)

# if __name__ == '__main__':

    # prj = Project.load("D:/PROJECT", "LANDSCAPE")
    # asset = prj.get_asset("MOUNTAIN")

    # task = Task(asset, type=TaskType.LIGHTING)

    # print(task.name)
