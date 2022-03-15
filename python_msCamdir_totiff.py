
import imageio
import os
import numpy as np
import sys
from tqdm import tqdm
from skimage import io

dir_path = sys.argv[1]
v4 = sys.argv[2]

if v4=='v4':
    avi_files = [dir_path + fname for fname in os.listdir(dir_path) if 'msCam' in fname and 'avi' in fname]
elif v4=='v3':
    avi_files = [dir_path + fname for fname in os.listdir(dir_path) if 'avi' in fname]

for path_to_video in tqdm(avi_files):
    print('converting to tiff')
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

print('files converted to tiffs')


