import os
import subprocess
from typing import Dict

from ..globals import Logger as log
from .yaml_parser import Parser


def get_launch_env(py_ver):
    # type: (str) -> Dict[str: str]
    launch_env = os.environ.copy()

    python_path = os.path.join(os.getenv("venv"), py_ver, "Lib/site-packages;")

    log.info("PYTHONPATH: {}".format(python_path))

    launch_env["PYTHONPATH"] = python_path

    return launch_env


def launch_software(name, version):
    # type: (str, str) -> None
    bat_file = os.getcwd().replace("\\", "/") + "/softwareList/" + name + ".bat"

    if os.path.isfile(bat_file):
        soft_config = Parser().open("./config/software_config.yaml").data[name]

        cwd = soft_config["cwd"]
        exe = soft_config["exe"]
        cmd = [bat_file, exe]

        log.info("Starting {}".format(name))
        log.info(exe)
        log.info(cwd)

        launch_env = get_launch_env(version)

        subprocess.Popen(cmd, env=launch_env, cwd=cwd)
