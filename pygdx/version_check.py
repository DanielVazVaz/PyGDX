from shutil import which
from sys import version_info
from os.path import dirname

if which("gams"):
    GAMS_PATH = which("gams")
    GAMS_PATH = dirname(GAMS_PATH)
else:
    GAMS_PATH = None

PYTHON_VERSION = (version_info[0], version_info[1])