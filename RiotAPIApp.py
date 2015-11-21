# -*- coding: cp1252 -*-
#This tutorial was built by me, Farzain! You can ask me questions or troll me on Twitter (@farzatv)

#First we need to import requests. Installing this is a bit tricky. I included a step by step process on how to get requests in readme.txt which is included in the file along with this program.
import requests
import os
import requestsEngine
import spreadsheetEngine
from APIKeyFile import APIKey

def spreadsheetExistCheck():#       Para revisar si hay una Spreadsheet existente en el folder
    controlSpeadsheet = os.path.exists('RankedData.xlsx')
    return controlSpeadsheet
    
def getSummonerData():#             Para pedir la info del Summoner y su ID y guardarla global
    print "\nEnter your region to get started"
    print "Type in one of the following regions or else the program wont work correctly:\n"
    print "NA EUW EUNE LAN BR KR LAS OCE TR RU PBE\n"
    global summonerData
    region = str.lower((str)(raw_input('Type in one of the regions above: ')))
    summonerName = str.lower((str)(raw_input('Type your Summoner Name here and DO NOT INCLUDE ANY SPACES: ')))
    summonerData  = requestsEngine.requestSummonerData(region, summonerName, APIKey)
    summonerData[summonerName]['region'] = region
    summonerData['summonerName'] = summonerName
    ID = str(summonerData[summonerName]['id'])
    summonerIcon = summonerData[summonerName]['profileIconId']# Valor tipo int
    

def getRankedData(summonerData, APIKey):#               Para obtener la info de Ranked del Invocador
    global summonerRankedData
    summonerRankedData = requestsEngine.requestRankedData(summonerData, APIKey)
    
def getLastGameResult():#              Para mostrar resultado de ultima partida
    summonerRecentGames = requestsEngine.requestRecentGames(summonerData, APIKey)
    if summonerRecentGames['games'][0]['stats']['win']:
        print "\nYou Win\n"
    else:
        print "\nYou Loss\n"

def spreadsheetGraber():# Para seleccionar la spreadsheet
    global wb
    global ws
    from openpyxl import load_workbook
    wb = load_workbook('RankedData.xlsx')

def getRankedSoloMatchlist():
    global summonerRankedSoloMatchlist
    summonerRankedSoloMatchlist = requestsEngine.requestRankedSoloMatchlist(summonerData, APIKey)

def getRankedMatchIDs():
    global RankedMatchIDs
    RankedMatchIDs = []
    i = 0
    while i < summonerRankedSoloMatchlist['totalGames']:
        RankedMatchIDs.append(summonerRankedSoloMatchlist['matches'][i]['matchId'])
        i += 1
    print RankedMatchIDs

def main():#                    ---El programa---

    spreadsheetExistCheck()# Si existe spreadsheet (datos) ya no los pregunta
    if spreadsheetExistCheck():
        spreadsheetGraber()
        ws = wb["Summoner Info"]
        global summonerData
        ID = (str)(ws['B2'].value)
        summonerName = str.lower((str)(ws['B3'].value))
        summonerData = {}
        summonerData[summonerName] = {}
        summonerData[summonerName]['id'] = (str)(ws['B2'].value)
        summonerData[summonerName]['name'] = (str)(ws['B3'].value)
        summonerData[summonerName]['profileIconId'] = (str)(ws['B5'].value)
        summonerData[summonerName]['revisionDate'] = (ws['A1'].value)
        summonerData[summonerName]['summonerLevel'] = (str)(ws['B6'].value)
        summonerData[summonerName]['region'] = str.lower((str)(ws['B4'].value))
        summonerData['summonerName'] = summonerName
        
    else:#   Obtener los los datos del invocador
        getSummonerData()
            
    print "\nWelcome Summoner!!\n"  

    #   Establecido el ID. Preguntar que hacer
    control = 0
    while control != 6:
        print "\nWhat do you want to do?\n"
        print "\nPruebas escribe 0"
        print "Type 1 for Rankded Stats"
        print "Type 2 for last match result"
        print "Type 3 if you want to creat your Ranked Statistics Spreadsheet"
        print "Type 4 to update your Ranked Statistics Spreadsheet"
        print "Type 5 to get your ranked list"
        print "Type 6 for Exit\n"
        control = input()
        if control == 1:#       Para imprimir datos de Ranked          
            summonerName = summonerData['summonerName']
            getRankedData(summonerData, APIKey)
            ID = (str)(summonerData[summonerName]['id'])
            summonerLP = summonerRankedData[ID][0]['entries'][0]['leaguePoints']# Se tiene que convertir a str
            summonerLP = str(summonerLP)
            print "Your current Tier is: " + summonerRankedData[ID][0]['tier']
            print "Your current Division is: " + summonerRankedData[ID][0]['entries'][0]['division']
            print "And you currently have: " + summonerLP + " League Points"
            print "\nDone!\n"

        elif control == 2:#     Imprimir resultado del ultimo match
            getLastGameResult()

        elif control == 3:#     Crear Ranked Spreadsheet de Invocador
            if spreadsheetExistCheck():#        Revisa si exite ya un archivo primero
                print "\nThere is already a Ranked Statistics Spreadsheet\n"
            else:#                              Si no hay archivo, procede
                spreadsheetEngine.createSpreadsheet(summonerData, APIKey)
                spreadsheetEngine.spreadsheetUpdater(summonerData, APIKey)
                
        elif control == 4:#      Actualizar Ranked Spreadsheet
            if spreadsheetExistCheck():#        Revisa si existe spreadsheet que actualizar
                spreadsheetGraber()
                ws = wb["Summoner Info"]
                controlDe4 = (ws['A1'].value)#  Valor del ultimo cambio en la spreadsheet actual
                summonerName = summonerData['summonerName']
                
                if controlDe4 == summonerData[summonerName]['revisionDate']:#     Valida si el Revision Date es el mismo
                    print "\nYour Ranked Statistics Spreadsheet is up to date\n"
                else:#      Si el Revision Date no es el mismo se actulizará la spreadsheet
                    spreadsheetEngine.spreadsheetUpdater(summonerData, APIKey)
                                                            
            else:#           Si no hay spreadsheet te ofrece crear una y se actualiza
                print "\nThere is no Ranked Statistics Spreadsheet. Would you like to create one now?"
                controlDe4 = (str)(raw_input("Write y for Yes or n for No\n"))
                if controlDe4 == "y":
                    spreadsheetEngine.createSpreadsheet(summonerData, APIKey)
                    spreadsheetEngine.spreadsheetUpdater(summonerData, APIKey)    
                    
                else:#                          Si dice que no, no hace nada
                    print "Ok"
                
        elif control == 5:# Llamar rankedMatchList
            getRankedSoloMatchlist()
            getRankedMatchIDs()
            
        elif control == 6:#     Para salir
            print "Ok. See ya"
            break

        elif control == 0:# Para pruebas
            print summonerData

#This starts my program!
if __name__ == "__main__":
    main()

