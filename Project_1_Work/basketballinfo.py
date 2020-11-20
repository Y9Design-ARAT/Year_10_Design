#!/usr/bin/env python3

# https://stackoverflow.com/questions/20822553/align-tabs-from-right-to-left-using-ttk-notebook-widget

import tkinter as tk
import requests
import json
import os.path
from os import path
from tkinter import ttk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText


#---------------------------------------------------
#---------------------------------------------------
# Global variables
#---------------------------------------------------
#---------------------------------------------------

player_dict = []
teams_loaded = False

#---------------------------------------------------
#---------------------------------------------------
# Import the player database
#---------------------------------------------------
#---------------------------------------------------

def getplayers():
	global player_dict

	if path.exists("player_data.txt"):
		result = messagebox.askyesno("Load Existing Data", "Previously loaded player data found. Open local file?")
		if result == True:
			with open("player_data.txt", "r") as load_data:
				player_dict = json.load(load_data)
		else:
			loadAPIplayers()
	else:
		loadAPIplayers()

def loadAPIplayers():
	messagebox.showinfo("Alert", "Application will fetch player data from an online data base")
	global player_dict
	player_API_page = 1

	while(True):
		url = "https://www.balldontlie.io/api/v1/players?page="+str(player_API_page)+"&per_page=100"
		response = requests.get(url)
		print(player_API_page, response)
		json_response = json.loads(response.text)
		player_dict += json_response["data"]
		if json_response["meta"]["next_page"] != None:
			 player_API_page += 1
		else:
			break

	#deletes saved file if already exists before writting new data.
	# if path.exists("player_data.txt"):
	# 	save_file = open("player_data.txt", "r+")
	# 	save_file.truncate(0)
	# 	save_file.close()

	with open("player_data.txt", "w") as save_file:
		save_file.truncate(0)
		json.dump(player_dict, save_file)
	messagebox.showinfo("Alert", "Application has finished loading data")

#---------------------------------------------------
#---------------------------------------------------
# App functions
#---------------------------------------------------
#---------------------------------------------------

def tab_changed(event_data):
	global teams_loaded
	tab_name = event_data.widget.tab("current")["text"]
	if tab_name == "Teams" and teams_loaded == False:
		teams_loaded = True
		print("Teams Tab Opened")
		url = "https://www.balldontlie.io/api/v1/teams"
		reponse = requests.get(url)
		teams_json = json.loads(reponse.text)
		for team in teams_json["data"]:
			print(team["full_name"], team["id"])
			button = tk.Button(tab2_scrolled_text, bg='red', fg='blue', width=47, height=4, text=team["full_name"], command=lambda arg0=team["id"]: showteamplayers(arg0))
			tab2_scrolled_text.window_create(tk.END, stretch = True, window = button)

			#stuff = tk.Label(tab2_scrolled_text, text=":):):):):)")
			#img = tk.PhotoImage(file="bob.png")
			#tab2_scrolled_text.window_create(tk.END, window = stuff)

def showteamplayers(team_id):
	planner.select(tab3)
	# Get all the players from the player_dict and put them into a sortable players list
	# Note:  It's tough to sort a dictionary, but easy to sort a list
	playerList = []
	for player in player_dict:
		if player["team"]["id"] == team_id:
			# Get the next player
			# Adding the name to the list
			playerList.append(player)

			# Getting the player's information.  This should be elsewhere in the code
			# once all the players are converted into buttons.  You click on the player button and the
			# text field for STATS would be filled with that player's statistics.
			#print(playerId)
			#playerId=664
			#url = "https://www.balldontlie.io/api/v1/season_averages?player_ids[]="+str(playerId)
			#reponse = requests.get(url)
			#single_player_json = json.loads(reponse.text)
			#print(single_player_json)
			
	
	# Clear all existing widgets form the scorllbar
	child_widgets = tab3_scrolled_text.winfo_children()
	for each_widget in child_widgets:
		each_widget.destroy()

	# Show the SORTED player list
	for player in playerList:
		#player_text = tk.Label(tab3_scrolled_text, text = player, width = 50)
		player_name = player["last_name"] + ", " + player["first_name"]
		player_text = tk.Button(tab3_scrolled_text, text = player_name, width = 50, command = lambda arg0=player["id"]: get_stats(arg0))

		player_text.pack(fill = "x")
		#player_text.set(tk.END, player)
		tab3_scrolled_text.window_create(tk.END, window = player_text)


def get_teams(event):
	print("getting team data")

