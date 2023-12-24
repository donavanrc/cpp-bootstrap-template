import json
import os
import getopt
import shutil
import subprocess
import sys

DEPS_DIR_BASE = "Dependencies"
DEPS_JSON_BASE = "dependencies.json"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEPS_DIR = os.path.join(BASE_DIR, DEPS_DIR_BASE)
DEPS_JSON_FILENAME = os.path.join(BASE_DIR, DEPS_JSON_BASE)

def dlog(message):
    print(message)
    
def readJson(filename):
    try:
        source = open(filename).read()
    except:
        dlog(f"ERROR: Failed to read JSON file {filename}")
        return None
    
    try:
        return json.loads(source)
    except:
        dlog("ERROR: Failed to parse JSON")
        return None
 
def execCommand(command):
    return subprocess.call(command, shell=True, stdout=None, stderr=None)

def die(result):
    if result != 0:
        raise ValueError(f"Command returned non-zero status: {str(result)}")
   
def cloneRepository(url, name, version=None):
    targetDir = os.path.join(DEPS_DIR, name)
    dlog(f"Cloning {url} to {targetDir}")
    
    targetDirExists = os.path.exists(targetDir)
    repoExists = os.path.exists(os.path.join(targetDir, ".git"))
    
    if not repoExists:
        if targetDirExists:
            dlog(f"Removing {targetDir} before cloning")
            shutil.rmtree(targetDir)
        die(execCommand(f"git clone --recursive {url} {targetDir}"))
    else:
        dlog(f"Repository {targetDir} already exists. Fetching instead of cloning")
        die(execCommand(f"git -C {targetDir} fetch --recurse-submodules"))
        
    if version is None:
        version = "HEAD"
        
    die(execCommand(f"git -C {targetDir} reset --hard {version}"))
    die(execCommand(f"git -C {targetDir} clean -fxd"))
    
def main(argv):
    global BASE_DIR, DEPS_DIR, DEPS_JSON_FILENAME
    
    try:
        opts, args = getopt.getopt(argv, "ln:N:cCb:h", ["b"])
    except getopt.GetoptError:
        return 0;
    
    for opt, arg in opts:
        if opt in ("-b"):
            BASE_DIR = os.path.abspath(arg)
            DEPS_DIR = os.path.join(BASE_DIR,DEPS_DIR_BASE)
            DEPS_JSON_FILENAME = os.path.join(BASE_DIR, DEPS_JSON_BASE)
            
    data = readJson(DEPS_JSON_FILENAME)
    if data is None:
        return -1;
    
    dependencies = data.get("dependencies");
    
    for dependency in dependencies:
        name = dependency.get("name")
        source = dependency.get("source")
        type = source.get("type")
        
        if type == "git":
            url = source.get("url")
            version = source.get("version")
            cloneRepository(url, name, version)
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))