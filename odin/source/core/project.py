import glob

from . import trees_path
from .create_tree import Tree

from CommonTools.os_ import make_dirs
from CommonTools.concat import concat


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


def find_project(root):
    """
    Get the projects available in the root path

    Args:
        root (str): root path

    Returns:
        list(str): return all projects found

    """
    projects = glob.glob(root + "\\*\\DATA\\LIB")

    projects_name = list()

    for prj in projects:
        project = prj.replace("\\", "/")
        project = project.replace(root + "/", "")

        project_name = project.split("/")[0]

        projects_name.append(project_name)

    return projects_name
