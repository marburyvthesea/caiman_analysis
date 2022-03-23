import imageio
import glob
from tqdm import tqdm 
import numpy as np 
import sys

dir_path = sys.argv[1]


for img_to_convert in tqdm(glob.glob(dir_path+'/*tif')):
     #load image as tiff stack
     print(img_to_convert)
     try:
         tiff_stack = imageio.mimread(img_to_convert, memtest=False)
     except IndexError:
          print('error with', img_to_convert)
          pass
     #check if rgb
     if len(np.shape(tiff_stack))>3:
        #split into r,g,b channels 
          gray_stack = np.empty([np.shape(tiff_stack[:])[0],
                             np.shape(tiff_stack[:])[1],
                             np.shape(tiff_stack[:])[2]],
                             tiff_stack[1].dtype)
          for i in tqdm(range(np.shape(tiff_stack[:])[0])):
               frame = tiff_stack[i][:][:][:]
               r = frame[:,:,0]
               g = frame[:,:,1]
               b = frame[:,:,2]
	#scale pixel values to gray
               gray_image = (r*0.299 + g*0.587 +b*0.114)
               gray_stack[i]=gray_image
	
          imageio.mimwrite(img_to_convert, gray_stack)
     else:
          imageio.mimwrite(img_to_convert, tiff_stack)

print('converted to 8 bit')
