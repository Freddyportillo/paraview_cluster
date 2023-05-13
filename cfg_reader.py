#!./paraview-5.11.1/bin/pvpython
import os 
import re
import glob

def getOutputPath(cfg_path):
    cfgs = []
    outputs = []
    if not os.path.exists(cfg_path):
        print("Can't find mfsim cfg file or directory with cfg files on: "+cfg_path)
        exit(1)
    if os.path.isfile(cfg_path):
        cfgs.append(cfg_path)
    elif os.path.isdir(cfg_path):
        for filename in glob.iglob(cfg_path + '/**/*.cfg', recursive=True):
            if not "paraview-5.11.1" in filename:
                cfgs.append(filename)
    for cfg in cfgs:
        with open(cfg, "r") as file:
            content = file.read()
            if not "output_path:" in content:
                print("Not a mfsim cfg file: "+cfg)
                exit(1)
            r = re.search(r"output_path: \"(.*)\"",content)
            if r:
                if r.group(1) != None:
                    outputs.append(r.group(1))
    return outputs

def checkResultPath(result_path):
    if not os.path.exists(result_path):
        os.makedirs(result_path)

def generateResultPathForOutput(output_path, result_path):
    splt = output_path.split('/')
    case_name = splt[len(splt)-2] + "_" + splt[len(splt)-1]
    result = result_path + "/" + case_name
    if not os.path.exists(result):
        os.makedirs(result)
    return result

def formatCounter(ct, max = 9):
    if(len(ct) == max):
        return ct
    ct_id = ""
    for i in range(0,(max-len(ct))):
        ct_id = ct_id + "0"
    ct_id = ct_id + ct
    return ct_id

def getCT(output_path, ct_config):
    if len(ct_config) != 0:
        f_name = output_path+'/ns_output_ct.'+formatCounter(ct_config)+'.hdf5'
        if not os.path.isfile(f_name):
            print("Can't find HDF5 file: "+f_name)
            exit(1)
        return 'ns_output_ct.'+formatCounter(ct_config)+'.hdf5'
    else:
        files = [f for f in os.listdir(output_path) if re.match(r'ns_output_ct.*\.hdf5', f)]
        if len(files) == 0:
            print("Can't find ns_output_ct HDF5 files on: "+output_path)
            exit(1)
        files.sort(key=lambda f: int(re.sub('\D', '', f)), reverse=True)
        return files[0]

def getNode(output_path, node_config,id_node):
    out_path = output_path+'/probes_fsi'
    if len(node_config) != 0:
        f_name = out_path+'/str_001_node'+formatCounter(id_node, 6)+'.dat'
        if not os.path.isfile(f_name):
            print("Can't find NODE file: "+f_name)
            exit(1)
        return { "file": 'str_001_node'+formatCounter(id_node, 6)+'.dat', "id": formatCounter(id_node, 6) }
    else:
        files = [f for f in os.listdir(out_path) if re.match(r'str_001_node.*\.dat', f)]
        if len(files) == 0:
            print("Can't find str_001_node NODE files on: "+out_path)
            exit(1)
        files.sort(key=lambda f: int(re.sub('\D', '', f)), reverse=True)
        r = re.match(r'str_001_node(.*)\.dat', files[0])
        return { "file": files[0], "id": r.group(1) }
