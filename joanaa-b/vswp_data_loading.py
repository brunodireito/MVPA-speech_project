import nilearn
from nilearn import plotting
from nilearn import datasets
from nilearn import image
from nilearn.image import mean_img
from nilearn.image import index_img
from nilearn.glm.first_level import make_first_level_design_matrix
from nilearn.glm.first_level import FirstLevelModel
from nilearn.plotting import plot_design_matrix

from timeit import default_timer as timer

import numpy as np
import pandas as pd
import nibabel as nib

import os


## EVENTS

# Set variables
ROOT_DATA='/Users/home/Documents/BIDS/DATA_joanaab'
#ROOT_DATA='/home/brunomiguel/Documents/data/BIDS/'
SUB='sub-0001'
SES='ses-001'
TASK='innerspeech'
RUN='run-03'


# data folder
data_path=os.path.join(ROOT_DATA)
print('The data is in this folder - ' + data_path)

# project folder
ROOT_PROJECT="/Users/home/Documents/GitHub/MVPA-speech_project"


fmri_img=os.path.join(data_path,
                      SUB + '_' + SES + '_task-' + TASK + '_'+ RUN +'_bold_pp_standard.nii.gz')

dataset_shape=(image.load_img(fmri_img).shape)

tr = 2  # repetition time is ? second

n_scans = dataset_shape[3]  # the acquisition comprises ?? scans

frame_times = np.arange(n_scans) * tr  # here are the correspoding frame times

# load events.tsv
events_PATH=os.path.join(data_path,
                          SUB + '_' + SES + 
                          '_task-' + TASK + '_'+ RUN + '_events.tsv')

events_df = pd.read_csv(events_PATH, sep='\t', na_values="n/a")


## DESIGN MATRICES
hrf_model='spm'
design_matrix = make_first_level_design_matrix(frame_times, events_df,
                                    drift_model='polynomial', drift_order=3,
                                    hrf_model=hrf_model)


first_level_model = FirstLevelModel(tr)
first_level_model = first_level_model.fit(fmri_img, events=events_df)
design_matrix = first_level_model.design_matrices_[0]
plot_design_matrix(design_matrix)

contrast_matrix = np.eye(design_matrix.shape[1])
basic_contrasts = dict([(column, contrast_matrix[i])
                        for i, column in enumerate(design_matrix.columns)])

fmri_glm4mask = FirstLevelModel()
fmri_glm4mask = fmri_glm4mask.fit(fmri_img, design_matrices=design_matrix)

## BETA SERIES
onset=[]
duration=[]
trialtype=[]

labels=[]

onsett=0
evtt=0

for idx in range(len(events_df)-1):
    block_event=events_df.loc[idx]

    num_evts=block_event['duration']/tr

    for evt in range(int(num_evts)):

        onset.append(onsett)
        onsett+=tr

        duration.append(tr)

        trialtype.append(evtt)
        evtt+=1

        labels.append(block_event['trial_type'])


events_bs = pd.DataFrame({'trial_type': trialtype,
                       'onset': onset,
                       'duration': duration})


df = pd.DataFrame(labels)

labels_fn=os.path.join(SUB + '_' + SES + '_task-' + TASK + '_'+ RUN +'_labels.csv')

df.to_csv(labels_fn)

first_level_model = FirstLevelModel(tr)
first_level_model = first_level_model.fit(fmri_img, events=events_bs)
design_matrix_b_series = first_level_model.design_matrices_[0]
plot_design_matrix(design_matrix_b_series)
design_matrix_b_series.drop({'drift_1', 'drift_2', 'drift_3', 'drift_4', 'drift_5', 'drift_6', 'drift_7', 'drift_8', 'drift_9', 'drift_10', 'constant'}, axis='columns', inplace=True)

## Contrasts

contrast_matrix_b_series = np.eye(design_matrix_b_series.shape[1])
basic_contrasts_b_series = dict([(column, contrast_matrix_b_series[i]) for i, column in enumerate(design_matrix_b_series.columns)])
    

fmri_glm = FirstLevelModel()
fmri_glm = fmri_glm.fit(fmri_img, design_matrices=design_matrix_b_series)

mean_image = mean_img(fmri_img)
z_map=[]

for idx in range(len(basic_contrasts_b_series)):
    z_map.append(fmri_glm.compute_contrast(basic_contrasts_b_series[idx], output_type='z_score'))
    
contrast_matrix_b_series = np.eye(design_matrix_b_series.shape[1])
basic_contrasts_b_series = dict([(column, contrast_matrix_b_series[i]) for i, column in enumerate(design_matrix_b_series.columns)])
    

fmri_glm = FirstLevelModel()
fmri_glm = fmri_glm.fit(fmri_img, design_matrices=design_matrix_b_series)

mean_image = mean_img(fmri_img)
z_map=[]

for idx in range(len(basic_contrasts_b_series)):
    z_map.append(fmri_glm.compute_contrast(basic_contrasts_b_series[idx], output_type='z_score'))
    

bs_fn=os.path.join( SUB + '_' + SES + '_task-' + TASK + '_'+ RUN +'_bold_bs.nii.gz')

img4D=nilearn.image.concat_imgs(z_map)
img4D.to_filename(bs_fn)