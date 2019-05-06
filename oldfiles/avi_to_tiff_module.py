import av
import glob
import sys
from tqdm import tqdm

def convert_to_tiff(avi_file):
    container = av.open(avi_file)
    frames = []
    for packet in container.demux():
        for frame in packet.decode():
            frames.append(frame.to_image())  # PIL/Pillow image
    frames[0].save(avi_file.rstrip('.avi')+'.tif', save_all=True, append_images=frames[1:])
    return()
    



