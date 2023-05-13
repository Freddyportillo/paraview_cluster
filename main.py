#!./paraview-5.11.1/bin/pvpython
import sys
from postproc_pv import *
from structural_postproc import *
from cfg_reader import *

use_str = """Use: ./main.py [params]
Possible parameters:
                    \033[92mmfsim_cfg_path\033[0m=path                                              \033[91m[REQUIRED]\033[0m
                        Path to where MFSim's cfg files can be finded or path to MFSim cfg file
                    \033[92mresults_path\033[0m=path                                                \033[91m[REQUIRED]\033[0m
                        Path to where results should be generated
                    \033[92mct\033[0m=CT_NUMBER                                                     \033[93m[OPTIONAL]\033[0m
                        CT number from which results should be extracted. 
                        Default: last CT finded on output path
                    \033[92mnode\033[0m=STR_NODE                                                    \033[93m[OPTIONAL]\033[0m
                        Structural node from which results should be extracted. 
                        Default: last node finded on output path
                    
\033[94m** Examples **\033[0m

1 - Extract results from last CT and Node for all cases in /home/USER/cases and write results in /home/USER/cases-result
    ./main.py mfsim_cfg_path=/home/USER/cases results_path=/home/USER/cases-result

2 - Extract results from CT 100 and Node 1 for all cases in /home/USER/cases and write results in /home/USER/cases-result
    ./main.py mfsim_cfg_path=/home/USER/cases results_path=/home/USER/cases-result ct=100 node=1

3 - Extract results from last CT and Node for case in /home/USER/cases/case1.cfg and write results in /home/USER/case1-result
    ./main.py mfsim_cfg_path=/home/USER/cases/case1.cfg results_path=/home/USER/case1-result

"""


def validateArgs():
    if len(sys.argv) < 3:
        print(use_str)
        exit(1)
    args = {
        "mfsim_cfg_path": { "type": "str", "value": "", "setted": False, "required": True },
        "results_path": { "type": "str", "value": "", "setted": False, "required": True },
        "ct": { "type": "str", "value": "", "setted": False, "required": False },
        "node": { "type": "str", "value": "", "setted": False, "required": False }
    }
    for arg in sys.argv:
        arg_data = arg.split('=')
        if len(arg_data) > 1:
            arg_key = arg_data[0]
            arg_value = arg_data[1]
            if arg_key in args:
                if args[arg_key]['required']:
                    if len(arg_value) == 0:
                        print(use_str)
                        exit(1)
                if not args[arg_key]['setted']:
                    if args[arg_key]['type'] == "str":
                        args[arg_key]['value'] = arg_value
                    elif args[arg_key]['type'] == "bool":
                        if arg_value in ['false', 'False']:
                            args[arg_key]['value'] = False
                        else:
                            args[arg_key]['value'] = True
                    args[arg_key]['setted'] = True
    return args

def main():
    nodes2read = np.loadtxt(fname='nodes2read.dat').astype(int)
    args = validateArgs()
    output_paths = getOutputPath(args['mfsim_cfg_path']['value'])
    checkResultPath(args['results_path']['value'])
    for output_path in output_paths:
        result = generateResultPathForOutput(output_path, args['results_path']['value'])
        ct = getCT(output_path, args['ct']['value'])
        node = getNode(output_path, args['node']['value']) # nodes2read[0]); print(node) # args['node']['value'])
        run_postproc(output_path, result, ct)
        # for node in nodes2read:
        run_structural_postproc(output_path, result, node)

if __name__ == '__main__':
    main()