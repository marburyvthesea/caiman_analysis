#!/bin/bash
#SBATCH -A p30771
#SBATCH -p normal
#SBATCH -t 12:00:00
#SBATCH -o /home/jma819/caiman_quest/demos/notebooks/caiman_analysis/logfiles/slurm.%x-%j.out # STDOUT
#SBATCH --job-name="slurm_normcorr"
#SBATCH -N 1
#SBATCH -n 6
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

cd /home/jma819/caiman_quest/demos/notebooks/caiman_analysis

#run normcorr

INPUT_folder=$1
#INPUT_regexp=$2
#INPUT_start=$3
#INPUT_end=$4
INPUT_procs=6

echo "loading folder: $INPUT_folder"
echo "file: $INPUT_start"
echo "through: $INPUT_end"

echo "running motion correction"

# inputs are folder path, regular expression in file names(e.g. msCam), start and end files to correct, number of processors to run
python caiman_motion_correction_normcorr_e_script_directory.py $INPUT_folder $INPUT_procs

echo "finished motion correction"
