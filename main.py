import requests
import json

#LINK TO API DOCUMENTATION: https://www.balldontlie.io/?shell#introduction


playerUrl = "https://www.balldontlie.io/api/v1/players?search="
averagesUrl = "https://www.balldontlie.io/api/v1/season_averages?season=2020&player_ids[]="


candidates = ["Joel Embiid", "Nikola Jokic", "Lebron James", "Damian Lillard", "Luka Doncic", "Stephen Curry", "Giannis Antetokounmpo", "James Harden", "Kawhi Leonard", "Donovan Mitchell"]
ids = []
seasonScores= []
mvpscore = 0

def formatjson(obj):
    text = json.dumps(obj.json(), sort_keys=True, indent=4)
    return(text)
    

for player in candidates:
    response = requests.get(playerUrl+str(player))
    sc = response.status_code
    if sc == 200:
        player = json.loads(formatjson(response))['data'][0]
        ids.append(player['id'])
    else:
        print("ERROR")

for plyrid in ids:
    response = requests.get(averagesUrl+str(plyrid))
    sc = response.status_code
    if sc == 200:
        stats = json.loads(formatjson(response))['data'][0]
        gmsc = stats["pts"] + (stats["fgm"]*0.4) + (stats["fga"]*( -0.7)) + ((stats["fta"]-stats["ftm"]) *(-0.4)) + (stats["oreb"]* 0.7) + (stats["dreb"] * 0.3) + stats["stl"] + (stats["ast"] * 0.7) + (stats["blk"] * 0.7) + (stats["pf"] *(-0.4)) - stats["turnover"]
        seasonScores.append(gmsc)
    else:
        print("ERROR")

sortedscores = sorted(seasonScores, reverse=True)

for i in range(10):
    print(str(i+1) + ". " + str(candidates[seasonScores.index(sortedscores[i])]) + " "+ str(sortedscores[i]))


