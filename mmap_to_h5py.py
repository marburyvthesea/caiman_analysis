import h5py as hd
import numpy as np
from tqdm import tqdm
import sys
import os
from caiman import mmapping as mmp


def caiman_mmap_to_hdf(array_from_mmap, dims):
	movie_by_frames = []
	for frame in tqdm(range(np.shape(array_from_mmap)[1])):
		movie_by_frames.append(array_from_mmap[:, frame].reshape([dims[1],dims[0]]).transpose())

	return(movie_by_frames)

def save_to_hdf(folder, mmap_fname, frames_to_save):

	output_fname = (folder + '/' + mmap_fname.rstrip('.mmap') + '_resized.h5')
	output_file = hd.File(output_fname, 'w')
	movie = output_file.create_dataset('motion_corrected', data = frames_to_save)
	output_file.close()

	return(output_fname)




path_to_mmap = sys.argv[1]

folder_path, mmap_path  = os.path.split(path_to_mmap)

frames, dims, T = mmp.load_memmap(path_to_mmap)

frames_array = np.array(frames)

movie_reshaped = caiman_mmap_to_hdf(frames_array, dims)

output_fname = save_to_hdf(folder_path, mmap_path, movie_reshaped)

print('saved file')
print(output_fname)

