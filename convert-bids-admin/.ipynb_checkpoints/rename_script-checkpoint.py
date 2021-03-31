#!/usr/bin/env python
import sys

subj_map = {
   'JoaoPereira': '0001'
}

sid = sys.argv[-1]
if sid in subj_map:
    print(subj_map[sid])
