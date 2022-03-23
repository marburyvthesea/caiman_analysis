#!/bin/bash
#SBATCH -A p30771
#SBATCH -p short 
#SBATCH -t 00:20:00
#SBATCH -o ./logfiles/slurm_avi_to_tiff.%x-%j.out # STDOUT
#SBATCH --job-name="slurm_python_avi_to_tiff"
#SBATCH --mem=20G
#SBATCH -N 1
#SBATCH -n 5 


module purge all

cd ~

# Inputs from command line
# add final '/' in dir_path
DIR_path=$1
# switch for v4, type v3 or v4 at command line
INPUT_v4=$2

#add project directory to PATH
export PATH=$PATH/projects/p30771/

#load modules to use
module load python/anaconda3.6

#need to cd to load conda environment

cd pythonenvs
cd CaImAn
source activate caiman_with_tables

#cd to script directory
cd /home/jma819/caiman_quest/demos/notebooks/caiman_analysis

#run script

echo "converting to tiffs"
python python_msCamdir_totiff.py $DIR_path $INPUT_v4
echo "converting to 8bit"
python python_msCamdir_tiffsto8bit.py $DIR_path

echo "finished conversion"

