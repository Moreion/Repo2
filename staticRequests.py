# Las llamadas al Static data

import requests

def requestStaticChampion(summonerData, APIKey):#Usamos True en dataById para listar por ID
    summonerName = summonerData.keys()[0]
    region = summonerData[summonerName]['region']
    URL = "https://global.api.pvp.net/api/lol/static-data/" + region + "/v1.2/champion?dataById=true&api_key=" + APIKey
    response = requests.get(URL)
    return response.json()

def requestStaticItem(summonerData, APIKey):
    summonerName = summonerData.keys()[0]
    region = summonerData[summonerName]['region']
    URL = "https://global.api.pvp.net/api/lol/static-data/" + region + "/v1.2/item?api_key=" + APIKey
    response = requests.get(URL)
    return response.json()

def requestStaticSpells(summonerData, APIKey):#Usamos True en dataById para listar por ID
    summonerName = summonerData.keys()[0]
    region = summonerData[summonerName]['region']
    URL = "https://global.api.pvp.net/api/lol/static-data/" + region + "/v1.2/summoner-spell?dataById=True&api_key=" + APIKey
    response = requests.get(URL)
    return response.json()
