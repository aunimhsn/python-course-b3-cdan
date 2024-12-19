import json

# 0. Lire le fichier json
def read_json_file(file_path:str) -> list[dict]:
    with open(file_path) as f:
        players = json.load(f)

    return players


# 1. Trier les joueurs par points d'elo
sorted_players = sorted(read_json_file('./data/players.json'), key=lambda d: d['elo_points'])

# 2. Création des deux groupes
group_1 = sorted_players[0:len(sorted_players)//2]
group_2 = sorted_players[len(sorted_players)//2:len(sorted_players)]

# 3. Création des paires / matchs
matches = []
for i in range(0, len(sorted_players)//2):
    matches.append([group_1[i], group_2[i]])

# 4. Création d'un nouveau fichier json avec les matchs
with open("./data/matches.json", "w") as f:
    json.dump(matches, f, indent=4)