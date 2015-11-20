# -- Aqui se euncuentan las Requests de la APP --

import requests

def requestSummonerData(region, summonerName, APIKey):#     Here is how I make my URL.  There are many ways to create these. summoner-v1.4
    URL = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v1.4/summoner/by-name/" + summonerName + "?api_key=" + APIKey
    response = requests.get(URL)
    # Obtenemos codigo de Respuesta;  200 es bueno
    if response.status_code == 200:# Si es bueno se regresa el JSON
        return response.json()
    else:#  Llama a funcion para imprimir razon de error
        errorReason(response.status_code)

def requestRankedData(region, ID, APIKey):#     Llamado de la info de Ranked
    URL = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v2.5/league/by-summoner/" + ID + "/entry?api_key=" + APIKey
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()
    else:
        errorReason(response.status_code)

def requestRecentGames(region, ID, APIKey):#    Llamado para obtener info de los ultimos matches NO DETALLADA
    URL = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v1.3/game/by-summoner/" + ID + "/recent?api_key=" + APIKey
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()
    else:
        errorReason(response.status_code)

def requestRankedSoloMatchlist(region, ID, APIKey):# Para obtener los matches Ranked del invocador
    URL = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v2.2/matchlist/by-summoner/" + ID + "?rankedQueues=RANKED_SOLO_5x5&seasons=SEASON2015&api_key=" + APIKey
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()
    else:
        errorReason(response.status_code)

def errorReason(code):# Para imprimir razon de los errores
    if code == 400:
        print '\nBad Request\n'
    elif code == 401:
        print '\nUnauthorized (Possible APIKey Change)\n'
    elif code == 404:
        print '\nNo Data found for any specified inputs\n'
    elif code == 422:
        print '\nSummoner has an entry, but hasn\'t played since the start of 2013\n'
    elif code == 429:
        print '\nRate limit exceeded\n'
    elif code == 500:
        print '\nInternal server error\n'
    elif code == 503:
        print '\nService unavailable\n'
