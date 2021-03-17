import requests
import json

#LINK TO API DOCUMENTATION: https://www.balldontlie.io/?shell#introduction

search = input()

url = "https://www.balldontlie.io/api/v1/players?search="+str(search)
url2 = "https://www.balldontlie.io/api/v1/season_averages?"

response = requests.get(url)
sc = response.status_code

def formatjson(obj):
    text = json.dumps(obj.json(), sort_keys=True, indent=4)
    return(text)
    #create a formatted string of the Python JSON object

NBAData = formatjson(response)
# player = NBAData['data'][0]
player = NBAData
print(player)

# if sc == 200:
#   print(jsonPrint(response))