#!./paraview-5.11.1/bin/pvpython
import sys
from postproc_pv import *
from structural_postproc import *
from cfg_reader import *

if len(sys.argv) < 4:
    print('Uso: ./main.py mfsim_cfg_file ct STR_NODE')
    print('----------')
    print('ex: ./main.py /home/MFSim/case.cfg 100 1')
    exit(1)

cfg_path = sys.argv[1]
ct = sys.argv[2]
node = sys.argv[3]

output_path = getOutputPath(cfg_path)
run_postproc(output_path, ct)
run_structural_postproc(output_path, node)