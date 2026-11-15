#!/usr/bin/env python3
import sys

current_key = None
totals = [0] * 9

def emit_result(key, stats):
    player, team, pos = key.split("|")
    matches, mins, goals, assists, p_comp, p_att, tackles, shots, shots_ot = stats
    
    pass_acc = round((p_comp / p_att) * 100, 2) if p_att > 0 else 0.0
    shot_acc = round((shots_ot / shots) * 100, 2) if shots > 0 else 0.0
    
    per_90_factor = (mins / 90.0) if mins > 0 else 1.0
    raw_points = (goals * 5.0) + (assists * 3.5) + (tackles * 1.5) + (shots_ot * 1.0) + (p_comp * 0.05)
    perf_score = round(raw_points / per_90_factor, 2)
    
    print(f"{player},{team},{pos},{matches},{mins},{goals},{assists},{p_comp},{p_att},{pass_acc},{tackles},{shots},{shots_ot},{shot_acc},{perf_score}")

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    key, val = line.split("\t", 1)
    nums = [int(x) for x in val.split(",")]
    
    if current_key == key:
        for i in range(9):
            totals[i] += nums[i]
    else:
        if current_key:
            emit_result(current_key, totals)
        current_key = key
        totals = nums

if current_key:
    emit_result(current_key, totals)
