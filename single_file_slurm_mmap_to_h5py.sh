#!/bin/bash
#SBATCH -A p30771
#SBATCH -p short
#SBATCH -t 00:30:00
#SBATCH -o ./logfiles/slurm.%x-%j.out # STDOUT
#SBATCH --job-name="mmap_to_h5py"
#SBATCH -N 1
#SBATCH -n 3
#SBATCH --mem=80G


#file to convert

INPUT_file=$1

cd ~

#add project directory to PATH
export PATH=$PATH/projects/p30771/

#load modules to use
module load python/anaconda3.6 

#need to cd to load conda environment

cd /projects/p30771/pythonenvs/CaImAn/
source activate caiman

#need to cd to module directory

cd /home/jma819/caiman_quest/demos/notebooks/caiman_analysis

#inputs are file

python single_file_mmap_to_h5py.py $INPUT_file 
