#!/usr/bin/env python
import sys

subj_map = {
   'AndreiaVerdade': '0001',
   'BrunoDireito': '0002',
   'CarlosFerreira': '0003',
   'CarolinaTravassos': '0004',
   'CatarinaDuarte': '0005',
}


sid = sys.argv[-1]
if sid in subj_map:
    print(subj_map[sid])
