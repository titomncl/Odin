import os

try:
    from typing import List, Dict, Optional
except ImportError:
    pass

from .yaml_parser import Parser


def add_days(root, project_name, days):
    # type: (str, str, int) -> None
    rush_path = os.path.join(root, project_name, "IN/FILMING/RUSH").replace("\\", "/")

    files = os.listdir(rush_path)

    days_file = len([f for f in files if "DAY" in f])

    # create folders
    for day in range(days):
        day_offset = day + days_file + 1
        day_path = rush_path + "/DAY" + str(day_offset).zfill(2)
        os.mkdir(day_path)

    # update odin.yaml file
    files = os.listdir(rush_path)

    p = Parser.open(os.path.join(root, project_name, "odin.yaml"))
    prj_data = p.data

    filming = prj_data[project_name]["IN"]["FILMING"]

    for file_ in files:
        if file_ not in filming["RUSH"]:
            filming["RUSH"].update({file_: None})

    p.write()
