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
					nflWindow = pL.init_nflPage()
					stack.push(nflWindow)
					nflButton, nflValues = nflWindow.Read()
					if nflButton is None:
						stack.pop()
						prevWindow = stack.peek()
						prevWindow.UnHide()
						break



