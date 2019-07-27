import base64
import requests
import json
import csv

def getLatestStandings():
    try:
        response = requests.get(
            url='https://api.mysportsfeeds.com/v2.1/pull/nfl/2018-2019-regular/standings.json',
            params={
                "fordate": "20190723"
            },
            headers={
                "Authorization": "Basic " + base64.b64encode('{}:{}'.format('83298d15-107d-4444-a888-3523ba','MYSPORTSFEEDS').encode('utf-8')).decode('ascii')
            }
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        # print('Response HTTP Response Body: {content}'.format(
        #     content=response.content))
        # jsonResp = response.json()
        # print(jsonResp['teams'])
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

    jsonResp = response.json()
    teamList = jsonResp['teams']
    divList = ['NFC North', 'NFC South', 'NFC East', 'NFC West', 'AFC North', 'AFC South', 'AFC East', 'AFC West']

    for div in divList:
        filename = div + ' Standings.csv'
        with open(filename, mode = 'w', newline = '') as file:
            csvFile = csv.writer(file, delimiter = ',')
            csvFile.writerow(['Team','W','L','T','Win %', 'GB'])
            divDict = {}
            for i in range(32):
                newTeam = []
                if teamList[i]['divisionRank']['divisionName'] == div:
                    newTeam.append(teamList[i]['team']['city'] + " " + teamList[i]['team']['name'])
                    newTeam.append(teamList[i]['stats']['standings']['wins'])
                    newTeam.append(teamList[i]['stats']['standings']['losses'])
                    newTeam.append(teamList[i]['stats']['standings']['ties'])
                    newTeam.append(teamList[i]['stats']['standings']['winPct'])
                    newTeam.append(teamList[i]['divisionRank']['gamesBack'])
                    divDict[teamList[i]['divisionRank']['rank']] = newTeam
            for j in range(1,5):
                csvFile.writerow(divDict[j])

getLatestStandings()

