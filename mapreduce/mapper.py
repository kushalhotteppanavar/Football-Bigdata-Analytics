#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)
for row in reader:
    if not row or row[0] == "match_id" or len(row) < 12:
        continue
    try:
        player = row[1].strip()
        team = row[2].strip()
        pos = row[3].strip()
        mins = int(row[4])
        goals = int(row[5])
        assists = int(row[6])
        passes_comp = int(row[7])
        passes_att = int(row[8])
        tackles = int(row[9])
        shots = int(row[10])
        shots_ot = int(row[11])
        
        key = f"{player}|{team}|{pos}"
        val = f"1,{mins},{goals},{assists},{passes_comp},{passes_att},{tackles},{shots},{shots_ot}"
        print(f"{key}\t{val}")
    except ValueError:
        continue
