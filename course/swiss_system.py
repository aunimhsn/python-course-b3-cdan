import json

# 1. Lire le fichier players.json
with open('./data/players.json', 'r') as f:
    players:list = json.load(f)

# 2. Trier mes joueurs par points d'elo
players_sorted = sorted(players, key = lambda player:player['elo_points'])

# 3. Faire les deux groupes
middle = len(players)//2
s1 = players_sorted[:middle]
s2 = players_sorted[middle:]

versus:list = [] 
for i in range(0, middle):
    versus.append([s1[i], s2[i]])

# 4. Création d'un nouveau fichier json avec les matchs
with open("./data/matches.json", "w") as f:
    json.dump(versus, f, indent=4)




