
import os
from pickle import TRUE
# import the library for riot api
from riotwatcher import LolWatcher, ApiError
import pandas as pd
import riotwatcher
import time
import json
# set wd 
os.chdir('C:\\Users\\wwwha\\OneDrive\\Desktop\\ucsb\\Pstat 131\\hw1\\Riot-api')
# the dataset 
new_df=pd.read_csv('gameInfo.csv')
puuid_df = pd.read_csv('puuid_df.csv')
# golbal variables
api_key = 'RGAPI-c7555bcb-3a3c-4451-b4a6-f6e63468dce0'
# set the api access
watcher = LolWatcher(api_key)
# set region
my_region = 'na1'

# test the api
me = watcher.summoner.by_name(my_region, 'UnsungSoul')
print(me)



Tier = ['GOLD','PLATINUM','DIAMOND']
Div = ['I','II','III','IV']





# get random rank data by player name 
DiamondList = watcher.league.entries("na1","RANKED_SOLO_5x5","DIAMOND","II",1)

for i in DiamondList:
  print(i['summonerName'])




# open file to write player id
f = open("test2.txt", "a",encoding='utf-8')
f.truncate(0)
for t in range(150):
    f.write(watcher.summoner.by_name(
        my_region,DiamondList[t]["summonerName"])["puuid"]+
        '||'+DiamondList[t]["summonerName"]+'\n')
f.close()

# get puuid 
test_puuid = watcher.summoner.by_name(my_region,'UnsungSoul')['puuid']

# use puuid to get a list of games that player has played using puuid
watcher.match.matchlist_by_puuid('AMERICAS',
'UmFDyJV9IIWfPwI-T3jZccdgKBet0e8KsoEFSWjEEjQUznmk4pgqJI_9fNuGyLHfPFc_3nj9GU5XXQ',
count=10)

# get single game information by that player
temp = watcher.match.by_id('AMERICAS','NA1_4266324078')['info']['participants']

len(temp)

type(temp[1])
temp[1].get('assists')






a =watcher.match.by_id('AMERICAS','NA1_4266324078')

# use dataframe from pandas  updated
mydf = pd.DataFrame(a)

# get game info 
mydf['info']['participants']

# set game info into variable 
game_info = pd.DataFrame(mydf['info']['participants'])
test_gameinfo = game_info[game_info.summonerName =='UnsungSoul']
test_gameinfo.append(game_info[game_info.summonerName =='VoidBBlade'],ignore_index=True)


test_gameinfo.head()

Diamond_puuid_list=[]

def get_puuid(list_of_summonerName):
  list_to_return=[]
  for t in range(len(list_of_summonerName)):
    time.sleep(1.3)
    list_to_return.append(watcher.summoner.by_id(my_region, list_of_summonerName[t]["summonerId"])["puuid"])
    
  return list_to_return

def get_puuid_single(summonerId):
  time.sleep(1.25)
  return watcher.summoner.by_id(my_region, summonerId)["puuid"]


def get_game_list(puuid):
  return watcher.match.matchlist_by_puuid('AMERICAS',puuid,count=10,type='ranked')

def get_game_info(gameid):
  time.sleep(1.25)
  return pd.DataFrame(watcher.match.by_id('AMERICAS',gameid))['info']


puuid_df = pd.DataFrame(columns = ['Tier', 'Div', 'puuid'])
puuid_df
dic = {}
for i in Tier:
  for j in Div:
    dic[i+' '+j]=watcher.league.entries("na1","RANKED_SOLO_5x5",i,j,1)[0:100]
count = 0

for i in Tier:
  for j in Div:
    for k in dic[i+' '+j]:
      puuid_df = puuid_df.append({'Tier':i,'Div':j,'puuid': get_puuid_single(k['summonerId'])},ignore_index = True)

puuid_summonerId_df = puuid_df.copy()

puuid_summonerId_df['summonerId'] = ''

count=0
for i in Tier:
  for j in Div:
    for k in dic[i+' '+j]:
      puuid_summonerId_df['summonerId'][count]=k['summonerId']
      count+=1





game_list_df = pd.DataFrame(columns = ['puuid', 'gameList'])
game_list_df

for i in range(len(puuid_df)):
  game_list_df = game_list_df.append({'puuid':puuid_df['puuid'][i],'gameList':get_game_list(puuid_df['puuid'][i])}, ignore_index = True)



df_to_stack = game_list_df.copy()

df_stack = pd.DataFrame(df_to_stack.gameList.to_list(), index=df_to_stack.puuid).stack()
df_stack = df_stack.reset_index(["puuid"])
df_stack.columns = ["puuid", "gameList"]


merge_df = puuid_summonerId_df.copy()
merge_df = merge_df.merge(df_stack, how='left', on='puuid')



game_info_df = merge_df.copy()
game_info_df['gameInfo'] = ''

game_info_df=game_info_df.drop(game_info_df[game_info_df['Tier']=='BRONZE'].index)
game_info_df=game_info_df.drop(game_info_df[game_info_df['Tier']=='SILVER'].index)


game_info_df = merge_df.head()

game_info_df.dropna(subset = ["gameList"], inplace=True)
game_info_df.dropna(subset = ["puuid"], inplace=True)
game_info_df.dropna(subset = ["summonerId"], inplace=True)
game_info_df.dropna(subset = ["gameInfo"], inplace=True)
game_info_df = game_info_df.reset_index()

11936
dtf = pd.read_csv('gameInfo6.csv')

new_df = dtf.dropna()
new_df = new_df.drop(columns=['Unnamed: 0','index'])
new_df = new_df.reset_index()
new_df = new_df.drop(columns='index')




