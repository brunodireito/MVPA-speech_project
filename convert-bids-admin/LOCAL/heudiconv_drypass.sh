#!/bin/sh

heudiconv -d /media/brunomiguel/LANGLYBACKU/DATA/DATA_Carlos_Phonos/{subject}/*/DATA/*.dcm \
-s AnaSapalo \
-c none \
-f convertall \
-o /home/brunomiguel/Documents/data/BIDS \
--overwrite
