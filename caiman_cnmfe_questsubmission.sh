#!/bin/bash
#MSUB -A p30771
#MSUB -q short
#MSUB -l walltime=04:00:00
#MSUB -M johnjmarshall@u.northwestern.edu
#MSUB -j oe
#MSUB -N caiman_cnmfe_analysis
#MSUB -l nodes=1:ppn=20
cd ~

add project directory to PATH
export PATH=$PATH/projects/p30771/

#load modules to use
module load python/anaconda3.6 

#need to cd to load conda environment

cd pythonenvs
cd CaImAn
source activate caiman

#need to cd to module directory

cd /home/jma819/caiman_data/demos/notebooks/caiman_analysis

#run normcorr

#echo "loading folder: $1"
#echo "file: $2 $3"
#echo "through: $4"

#echo "running motion correction"

python jjm_cnmfe_caiman_script.py /projects/p30771/miniscope/data/GRIN012/3_8_2019/H16_M57_S23/TIFs/mmap_files/memmap__d1_480_d2_752_d3_1_order_C_frames_9000_.mmap

echo "finished cnmfe"
