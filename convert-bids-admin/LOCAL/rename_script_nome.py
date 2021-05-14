#!/usr/bin/env python
import sys

subj_map = {
   'JoaoPereira': '0001',
   'AnaSapalo': '0002',
   'NadiaAlves': '0003',
   'RenatoFonseca': '0004',
   'RicardoSilva': '0005'
}


sid = sys.argv[-1]
if sid in subj_map:
    print(subj_map[sid])
