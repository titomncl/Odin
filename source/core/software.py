import subprocess
import os


def get_launch_env(py_ver):
    launch_env = os.environ.copy()

    launch_env["PYTHONPATH"] = os.getenv("DEV_ENV") + "/venv/" + py_ver + "/Lib/site-packages;"

    return launch_env


def launch_software(name, version):

    soft = os.getcwd().replace("\\", "/") + "/softwaresList/" + name + ".bat"

    if os.path.isfile(soft):

        launch_env = get_launch_env(version)

        subprocess.Popen(soft, env=launch_env)