for i in range(len(new_df['gameInfo'])):
  print(new_df['gameInfo'][i][1])




temp_list = (new_df['gameInfo'][9999].replace(' ','').replace('\'',
'').replace('[','').replace(']','').replace('}',
'').replace('{','').split(','))
l1=[]
l2=[]
for i in range(len(temp_list)):
  l1.append(temp_list[i].partition(':')[0])
  l2.append(temp_list[i].partition(':')[2])
  print(l1[i],'  ',l2[i])

print(i,' : '+temp_list[i])
d1=dict(zip(l1,l2))
print(d1)

list_of_dict = []
for i in range(len(new_df['gameInfo'])):
  temp_list = (new_df['gameInfo'][i].replace(' ','').replace('\'',
  '').replace('[','').replace(']','').replace('}',
  '').replace('{','').split(','))
  for j in range(len(temp_list)):
    l1.append(temp_list[j].partition(':')[0])
    l2.append(temp_list[j].partition(':')[2])
  temp_dict = dict(zip(l1,l2))
  list_of_dict.append(temp_dict)
  l1=[]
  l2=[]

list_of_dict[10000]

final_dataframe = pd.DataFrame(list_of_dict)

final_dataframe.to_csv('full_dataset.csv')

list_of_columns = final_dataframe.columns


my_file = open("list_of_variable.txt", "r")

cols = my_file.read()
list_of_columns = cols.split("\n")

for i in list_of_columns:
  print(i)


len(list_of_columns)


fd = final_dataframe[list_of_columns].fillna(0)
fd.to_csv('final_dataset.csv')


fd.merge(puuid_df, how='left', on='puuid').to_csv('datasetForR.csv')
fd = pd.read_csv('datasetForR.csv')
fd = fd.drop(columns=['summonerName','puuid'])
fd = fd.drop(columns=['Unnamed: 0','summonerId_y','Unnamed: 0.1'])
fd = fd.drop(columns='summonerId_x')
fd = fd.reset_index()
fd.to_csv('Rdataset.csv')

for i in range(10955,len(game_info_df)):
  temp_game_info = get_game_info(game_info_df.gameList[i])
  temp_id = game_info_df.summonerId[i]
  for j in range(len(temp_game_info['participants'])):
    if temp_id == temp_game_info['participants'][j]['summonerId']:
      game_info_df['gameInfo'][i] = temp_game_info['participants'][j]

temp_id = game_info_df.summonerId    
temp_game_info = get_game_info('NA1_4220534744')  
get_game_info('NA1_4220534744')
for i in range(len(temp_game_info['participants'])):
  if temp_id ==temp_game_info['participants'][i]['summonerId']:
    game_info_df['gameInfo'][852] = temp_game_info['participants'][i]


game_info_df.to_csv('gameInfo.csv')

game_info_df['puuid'][852]





print(game_info_df.columns)
test_game_info = get_game_info(merge_df.gameList[0])
test_sum_id = merge_df.summonerId[0]
test_game_info['participants'][0].pop('challenges', None)
test_game_info['participants'][0].pop('styles', None)
test_game_info['participants'][0].pop('statPerks', None)

game_info_df.gameInfo[0] = pd.DataFrame(test_game_info['participants'])['summonerId']

tdf = pd.DataFrame(test_game_info['participants'])

tdf.loc[tdf['summonerId']==test_sum_id]

for i in range(10):
  if test_sum_id == test_game_info['participants'][i]['summonerId']:
    print(i)

len(test_game_info['participants'])








game_list_df.to_csv('game_list_df.csv')
puuid_summonerId_df.to_csv('puuid_df.csv')



game_list = []

game_info = []

participants_list = []

dataset = pd.DataFrame()

for i in Diamond_puuid_list:
  for j in get_game_list(i):
    game_list.append(j)


for i in range(len(game_list)):
  game_info.append(get_game_info(game_list[i]))
  
len(game_info)


for i in game_info:
  participants_list.append(pd.DataFrame(i['participants']))
  

  
dataset = pd.concat(participants_list)


oo =pd.DataFrame(dataset)

filepath = Path('C:/Users/wwwha/OneDrive/Desktop/ucsb/Pstat 131/hw1/Riot-api/test.csv')  
filepath.parent.mkdir(parents=True, exist_ok=True) 
oo.to_csv(filepath)
pd.DataFrame(mydf['info']['participants']).to_csv(filepath)











game_info = get_game_info('NA1_4270151175')



test_list = get_game_list(Diamond_puuid_list[0])

test_gameinfo = get_game_info(test_list[0])

test_participants = pd.DataFrame(test_gameinfo['participants'])
test_gameinfo['participants'][1]
type(test_participants)
test_df=pd.DataFrame()

test_df.append(test_participants)



























from pathlib import Path  
filepath = Path('C:/Users/wwwha/OneDrive/Desktop/ucsb/Pstat 131/hw1/Riot-api/out1.csv')  
filepath.parent.mkdir(parents=True, exist_ok=True) 
pd.DataFrame(mydf['info']['participants']).to_csv(filepath)

# check the type of returned frame
type(test)

# get player name
test[0]["summonerName"]

# import web api library
import requests
import json


def get_mmr(playername):
  response  = requests.get('https://na.whatismymmr.com/api/v1/summoner?name='+playername)
  return response.json()['ranked']['avg']



# request data from webside 
response  = requests.get('https://na.whatismymmr.com/api/v1/summoner?name='+'UnsungSoul')
print(response.json())
# get mmr data
response.json()['ranked']['avg']





















