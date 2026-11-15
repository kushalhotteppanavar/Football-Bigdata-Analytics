import csv
import os
import random

players = [
    ("Erling Haaland", "Man City", "FW"), ("Kevin De Bruyne", "Man City", "MF"),
    ("Rodri", "Man City", "MF"), ("Phil Foden", "Man City", "FW"),
    ("Mohamed Salah", "Liverpool", "FW"), ("Virgil van Dijk", "Liverpool", "DF"),
    ("Trent Alexander-Arnold", "Liverpool", "DF"), ("Alexis Mac Allister", "Liverpool", "MF"),
    ("Bukayo Saka", "Arsenal", "FW"), ("Martin Odegaard", "Arsenal", "MF"),
    ("Declan Rice", "Arsenal", "MF"), ("William Saliba", "Arsenal", "DF"),
    ("Jude Bellingham", "Real Madrid", "MF"), ("Vinicius Junior", "Real Madrid", "FW"),
    ("Kylian Mbappe", "Real Madrid", "FW"), ("Federico Valverde", "Real Madrid", "MF"),
    ("Harry Kane", "Bayern Munich", "FW"), ("Jamal Musiala", "Bayern Munich", "MF"),
    ("Joshua Kimmich", "Bayern Munich", "MF"), ("Lamine Yamal", "Barcelona", "FW"),
    ("Pedri", "Barcelona", "MF"), ("Robert Lewandowski", "Barcelona", "FW"),
    ("Lautaro Martinez", "Inter Milan", "FW"), ("Nicolo Barella", "Inter Milan", "MF"),
    ("Son Heung-min", "Tottenham", "FW"), ("Bruno Fernandes", "Man United", "MF")
]

os.makedirs("data", exist_ok=True)
output_file = "data/football_match_logs.csv"
random.seed(42)

with open(output_file, mode="w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "match_id", "player_name", "team", "position",
        "minutes_played", "goals", "assists", "passes_completed",
        "passes_attempted", "tackles", "shots", "shots_on_target"
    ])
    for match_id in range(1, 50001):
        player, team, pos = random.choice(players)
        mins = random.randint(45, 90)
        
        if pos == "FW":
            goals = random.choices([0, 1, 2, 3], weights=[55, 30, 12, 3])[0]
            assists = random.choices([0, 1, 2], weights=[70, 22, 8])[0]
            passes_att = random.randint(20, 50)
            tackles = random.randint(0, 3)
            shots = random.randint(2, 7)
        elif pos == "MF":
            goals = random.choices([0, 1, 2], weights=[75, 20, 5])[0]
            assists = random.choices([0, 1, 2], weights=[60, 30, 10])[0]
            passes_att = random.randint(45, 95)
            tackles = random.randint(1, 6)
            shots = random.randint(1, 4)
        else:  # DF
            goals = random.choices([0, 1], weights=[92, 8])[0]
            assists = random.choices([0, 1], weights=[85, 15])[0]
            passes_att = random.randint(50, 100)
            tackles = random.randint(2, 8)
            shots = random.randint(0, 2)
            
        passes_comp = int(passes_att * random.uniform(0.78, 0.96))
        shots_ot = random.randint(0, shots)
        
        writer.writerow([
            f"M{match_id:05d}", player, team, pos,
            mins, goals, assists, passes_comp, passes_att, tackles, shots, shots_ot
        ])

print(f"Generated 50,000 match records at {output_file}")
