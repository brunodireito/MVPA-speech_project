#!/bin/sh

heudiconv -d /media/brunomiguel/LANGLYBACKU/DATA/DATA_Carlos_Phonos/{subject}/*/DATA/*.dcm \
--anon-cmd /home/brunomiguel/Documents/GitHub/MVPA-speech_project/convert-bids-admin/LOCAL/rename_script.py \
-s NadiaAlves \
--ses 001 \
-f /home/brunomiguel/Documents/GitHub/MVPA-speech_project/convert-bids-admin/LOCAL/heuristic.py \
-c dcm2niix -b \
-o /home/brunomiguel/Documents/data/BIDS \
--overwrite
