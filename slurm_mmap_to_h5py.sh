#!/bin/bash
#SBATCH -A p30771
#SBATCH -p short
#SBATCH -t 00:30:00
#SBATCH -o ./logfiles/slurm.%x-%j.out # STDOUT
#SBATCH --job-name="mmap_to_h5py"
#SBATCH -N 1
#SBATCH -n 3
#SBATCH --mem=90G

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

#inputs are path to directory containing files, number or processors to use and length of batches to concactenate into one file

python mmap_to_h5py.py /projects/p30771/miniscope/data/GRIN032/H16_M49_S22/mmap/test/ 2 1 
