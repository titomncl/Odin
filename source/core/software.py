import subprocess
import os

from Odin.source.common import concat

def maya():

    maya = concat(os.getcwd().replace("\\", "/"), "softwaresList/maya.bat", separator="/")

    subprocess.Popen(maya, shell=True)


def houdini():

    houdini = concat(os.getcwd().replace("\\", "/"), "softwaresList/houdini.bat", separator="/")

    subprocess.Popen(houdini, shell=True)
