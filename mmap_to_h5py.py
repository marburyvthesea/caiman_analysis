import h5py as hd
import numpy as np
from tqdm import tqdm
import sys
import os
import glob
import multiprocessing as mp
from caiman import mmapping as mmp

def chunks(l, n):
	for i in range(0, len(l), n):
		yield(l[i:i+n])


def caiman_mmap_to_hdf(array_from_mmap, dims):
	movie_by_frames = []
	for frame in tqdm(range(np.shape(array_from_mmap)[1])):
		movie_by_frames.append(array_from_mmap[:, frame].reshape([dims[1],dims[0]]).transpose())
	movie_frames_array = np.array(movie_by_frames)
	return(movie_frames_array)

def save_to_hdf(folder, mmap_fname, frames_to_save):

	output_fname = (folder + '/' + mmap_fname.rstrip('.mmap') + '_resized.h5')
	output_file = hd.File(output_fname, 'w')
	movie = output_file.create_dataset('motion_corrected', data = frames_to_save)
	output_file.close()

	return(output_fname)


def convert_from_mmap(full_file_path):
	folder_path, mmap_path  = os.path.split(full_file_path)
	frames, dims, T = mmp.load_memmap(full_file_path)
	frames_array = np.array(frames)
	output_fname = save_to_hdf(folder_path, mmap_path, frames_array)
	print(mmap_path, 'done')
	return()

def concat_convert_from_mmap(full_file_paths, reshape=True):
	
	folder_path, mmap_path_start  = os.path.split(full_file_paths[0])
	mmap_path_end  = os.path.split(full_file_paths[-1])[1]
	mmap_path_out = mmap_path_start[:11] + mmap_path_end[:11]
	print('starting chunk with', mmap_path_start)

	#load 1st array 
	frames_0, dims, T = mmp.load_memmap(full_file_paths[0])
	concatenated = np.array(frames_0)
	dims_list = [dims]
	T_list = [T]

	#join arrays frame by frame
	for file_name in full_file_paths[1:]:
		frames, dims, T = mmp.load_memmap(file_name)
		concatenated = np.concatenate((concatenated, np.array(frames)), axis=1)
		dims_list.append(dims)
		T_list.append(T)

	if reshape:
		print('reshaping')
		reshaped = caiman_mmap_to_hdf(concatenated, dims)

	output_fname = save_to_hdf(folder_path, mmap_path_out, reshaped )
	print(mmap_path_out, 'done')
	return()

def run_convert_concat(files, num_procs, concat_size):
	#start pool
	chunk_list = list(chunks(files, concat_size))
	pool = mp.Pool(num_procs)
	print('starting pool with procs:', num_procs)
	print('starting pool with procs:', concat_size)
	print(chunk_list)
	pool.map(mmp_h5.concat_convert_from_mmap, [chunk for chunk in chunk_list])
	return()


folder_path = sys.argv[1]
processors = int(sys.argv[2])
num_files_to_combine = int(sys.argv[3])

files_list = glob.glob(folder_path+'/*.mmap')
run_convert_concat(files_list, processors, num_files_to_combine)






