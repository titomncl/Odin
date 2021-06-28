import trees_path

from Odin.source.core.create_tree import Tree
from Odin.source.common import concat, make_dirs


def create_project(root, project):
    """

    Args:
        root (str): root path of the project without the slash at the end
        project (str): project name

    Returns:
        bool: True if the project was created, False if it was not

    """
    project_path = concat(root, project, separator="/")
    project_tree = Tree.create_from_template(trees_path.project_tree(), project_path)

    project_created = make_dirs(project_path)

    if project_created:
        project_tree.create_on_disk()

        return True
    else:
        return False
