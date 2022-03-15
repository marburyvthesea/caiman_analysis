#!/bin/bash

#use $input_folder as variable containing session name
#also animal name
#take inputs from command line

#i.e. input_folder=H17_M46_S35
#i.e. animal=GRIN012

input_folder=$1
#animal

#create new timestampeddir

today=$(date +%m%d%y)

#create directory

mkdir $input_folder $input_folder'_normcorr_'$today

#move unnneeded files
mv $input_folder/*tif $input_folder'_normcorr_'$today
mv $input_folder/*order_F_frames* $input_folder'_normcorr_'$today
mv $input_folder/memmap__* $input_folder'_normcorr_'$today

#slower option
#cp -r $input_folder $input_folder'_normcorr_'$today


#for globus transfer 

#quest=d5990400-6d04-11e5-ba46-22000b92c6ec
#resfiles=8f796c9e-f5c8-11e5-9842-22000b9da45e


#globus transfer $quest:/projects/b1118/miniscope/data/$animal/$folder $resfiles:~/rdss/jma819/fsmresfiles/Projects/JJM/MiniscopeMovies/analysis/$animal/ --recursive
