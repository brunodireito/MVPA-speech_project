#!/bin/sh
ROOT_RAWDATA="/media/brunomiguel/TOSHIBA\ EXT/DATA_Carlos_PhD_Final"
ROOT_OUPUT='/home/brunomiguel/Documents/data/BIDS_vswp'


heudiconv -d /media/brunomiguel/TOSHIBA\ EXT/DATA_Carlos_PhD_Final/{subject}/*/DATA/*.dcm \
-s BrunoDireito \
-c none \
-f convertall \
-o $ROOT_OUPUT \
--overwrite
