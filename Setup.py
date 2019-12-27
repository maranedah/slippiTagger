import os
from slippi import Game as SlippiGame
from Game import *

class Setup:
	def __init__(self, slippiPath, matchPath, setupName):
		self.slippiPath = slippiPath
		self.initGames(slippiPath)

		self.matchPath = matchPath
		self.setupName = setupName
		self.setPlayers(self.matchPath, self.setupName)
		self.currentGame = 0
		

	def initGames(self, slippiPath):
		files = os.listdir(slippiPath)
		files.sort()
		slippi_games = list(map(lambda file: SlippiGame(slippiPath + file), files))
		games = list(map(lambda slippi_game: Game(slippi_game, slippiPath+file, self), slippi_games))
		self.games = games

	def getGames(self):
		return self.games

	def filterGames(self, startDateTime, minLength):
		self.games = list(filter(lambda x: x.getDate().replace(tzinfo=None)>datetime.strptime(startDateTime, '%d-%m-%Y %H:%M:%S'), self.games))
		self.games = list(filter(lambda x: x.duration>minLength, self.games))
		self.games = list(filter(lambda g: g.getCharacters()[0].isHuman() and g.getCharacters()[1].isHuman(), self.games))
		

	def getCharactersList(self):
		return list(map(lambda x: x.getCharacters(), self.games))

	def setPlayers(self, matchPath, setupName):
		self.players = list(map(lambda x: x.replace("\n","").replace(" ", "").split("-"),open(matchPath + setupName,'r').readlines()))

	def getPlayers(self):
		return self.players

	def getGamesPlayedByMatch(self, mains, players):
		return list(filter(lambda x: x.charsInTwoGames(mains,players), self.games))

	def getGamesPlayedAllPlayers(self, mains):
		return list(map(lambda x: self.getGamesPlayedByMatch(mains,x), self.players))
