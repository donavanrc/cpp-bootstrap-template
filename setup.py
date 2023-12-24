import os
import platform
import subprocess

def execCommandQuiet(message):
    return subprocess.call(message, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if execCommandQuiet("git --version") != 0:
    print("Git is required. Install Git and try again")
    exit(255)
if execCommandQuiet("cmake --version") != 0:
    print("CMake is required. Install CMake and try again")
    exit(255)
    
pythonExecutable = "python" if platform.system() == "Windows" else "python3"
scriptFilename = "External/bootstrap.py"
if os.system(f"{pythonExecutable} {scriptFilename} -b External") != 0:
    print(f"Unable to run {scriptFilename}")
    exit(255)
    
print("\nBootstrap: Done!")