#!/bin/sh

ROOT_RAWDATA='/media/brunomiguel/LANGLYBACKU/DATA/DATA_Carlos_Phonos'
ROOT_OUPUT='/home/brunomiguel/Documents/data/BIDS'
ROOT_CODE='/home/brunomiguel/Documents/GitHub/MVPA-speech_project/convert-bids-admin/LOCAL/'

heudiconv -d $ROOT_RAWDATA/{subject}/*/DATA/*.dcm \
--anon-cmd $ROOT_CODE//rename_script.py \
-s NadiaAlves \
--ses 001 \
-f $ROOT_CODE/heuristic.py \
-c dcm2niix -b \
-o $ROOT_OUPUT \
--overwrite
