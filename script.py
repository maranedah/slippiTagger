from slippi import Game as SlippiGame
import os
import sys
from Setup import *
from Game import *


mains = {
	"Zera": {"Marth", "Falco"},
	"LarryCatula": {"Falco"},
	"Nyx": {"Game_and_watch","Falco","Fox"},
	"Clavit4": {"Marth"},
	"Darkside": {"Falco","Fox"},
	"Benyay": {"Marth"},
	"Jochava": {"Fox","Sheik"},
	"Deimos": {"Peach","Falco"},
	"DAC": {"Peach"},
	"AnonimoN": {"Fox"},
	"Cremaster": {"Fox","Sheik"},
	"Skykek": {"Captain_falcon"},
	"NDJ": {"Pikachu", "Ganondorf"},
	"CronoNes": {"Fox"},
	"Dom": {"Jigglypuff"},
	"Bou": {"Marth","Fox"},
	"Guasauski": {"Mewtwo"},
	"Rocket": {"Young_link"}
}





slippiPath = "/home/mauro/Escritorio/DPS_2/Setup_Rocket/"

matchPath = '/home/mauro/Documentos/U-Smash/Analisis Slippi/Setups/'
setupName = 'Setup_Rocket'

setup = Setup(slippiPath, matchPath, setupName)
charactersList = setup.getCharactersList()
players = setup.getPlayers()


gamesPlayed = setup.getGamesPlayedAllPlayers(mains)

matchs = len(gamesPlayed)
for i in range(matchs):
	posibleGames = len(gamesPlayed[i])
	print(players[i])
	for j in range(posibleGames):
		game = gamesPlayed[i][j]
		char1 = game.getCharacters()[0].getName() + "(" + game.getCharacters()[0].getColor() +  ")"
		char2 = game.getCharacters()[1].getName() + "(" + game.getCharacters()[1].getColor() +  ")"
		print(char1 +"-"+ char2, game.getIndexGame(), game.getDuration(), game.isHandWarmer(), game.getDate())


startTime = '21-12-2019 13:30:00'
minLength = 0.5
setup.filterGames(startTime, minLength)
gamesPlayed = setup.getGamesPlayedAllPlayers(mains)

matchs = len(gamesPlayed)
for i in range(matchs):
	posibleGames = len(gamesPlayed[i])
	print(players[i])
	for j in range(posibleGames):
		game = gamesPlayed[i][j]
		char1 = game.getCharacters()[0].getName() + "(" + game.getCharacters()[0].getColor() +  ")"
		char2 = game.getCharacters()[1].getName() + "(" + game.getCharacters()[1].getColor() +  ")"
		print(char1 +"-"+ char2, game.getIndexGame(), game.getDuration(), game.isHandWarmer(), game.getDate())




import pprint
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(players)

#getCharlist(directoryPath)

#setup_games = open('/home/mauro/Documentos/U-Smash/Analisis Slippi/Setups/'+ setup,'r').readlines()

#charList = getCharlist(directoryPath)
#print(charList)
#current_game = 0
"""for game in setup_games:
	game = game.split("\n")[0]
	players = game.split("-")
	player1 = players[0].strip()
	player2 = players[1].strip()
	
	print(player1 + " v/s " + player2)

	for i in range(1,len(charList)-1)	:
		chars = charList[i][0]
		duration = charList[i][1]
		nextGame = charList[i+1]
		prevGame = charList[i-1]

		if charsInGame(chars,mains, player1,player2) and (charsInGame(nextGame[0],mains, player1,player2) or charsInGame(prevGame[0],mains, player1,player2)):
			print(charList[i], i)
			#if i>current_game and isHandWarmer(duration):
				#print("calentamiento")
				#print(charList[i+1], i+1)
				#print(charList[i+2], i+2)
				
				#current_game = i+2

				#if charsInGame(charList[i+3][0],mains, player1,player2):
				#	print(charList[i+3], i+3)
					
				#	current_game += 1

				#break
	#print(current_game)	
"""