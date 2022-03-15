
import imageio
import os
import numpy as np
import sys

dir_path = sys.argv[1]


avi_files = [dir_path + fname for fname in os.listdir(dir_path) if 'msCam' in fname and 'avi' in fname]

for path_to_video in avi_files:
    
    print(path_to_video.split('/')[-1])
    joint = ('/')
    savepath = joint.join(path_to_video.split('/')[0:-1])
    savepath = savepath+'/'+path_to_video.split('/')[-2]+path_to_video.split('/')[-1].strip('.avi')+'.tif'
    print(savepath) 
    try:	
        video_loaded = imageio.get_reader(path_to_video)
        imageio.mimwrite(savepath, video_loaded)
    except OSError: 
        print('error in:'+path_to_video.split('/')[-1])
        pass


