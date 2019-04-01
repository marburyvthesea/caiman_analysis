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

#

python mmap_to_h5py.py /projects/p30771/miniscope/data/GRIN011/1_24_2019/H10_M19_S59/TIFs/caiman_analysis/memmap_0008_d1_480_d2_752_d3_1_order_C_frames_1000_.mmap