def get_stats(player_id):
	print("fetching player stats", player_id)
	url = "https://www.balldontlie.io/api/v1/season_averages?player_ids[]="+str(player_id)
	reponse = requests.get(url)
	player_stats = json.loads(reponse.text)
	
	child_widgets2 = tab4_scrolled_text.winfo_children()
	for each_widget2 in child_widgets2:
		each_widget2.destroy()


	planner.select(tab4)
	if len(player_stats["data"]) > 0:
		for stat_item in player_stats["data"][0]:
			#print(stat_item, ": ", player_stats["data"][0][stat_item])
			player_info = tk.Label(tab4_scrolled_text, text = stat_item + ": " + str(player_stats["data"][0][stat_item]), width = 50, height = 1)
			player_info.pack(fill ="x")
	else:
		no_data = tk.Label(tab4_scrolled_text, text = "No Available Data for this Player", width = 50, height = 5)
		no_data.pack(fill = "x")






#---------------------------------------------------
#---------------------------------------------------
# App
#---------------------------------------------------
#---------------------------------------------------

# App Root
root = tk.Tk()
root.minsize(400, 400)
root.geometry("500x1000")

# Notebook Style App
style = ttk.Style()
style.configure('TNotebook', tabposition='nw') #'nw' as in compass direction
# style.configure('lefttab.TNotebook', tabposition='ws')
planner = ttk.Notebook(root, width=500, height=800)

#----------------------------------------------------------------------------
# TAB 1 - Homepage
#----------------------------------------------------------------------------
# Create the frames of different colours that are 200*200 pixels in dimensions
tab1 = tk.Frame(planner, width=500, height=800)

w11=446
h11=238
welcome11 = tk.Label(tab1, text="Aaron's", width=w11, height=h11, bg='#00E8FF', fg='white', font=("Helvetica", 50))
welcome11.place(x=0,y=0,width=w11,height=h11)
w22=w11
h22=h11
welcome22 = tk.Label(tab1, text="Basketball", width=w22, height=h22, bg='blue', fg='white', font=("Helvetica", 40))
welcome22.place(x=0,y=h11,width=w22,height=h22)
w33=w11
h33=h11
welcome33 = tk.Label(tab1, text="Informatic", width=w33, height=h33, bg='#00E8FF', fg='white', font=("Helvetica", 40))
welcome33.place(x=0,y=h11+h22,width=w33,height=h33)

#----------------------------------------------------------------------------
# TAB 2 - Team list tab
#----------------------------------------------------------------------------
tab2 = tk.Frame(planner, bg='#00E8FF', width=500, height=800)
tab2.bind("<Button-1>",get_teams)
tab2.pack()
tab2_scrolled_text = ScrolledText(tab2, state = tk.DISABLED, width=500, height=800)
tab2_scrolled_text.pack()



#scroll bar for team list
#scrollbar = ttk.Scrollbar(tab2, orient=tk.VERTICAL)
#scrollbar.pack(fill=tk.Y, side=tk.RIGHT)
#scrollbar.config(command=canvas_tab2.yview)

#scrollable_frame = ttk.Frame(canvas_tab2, height=300, width=300)

#canvas_tab2.config(yscrollcommand=scrollbar.set)
#canvas_tab2.pack()

#----------------------------------------------------------------------------
# TAB 3 - Players Tab
#----------------------------------------------------------------------------
tab3 = tk.Frame(planner, bg='#00E8FF', width=500, height=800)
tab3_scrolled_text = ScrolledText(tab3, state = tk.DISABLED, width=500, height=800)
tab3_scrolled_text.pack(expand = True, fill = "y")


#----------------------------------------------------------------------------
# TAB 4 - Season Averages
#----------------------------------------------------------------------------
tab4 = tk.Frame(planner, bg='#00E8FF', width=500, height=800)
tab4_scrolled_text = ScrolledText(tab4, state = tk.DISABLED, width=500, height=800)
tab4_scrolled_text.pack(expand = True, fill = "y")
#----------------------------------------------------------------------------
# Consolidate all the widgets into the App (planner notebook canvas)
#----------------------------------------------------------------------------

planner.bind("<<NotebookTabChanged>>", tab_changed)

# Add the tabs/frames to the notebook object called "planner" 
planner.add(tab1, text='Home')
planner.add(tab2, text='Teams')
planner.add(tab3, text='Players')
planner.add(tab4, text="Season Averages")

# Tabs will be added to the "top" of the "frame"
planner.pack(side=tk.LEFT )

#----------------------------------------------------------------------------
# Run the App
#----------------------------------------------------------------------------

def appclosed():
	root.destroy()

root.protocol("WM_DELETE_WINDOW", appclosed)
root.after(2000, getplayers)
root.mainloop()





