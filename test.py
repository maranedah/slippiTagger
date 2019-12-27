from slippi import Game as SlippiGame
import os
import sys
from Setup import *
from Game import *

charactersColors = {  
	"Captain Falcon": ["Default", "Black", "Red", "White", "Green", "Blue"],
	"Donkey Kong": ["Default", "Black", "Red", "Blue", "Green"],
	"Fox": ["Default", "Red", "Blue", "Green"],
	"Mr. Game & Watch": ["Default", "Red", "Blue", "Green"],
	"Kirby": ["Default", "Yellow", "Blue", "Red", "Green", "White"],
	"Bowser": ["Default", "Red", "Blue", "Black"],
	"Link": ["Default", "Red", "Blue", "Black", "White"],
	"Luigi": ["Default", "White", "Blue", "Red"],
	"Mario": ["Default", "Yellow", "Black", "Blue", "Green"],
	"Marth": ["Default", "Red", "Green", "Black", "White"],
	"Mewtwo": ["Default", "Red", "Blue", "Green"],
	"Ness": ["Default", "Yellow", "Blue", "Green"],
	"Peach": ["Default", "Daisy", "White", "Blue", "Green"],
	"Pikachu": ["Default", "Red", "Party Hat", "Cowboy Hat"],
	"Ice Climbers": ["Default", "Green", "Orange", "Red"],
	"Jigglypuff": ["Default", "Red", "Blue", "Headband", "Crown"],
	"Samus": ["Default", "Pink", "Black", "Green", "Purple"],
	"Yoshi": ["Default", "Red", "Blue", "Yellow", "Pink", "Cyan"],
	"Zelda": ["Default", "Red", "Blue", "Green", "White"],
	"Sheik": ["Default", "Red", "Blue", "Green", "White"],
	"Falco": ["Default", "Red", "Blue", "Green"],
	"Young Link": ["Default", "Red", "Blue", "White", "Black"],
	"Dr. Mario": ["Default", "Red", "Blue", "Green", "Black"],
	"Roy": ["Default", "Red", "Blue", "Green", "Yellow"],
	"Pichu": ["Default", "Red", "Blue", "Green"],
	"Ganondorf": ["Default", "Red", "Blue", "Green", "Purple"]
}

game = SlippiGame('/home/mauro/Escritorio/DPS_2/Setup_Rocket/Game_20191221T200458.slp')
print(game.start.players[1].type.name == "HUMAN")
#print(charactersColors[game.start.players[1].character.name.capitalize()][game.start.players[1].costume])