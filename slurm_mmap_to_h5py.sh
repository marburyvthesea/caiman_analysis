#!/bin/bash
#SBATCH -A p30771
#SBATCH -p short
#SBATCH -t 01:00:00
#SBATCH -o ./logfiles/slurm.%x-%j.out # STDOUT
#SBATCH --job-name="mmap_to_h5py"
#SBATCH -N 1
#SBATCH -n 5
#SBATCH --mem=90G

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

#inputs are path to directory containing files, number or processors to use and length of batches to concactenate into one file

python mmap_to_h5py.py /projects/p30771/miniscope/data/GRIN033/H13_M42_S33/mmap00_05/ 5 1 
