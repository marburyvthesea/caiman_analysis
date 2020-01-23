#!/bin/bash
#MSUB -A p30771
#MSUB -q short
#MSUB -l walltime=4:00:00
#MSUB -M johnjmarshall@u.northwestern.edu
#MSUB -j oe
#MSUB -N mmap_to_h5py
#MSUB -l nodes=1:ppn=4


cd ~

#add project directory to PATH
export PATH=$PATH/projects/p30771/

#load modules to use
module load python/anaconda3.6 

#need to cd to load conda environment

cd pythonenvs
cd CaImAn
source activate caiman

#need to cd to module directory

cd /home/jma819/caiman_data/demos/notebooks/caiman_analysis

# file path, num processors, length to concat to 

python mmap_to_h5py.py /projects/p30771/miniscope/data/GRIN018/H17_M41_S43/mmap_C_order/ 4 5 
