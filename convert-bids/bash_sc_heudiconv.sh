docker run --rm -it \
-v /Users/home/Documents/data:/data:ro \
-v /Users/home/Documents/BIDS:/output \
nipy/heudiconv:latest \
-d /data/{subject}/{session}/*/DATA/*.dcm \
-f convertall \
-s JoaoPereira \
-ss 001 \
-c none  \
-o /output \
--overwrite


docker run --rm -it \
-v /Users/home/Documents/data:/data:ro \
-v /Users/home/Documents/BIDS:/output \
nipy/heudiconv:latest \
-d /data/{subject}/{session}/*/DATA/*.dcm \
--anon-cmd /output/code/rename_script.py \
-s JoaoPereira \
--ses 001 \
-f /output/code/heuristic.py \
-c dcm2niix -b \
-o /output/ \
--overwrite