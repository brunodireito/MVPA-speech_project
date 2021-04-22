#!/bin/sh

ROOT_RAWDATA='/media/brunomiguel/LANGLYBACKU/DATA/DATA_Carlos_Phonos'
ROOT_OUPUT='/home/brunomiguel/Documents/data/BIDS'

heudiconv -d $ROOT_RAWDATA/{subject}/*/DATA/*.dcm \
-s AnaSapalo \
-c none \
-f convertall \
-o $ROOT_OUPUT \
--overwrite
