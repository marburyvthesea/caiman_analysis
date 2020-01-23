#!/bin/bash
#SBATCH -A p30771
#SBATCH -p short
#SBATCH -t 4:00:00
#SBATCH -o ./logfiles/slurm.%x-%j.out # STDOUT
#SBATCH --job-name="slurm_normcorr"
#SBATCH -N 1
#SBATCH -n 12
#SBATCH --mem=20G

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

INPUT_folder=$1
INPUT_regexp=$2
INPUT_start=$3
INPUT_end=$4
INPUT_procs=$5

echo "loading folder: $INPUT_folder"
echo "file: $INPUT_start"
echo "through: $INPUT_end"

echo "running motion correction"

# inputs are folder path, regular expression in file names(e.g. msCam), start and end files to correct, number of processors to run
python caiman_motion_correction_normcorr_e_script.py $INPUT_folder $INPUT_regexp $INPUT_start $INPUT_end $INPUT_procs

echo "finished motion correction"
