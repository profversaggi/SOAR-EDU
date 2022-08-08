# Do imports all in one spot
import os
from os import environ as env
from os.path import join
import subprocess


### Set up the various environment path variables

# Set the SOAR Home Dir 
SOAR_HOME = ""
if "SOAR_HOME" in env:
    SOAR_HOME = env["SOAR_HOME"]
else:
    SOAR_HOME = join("..","..","SoarSuite_9.6.0-Multiplatform_64bit","bin")

# Set the agent file folder (only need '/' because this is fed to Soar for loading .soar files)
AGENT_FOLDER = "../../agents-master/"

# Get the os type
OS_NAME = os.name

# Relative Path from local JNB Dir for the SOAR Debugger and the SOAR executable app
SOAR_DEBUGGER_RUNNER = ""
SOAR_APP = ""
MARIO_RUNNER = ""
if OS_NAME == "posix":
    SOAR_DEBUGGER_RUNNER = join(SOAR_HOME,"..","SoarJavaDebugger.sh")
    SOAR_APP= join(SOAR_HOME,"soar")
    MARIO_RUNNER = join("..","..","Run_Mario_MacLinux.sh")
else:
    SOAR_DEBUGGER_RUNNER = join(SOAR_HOME,"..","SoarJavaDebugger.bat")
    SOAR_APP = join(SOAR_HOME,"soar.exe")
    MARIO_RUNNER = join("..","..","Run_Mario_Windows.bat")


### Setup the methods we'll use to run soar

def run_soar_debugger(agent_file):
    subprocess.run([SOAR_DEBUGGER_RUNNER, "-source", agent_file])
    #subprocess.run([SOAR_DEBUGGER_RUNNER, "-listen", "12121"])

def run_soar(agent_file):
    #!{SOAR_APP+" -s "+agent_file+" run"}            # For classic iPython notebook app
    os.system(SOAR_APP+" -s "+agent_file+" run")    # For if the "!{}" syntax isn't supported by your notebook environment

def get_soar_cmd(agent_file):                       # For feeding into "!{}" within a notebook
    return SOAR_APP+" -s "+agent_file+" run"

def run_mario_soar(agent_file=None, open_debugger=True):
    args = [MARIO_RUNNER]
    if agent_file:
        args += [agent_file]
        if open_debugger:
            args += ["--open-debugger"]
    subprocess.run(args)