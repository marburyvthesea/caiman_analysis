#!/bin/bash
#SBATCH -A p30771
#SBATCH -p short
#SBATCH -t walltime=04:00:00
#SBATCH --job-name="slurm_matlab_cnmfe_run"
#SBATCH -N 1
#SBATCH -n 2


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

python mmap_to_h5py.py /projects/p30771/miniscope/data/cellregtest/motion_corrected 2 1
