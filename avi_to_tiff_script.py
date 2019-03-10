
# coding: utf-8

# In[1]:


import av
import glob
import sys



# In[6]:



def convert_to_tiff(avi_file):
    container = av.open(avi_file)
    frames = []
    for packet in container.demux():
        for frame in packet.decode():
            frames.append(frame.to_image())  # PIL/Pillow image
    frames[0].save(avi_file.rstrip('.avi')+'.tif', save_all=True, append_images=frames[1:])
    return()
    


# In[ ]:


folder_name = sys.argv[1]
files = glob.glob(folder_name+'/*.avi')
for file in files:
	print('converting')
	print(file)
	convert_to_tiff(file)

