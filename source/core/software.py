import subprocess
import os

from Odin.source.common import concat

def get_launch_env(py_ver):
    launch_env = os.environ.copy()

    launch_env["PYTHONPATH"] = os.getenv("DEV_ENV") + "/venv/" + py_ver + "/Lib/site-packages;"

    return launch_env

def maya():

    maya = concat(os.getcwd().replace("\\", "/"), "softwaresList/maya.bat", separator="/")

    launch_env = get_launch_env("27")

    subprocess.Popen(maya, env=launch_env, cwd=r"C:\Program Files\Autodesk\Maya2019")


def houdini():

    houdini = concat(os.getcwd().replace("\\", "/"), "softwaresList/houdini.bat", separator="/")

    launch_env = get_launch_env("27")

    subprocess.Popen(houdini, env=launch_env, cwd=r"C:\Program Files\Autodesk\Maya2019")
