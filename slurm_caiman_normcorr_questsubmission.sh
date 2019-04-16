#!/bin/bash
#SBATCH -A p30771
#SBATCH -p normal
#SBATCH -t walltime=12:00:00
#SBATCH --job-name="slurm_normcorr"
#SBATCH -N 1
#SBATCH -n 12

module purge all

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

#run normcorr

echo "loading folder: $1"
echo "file: $2 $3"
echo "through: $4"

echo "running motion correction"

# inputs are folder path, regular expression in file names(e.g. msCam), start and end files to correct, number of processors to run
python caiman_motion_correction_normcorr_e_script.py /projects/p30771/miniscope/data/GRIN013/H11_M46_S9 msCam 1 39 12

echo "finished motion correction"
