import subprocess
import os

from Odin.source.common import concat

def maya():

    maya = concat(os.getcwd().replace("\\", "/"), "softwaresList/maya.bat", separator="/")

    launch_env = os.environ.copy()

    launch_env["PYTHONPATH"] = os.getenv("DEV_ENV") + "/venv/27/Lib/site-packages;"

    subprocess.Popen(maya, env=launch_env, cwd=r"C:\Program Files\Autodesk\Maya2019")


def houdini():

    houdini = concat(os.getcwd().replace("\\", "/"), "softwaresList/houdini.bat", separator="/")

    launch_env = os.environ.copy()

    launch_env["PYTHONPATH"] = os.getenv("DEV_ENV") + "/venv/27/Lib/site-packages;"

    subprocess.Popen(houdini, env=launch_env, cwd=r"C:\Program Files\Autodesk\Maya2019")
