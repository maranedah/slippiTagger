from datetime import datetime, timedelta
import re
from Character import *
import shutil 

class Game:
	def __init__(self, game, slippiPath, setup):
		self.game = game
		self.slippiPath = slippiPath
		self.setCharacters()
		self.setDuration()
		self.setDate()
		self.setup = setup

	def saveGame(self, out_path):
		pass
		#shutil.copyfile(self.slippiPath, self.out_path) 

	def setGamePlayers(self):
		pass

	def getIndexGame(self):
		return self.setup.getGames().index(self)

	def getNextGame(self):
		max_length = len(self.setup.getGames()) 
		return self.setup.getGames()[min(self.getIndexGame()+1, max_length-1) ]

	def getPrevGame(self):
		return self.setup.getGames()[max(0, self.getIndexGame()-1)]
	
	def getCharacters(self):
		return self.characters

	def setCharacters(self):
		playersNotNull = list(filter(lambda x: x!=None,self.game.start.players))
		self.characters = list(map(lambda x: Character(x.character.name.capitalize(), x.costume, x.type), playersNotNull))

	def getDuration(self):
		return self.duration

	def setDuration(self):
		self.duration = self.game.metadata.duration/3600

	def getDate(self):
		return self.date

	def setDate(self):
		date = self.game.metadata.date
		#print(s)
		#print(type(s))
		#str_date = re.search('\s(.*)\+', s).group(1)
		self.date = date + timedelta(hours=-8) #hora de chile


	def charsInTwoGames(self,mains,players):
		return self.charsInGame(mains, players) and (self.getPrevGame().charsInGame(mains,players) or self.getNextGame().charsInGame(mains,players))

	def charsInGame(self, mains, players):
		charsObject = self.getCharacters()
		chars = list(map(lambda c: c.getName(), charsObject))
		return any(main in chars[0] for main in mains[players[0]]) and any(main in chars[1] for main in mains[players[1]]) or any(main in chars[1] for main in mains[players[0]]) and any(main in chars[0] for main in mains[players[1]]) 

	def isHandWarmer(self):
		return self.getDuration()>=0.5 and self.getDuration()<2	