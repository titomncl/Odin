import subprocess
import os

from CommonTools.yaml_parser import Parser

from Odin.source.globals import Logger as log


def get_launch_env(py_ver):
    launch_env = os.environ.copy()

    launch_env["PYTHONPATH"] = os.path.join(os.getenv("venv"), py_ver, "Lib/site-packages;")

    return launch_env


def launch_software(name, version):

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
