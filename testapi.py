import base64
import requests
import json
import csv

try:
    response = requests.get(
        url='https://api.mysportsfeeds.com/v2.1/pull/nfl/latest/standings.json',
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
print(jsonResp)
teamList = jsonResp['teams']

with open('standings.csv', mode = 'w', newline = '') as file:
	csvFile = csv.writer(file, delimiter = ',')
	csvFile.writerow(['Team','W','L','T','Win %', 'GB'])
	nfcWestDict = {}
	for i in range(32):
		newTeam = []
		if teamList[i]['divisionRank']['divisionName'] == 'NFC West':
			newTeam.append(teamList[i]['team']['city'] + " " + teamList[i]['team']['name'])
			newTeam.append(teamList[i]['stats']['standings']['wins'])
			newTeam.append(teamList[i]['stats']['standings']['losses'])
			newTeam.append(teamList[i]['stats']['standings']['ties'])
			newTeam.append(teamList[i]['stats']['standings']['winPct'])
			newTeam.append(teamList[i]['divisionRank']['gamesBack'])
			nfcWestDict[teamList[i]['divisionRank']['rank']] = newTeam
	for j in range(1,5):
		csvFile.writerow(nfcWestDict[j])