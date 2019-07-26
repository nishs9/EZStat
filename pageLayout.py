import PySimpleGUI as sg
import GUIStack as stack
import apicalls as api
import csv

def init_homepage():
    homeLayout = [
    [sg.Text('Welcome to EZ-Stat!', size = (30, 1), font = ('Helvetica' , 40))],
    [sg.Text('Choose a league to view statistics:')],
    [sg.InputCombo('NFL', size = (5,1))],
    [sg.Button('View stats', bind_return_key = True)]
    ]

    homeWindow = sg.Window('EZ-Stat').Layout(homeLayout)

    return homeWindow

def init_nflPage():

    divList = ['NFC North', 'NFC South', 'NFC East', 'NFC West', 'AFC North', 'AFC South', 'AFC East', 'AFC West']

    api.getLatestStandings()

    standingsDict = {}

    for div in divList:
        data = []
        header_list = []
        with open(div + ' Standings.csv', "r") as infile:
            reader = csv.reader(infile)
            header_list = next(reader)
            try:
                data = list(reader)  # read everything else into a list of rows
            except:
                sg.PopupError('Error reading file')
                sys.exit(69)
            standingsDict[div] = data

    ##sg.SetOptions(element_padding=(0, 0))
    print(standingsDict)
    
    nfcNorth = [[sg.Text('NFC North:')], [sg.Table(values=standingsDict['NFC North'],
                            headings=header_list,
                            max_col_width=10,
                            auto_size_columns=True,
                            justification='left',
                            alternating_row_color='lightblue',
                            num_rows=min(len(data), 20))]]

    nfcSouth = [[sg.Text('NFC South:')], [sg.Table(values=standingsDict['NFC South'],
                            headings=header_list,
                            max_col_width=10,
                            auto_size_columns=True,
                            justification='left',
                            alternating_row_color='lightblue',
                            num_rows=min(len(data), 20))]]

    nfcEast = [[sg.Text('NFC East:')], [sg.Table(values=standingsDict['NFC East'],
                            headings=header_list,
                            max_col_width=10,
                            auto_size_columns=True,
                            justification='left',
                            alternating_row_color='lightblue',
                            num_rows=min(len(data), 20))]]

    nfcWest = [[sg.Text('NFC West:')], [sg.Table(values=standingsDict['NFC West'],
                            headings=header_list,
                            max_col_width=10,
                            auto_size_columns=True,
                            justification='left',
                            alternating_row_color='lightblue',
                            num_rows=min(len(data), 20))]]

    afcNorth = [[sg.Text('AFC North:')], [sg.Table(values=standingsDict['AFC North'],
                            headings=header_list,
                            max_col_width=10,
                            auto_size_columns=True,
                            justification='left',
                            alternating_row_color='lightblue',
                            num_rows=min(len(data), 20))]]

    afcSouth = [[sg.Text('AFC South:')], [sg.Table(values=standingsDict['AFC South'],
                            headings=header_list,
                            max_col_width=10,
                            auto_size_columns=True,
                            justification='left',
                            alternating_row_color='lightblue',
                            num_rows=min(len(data), 20))]]

    afcEast = [[sg.Text('AFC East:')], [sg.Table(values=standingsDict['AFC East'],
                            headings=header_list,
                            max_col_width=10,
                            auto_size_columns=True,
                            justification='left',
                            alternating_row_color='lightblue',
                            num_rows=min(len(data), 20))]]

    afcWest = [[sg.Text('AFC West:')], [sg.Table(values=standingsDict['AFC West'],
                            headings=header_list,
                            max_col_width=10,
                            auto_size_columns=True,
                            justification='left',
                            alternating_row_color='lightblue',
                            num_rows=min(len(data), 20))]]

    nflLayout = [
    [sg.Text('NFL Hub', size = (30, 1), font = ('Helvetica', 40))],
    [sg.Text('View more stats:') , sg.Button('Player Stats'), sg.Button('Team Stats'), sg.Button('League Stats')],
    [sg.Column(nfcNorth), sg.Column(nfcSouth), sg.Column(nfcEast), sg.Column(nfcWest)],
    [sg.Column(afcNorth), sg.Column(afcSouth), sg.Column(afcEast), sg.Column(afcWest)]
    ]

    nflWindow = sg.Window('NFL Hub').Layout(nflLayout)

    return nflWindow