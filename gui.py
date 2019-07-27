import PySimpleGUI as sg
import GUIStack as stack
import pageLayout as pL

sg.ChangeLookAndFeel('NeutralBlue')

stack = stack.GUIStack()

homeWindow = pL.init_homepage()

stack.push(homeWindow)

while True:
	button, sport = homeWindow.Read()
	if button is None:
		break
	else:
		league = sport[0]
		if button == 'View stats':
			homeWindow.Hide()
			if league == 'NFL':
				while True:
					nflHubWindow = pL.init_nflPage()
					stack.push(nflHubWindow)
					nflHubButton, nflHubValues = nflHubWindow.Read()
					if nflHubButton is None:
						stack.pop()
						prevWindow = stack.peek()
						prevWindow.UnHide()
						break
					if nflHubButton == 'Player Stats':
						nflHubWindow.Hide()
						while True:
							nflPlayerWindow = pL.init_nflPlayerPage()
							stack.push(nflPlayerWindow)
							nflPlayerButton, nflPlayerValues = nflPlayerWindow.Read()
							if nflPlayerButton is None:
								stack.pop()
								prevWindow = stack.peek()
								prevWindow.UnHide()
								break



