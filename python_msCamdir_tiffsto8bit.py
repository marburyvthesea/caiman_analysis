from skimage import io
from tifffile import imsave
import glob
from tqdm import tqdm 
import numpy as np 

dir_path = sys.argv[1]


for img_to_convert in tqdm(glob.glob('/projects/b1118/miniscope/data/v4/JJM/RotaryWheel/DIO_r2_1/Day1/2021_11_18/17_31_56/My_V4_Miniscope/*tif')):
    #load image as tiff stack
    print(img_to_convert)
    try:
        tiff_stack = io.imread(img_to_convert)
    except IndexError:
        print('error with', img_to_convert)
        pass
    #check if rgb
    if len(np.shape(tiff_stack))>3:
        #split into r,g,b channels 
        r = tiff_stack[:, :, :, 0]
        g = tiff_stack[:, :, :, 1]
        b = tiff_stack[:, :, :, 2]
        #scale pixel values to gray
        gray_image = (r*0.299 + g*0.587 +b*0.114)
        imsave(img_to_convert, gray_image)
    else:
        imsave(img_to_convert, tiff_stack)

print('converted to 8 bit')