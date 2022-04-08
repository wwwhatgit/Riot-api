
import os
os.chdir('C:\\Users\\wwwha\\OneDrive\\Desktop\\ucsb\\Pstat 131\\hw1\\Riot-api')
# import the library for riot api
from riotwatcher import LolWatcher, ApiError
import pandas as pd
import riotwatcher
# golbal variables
api_key = 'RGAPI-49fae1a1-02c9-4798-8aba-f7d8fbca6cec'
# set the api access
watcher = LolWatcher(api_key)
# set region
my_region = 'na1'

# test the api
me = watcher.summoner.by_name(my_region, 'UnsungSoul')
print(me)







# get random rank data by player name 
test = watcher.league.entries("na1","RANKED_SOLO_5x5","DIAMOND","II",1)

# open file to write player id
f = open("test2.txt", "a",encoding='utf-8')
# f.truncate(0)
for t in range(150):
    f.write(watcher.summoner.by_name(my_region,test[t]["summonerName"])["puuid"]+'||'+test[t]["summonerName"]+'\n')
f.close()

# check the type of returned frame
type(test)

# get player name
test[0]["summonerName"]

# import web api library
import requests
import json
# request data from webside 
response  = requests.get('https://na.whatismymmr.com/api/v1/summoner?name='+'UnsungSoul')
print(response.json())
# get mmr data
response.json()['ranked']['avg']
