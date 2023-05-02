#!./paraview-5.11.1/bin/pvpython
import os 
import re

def getOutputPath(cfg_path):
    if not os.path.isfile(cfg_path):
        print("Can't find mfsim cfg file on: "+cfg_path)
        exit(1)
    with open(cfg_path, "r") as file:
        content = file.read()
        if not "output_path:" in content:
            print("Not a mfsim cfg file: "+cfg_path)
            exit(1)
        r = re.search(r"output_path: \"(.*)\"",content)
        if r:
            if r.group(1) != None:
                return r.group(1)
        return ""