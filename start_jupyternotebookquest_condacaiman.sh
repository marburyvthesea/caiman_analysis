#!/bin/bash

module load python/anaconda3.6
source activate caiman

cd /home/jma819

jupyter notebook --port=$1 --no-browser
