
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
    f.write(watcher.summoner.by_name(
        my_region,test[t]["summonerName"])["puuid"]+
        '||'+test[t]["summonerName"]+'\n')
f.close()

# get puuid 
test_puuid = watcher.summoner.by_name(my_region,'UnsungSoul')['puuid']

# use puuid to get a list of games that player has played
watcher.match.matchlist_by_puuid('AMERICAS',
'UmFDyJV9IIWfPwI-T3jZccdgKBet0e8KsoEFSWjEEjQUznmk4pgqJI_9fNuGyLHfPFc_3nj9GU5XXQ',
count=10)

# get single game information by that player
temp = watcher.match.by_id('AMERICAS','NA1_4266324078')['info']['participants']

len(temp)

type(temp[1])
temp[1].get('assists')
# some useful data from the api will add more 
key_value = ['assists','baronKills','bountyLevel','champExperience','champLevel','championName',
'consumablesPurchased','damageDealtToBuildings','damageDealtToObjectives','damageDealtToTurrets',
'damageSelfMitigated', 'deaths', 'detectorWardsPlaced', 'goldEarned','goldSpent','kills',
'lane', 'largestCriticalStrike', 'largestKillingSpree', 'largestMultiKill', 'longestTimeSpentLiving',
'neutralMinionsKilled','role','summonerLevel','win','visionScore','visionWardsBoughtInGame','wardsKilled','wardsPlaced']

# get useful data for player
for i in range(len(temp)):
    if(temp[i]['summonerName']=='UnsungSoul'):
        [temp[i].get(k) for k in key_value]



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
