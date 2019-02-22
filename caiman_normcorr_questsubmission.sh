#!/bin/bash
#MSUB -A p30771
#MSUB -q short
#MSUB -l walltime=04:00:00
#MSUB -M johnjmarshall@u.northwestern.edu
#MSUB -j oe
#MSUB -N normcorr_caiman
#MSUB -l nodes=1:ppn=12
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

cd /home/jma819/caimandata/

#run normcorr

echo "loading folder: $1"
echo "file: $2 $3"
echo "through: $4"


python caiman_motion_correction_normcorr_e_script.py $1 $2 $3 $4 
