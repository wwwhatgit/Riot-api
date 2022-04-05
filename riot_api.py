

from riotwatcher import LolWatcher, ApiError
import pandas as pd
import riotwatcher
# golbal variables
api_key = 'RGAPI-531a5c5b-36dc-4deb-a7d0-07201dbab9d9'
watcher = LolWatcher(api_key)
my_region = 'na1'

me = watcher.summoner.by_name(my_region, 'UnsungSoul')
print(me)






# get random rank data by player name 
test = watcher.league.entries("na1","RANKED_SOLO_5x5","DIAMOND","II",1)


f = open("test.txt", "a",encoding='utf-8')
f.truncate(0)
for t in range(150):
    f.write(watcher.summoner.by_name(my_region,test[t]["summonerName"])["puuid"]+'\n')
f.close()

type(test)

test[0]["summonerName"]


import requests
import json
# request data from webside 
response  = requests.get('https://na.whatismymmr.com/api/v1/summoner?name='+'UnsungSoul')
print(response.json())
# get mmr data
response.json()['ranked']['avg']