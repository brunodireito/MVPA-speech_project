import nilearn
from nilearn import plotting
from nilearn import datasets
from nilearn import image
from nilearn.image import mean_img
from nilearn.image import index_img
from nilearn.glm.first_level import make_first_level_design_matrix
from nilearn.plotting import plot_design_matrix


import numpy as np
import pandas as pd
import os


# Set variables
ROOT_DATA='/Users/home/Documents/BIDS/'
#ROOT_DATA='/home/brunomiguel/Documents/data/BIDS/'
SUB='sub-0001'
SES='ses-001'
TASK='innerspeech'
RUN='run-02'


# data folder
data_path=os.path.join(ROOT_DATA, SUB, SES)
print('The data is in this folder - ' + data_path)

# project folder
ROOT_PROJECT="/Users/home/Documents/GitHub/MVPA-speech_project"


# Load mask
mask_fn=os.path.join( SUB + '_' + SES + '_task-' + TASK + '_'+ RUN +'_mask.nii.gz')
brain_mask= nilearn.image.load_img(mask_fn)

# Load data
bs_fn=os.path.join( SUB + '_' + SES + '_task-' + TASK + '_'+ RUN +'_bold_bs.nii.gz')
bs_maps= nilearn.image.load_img(bs_fn)


# Load labels
labels=np.genfromtxt('labels.csv',dtype='str')


# Decoding
from sklearn.model_selection import KFold
from nilearn.decoding import Decoder 

decoder = Decoder(estimator='svc',cv=3, mask=brain_mask, standardize=True)
decoder.fit(bs_maps, labels)

for i, (param, cv_score) in enumerate(zip(decoder.cv_params_,
                                          decoder.cv_scores_)):
    with open('results.txt', 'w') as f:
        print("Fold %d | Best SVM parameter: %.1f with score: %.3f" % (i + 1, param, cv_score),file=f)