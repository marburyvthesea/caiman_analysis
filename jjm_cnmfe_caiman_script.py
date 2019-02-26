
# coding: utf-8

# In[1]:


##script to run caiman cnmfe 
#pass folder containing motion corrected mmpap file concactenated in C order as sys arg 1
#motion corrected mmpap file concactenated in C order as sys arg 2

##!/Users/johnmarshall/miniconda3/envs/caiman/bin/python3
try:
    get_ipython().magic(u'load_ext autoreload')
    get_ipython().magic(u'autoreload 2')
    get_ipython().magic(u'matplotlib qt')
except:
    pass

import logging
import matplotlib.pyplot as plt
import numpy as np

logging.basicConfig(format=
                          "%(relativeCreated)12d [%(filename)s:%(funcName)20s():%(lineno)s] [%(process)d] %(message)s",
                    # filename="/tmp/caiman.log",
                    level=logging.DEBUG)

import caiman as cm
from caiman.source_extraction import cnmf
from caiman.utils.utils import download_demo
from caiman.utils.visualization import inspect_correlation_pnr
from caiman.motion_correction import MotionCorrect
from caiman.source_extraction.cnmf import params as params
from caiman.utils.visualization import plot_contours, nb_view_patches, nb_plot_contour
import cv2
import sys
import h5py

try:
    cv2.setNumThreads(0)
except:
    pass
import bokeh.plotting as bpl
bpl.output_notebook()

#%% start a cluster for parallel processing (if a cluster already exists it will be closed and a new session will be opened)
if 'dview' in locals():
    cm.stop_server(dview=dview)
c, dview, n_processes = cm.cluster.setup_cluster(
    backend='local', n_processes=None, single_thread=False)


# In[ ]:


## path to motion corrected tif file
folder = '/projects/p30771/miniscope/data/GRIN011/1_24_2019/H10_M19_S59/TIFs/full_movie_caiman_analysis/'
#mc_file = 'memmap__d1_480_d2_752_d3_1_order_C_frames_202_.mmap'

memory_map_file = sys.argv[1]


# In[4]:


# load memory mappable file
print('loading file:')
print(memory_map_file)
Yr, dims, T = cm.load_memmap(memory_map_file)
images = Yr.T.reshape((T,) + dims, order='F')

#
opts = params.CNMFParams(params_dict={})
#
bord_px = 0
# parameters for source extraction and deconvolution
p = 1               # order of the autoregressive system
K = None            # upper bound on number of components per patch, in general None
gSig = (3, 3)       # gaussian width of a 2D gaussian kernel, which approximates a neuron
gSiz = (13, 13)     # average diameter of a neuron, in general 4*gSig+1
Ain = None          # possibility to seed with predetermined binary masks
merge_thresh = .7   # merging threshold, max correlation allowed
rf = 40             # half-size of the patches in pixels. e.g., if rf=40, patches are 80x80
stride_cnmf = 20    # amount of overlap between the patches in pixels
#                     (keep it at least large as gSiz, i.e 4 times the neuron size gSig)
tsub = 2            # downsampling factor in time for initialization,
#                     increase if you have memory problems
ssub = 1            # downsampling factor in space for initialization,
#                     increase if you have memory problems
#                     you can pass them here as boolean vectors
low_rank_background = None  # None leaves background of each patch intact,
#                     True performs global low-rank approximation if gnb>0
gnb = 0             # number of background components (rank) if positive,
#                     else exact ring model with following settings
#                         gnb= 0: Return background as b and W
#                         gnb=-1: Return full rank background B
#                         gnb<-1: Don't return background
nb_patch = 0        # number of background components (rank) per patch if gnb>0,
#                     else it is set automatically
min_corr = .8       # min peak value from correlation image
min_pnr = 10        # min peak to noise ration from PNR image
ssub_B = 2          # additional downsampling factor in space for background
ring_size_factor = 1.4  # radius of ring is gSiz*ring_size_factor

opts.change_params(params_dict={'method_init': 'corr_pnr',  # use this for 1 photon
                                'K': K,
                                'gSig': gSig,
                                'gSiz': gSiz,
                                'merge_thresh': merge_thresh,
                                'p': p,
                                'tsub': tsub,
                                'ssub': ssub,
                                'rf': rf,
                                'stride': stride_cnmf,
                                'only_init': True,    # set it to True to run CNMF-E
                                'nb': gnb,
                                'nb_patch': nb_patch,
                                'method_deconvolution': 'oasis',       # could use 'cvxpy' alternatively
                                'low_rank_background': low_rank_background,
                                'update_background_components': True,  # sometimes setting to False improve the results
                                'min_corr': min_corr,
                                'min_pnr': min_pnr,
                                'normalize_init': False,               # just leave as is
                                'center_psf': True,                    # leave as is for 1 photon
                                'ssub_B': ssub_B,
                                'ring_size_factor': ring_size_factor,
                                'del_duplicates': True,                # whether to remove duplicates from initialization
                                'border_pix': bord_px})                # number of pixels to not consider in the borders)

# compute some summary images (correlation and peak to noise)
#cn_filter, pnr = cm.summary_images.correlation_pnr(images, gSig=gSig[0], swap_dim=False) # change swap dim if output looks weird, it is a problem with tiffile


# In[5]:

#inspect_correlation_pnr(cn_filter, pnr)


# In[6]:


# print parameters set above, modify them if necessary based on summary images
#print(min_corr) # min correlation of peak (from correlation image)
#print(min_pnr)  # min peak to noise ratio


# In[ ]:


cnm = cnmf.CNMF(n_processes=n_processes, dview=dview, Ain=Ain, params=opts)


# In[ ]:


print('running cnmfe')
cnm.fit(images)


# In[ ]:

print('finished fitting')

# get contours of found components
Cn = cm.local_correlations(images.transpose(1,2,0))
Cn[np.isnan(Cn)] = 0


# In[ ]:


#%% COMPONENT EVALUATION
# the components are evaluated in three ways:
#   a) the shape of each component must be correlated with the data
#   b) a minimum peak SNR is required over the length of a transient
#   c) each shape passes a CNN based classifier

min_SNR = 3            # adaptive way to set threshold on the transient size
r_values_min = 0.85    # threshold on space consistency (if you lower more components
#                        will be accepted, potentially with worst quality)
cnm.params.set('quality', {'min_SNR': min_SNR,
                           'rval_thr': r_values_min,
                           'use_cnn': False})
cnm.estimates.evaluate_components(images, cnm.params, dview=dview)

print(' ***** ')
print('Number of total components: ', len(cnm.estimates.C))
print('Number of accepted components: ', len(cnm.estimates.idx_components))


# In[ ]:


hf = h5py.File(folder + 'output_data.h5', 'w')
hf.create_dataset('A', data=cnm.estimates.A.toarray())
hf.create_dataset('C', data=cnm.estimates.C)
hf.close()

