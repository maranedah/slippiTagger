class Character:
	def __init__(self, name, colorIndex, typeChar):
		self.name = name
		self.colorIndex = colorIndex
		self.typeChar = typeChar
		self.charColors = {  
			"Captain_falcon": ["Default", "Black", "Red", "White", "Green", "Blue"],
			"Donkey_kong": ["Default", "Black", "Red", "Blue", "Green"],
			"Fox": ["Default", "Red", "Blue", "Green"],
			"Game_and_watch": ["Default", "Red", "Blue", "Green"],
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
			"Ice_climbers": ["Default", "Green", "Orange", "Red"],
			"Jigglypuff": ["Default", "Red", "Blue", "Headband", "Crown"],
			"Samus": ["Default", "Pink", "Black", "Green", "Purple"],
			"Yoshi": ["Default", "Red", "Blue", "Yellow", "Pink", "Cyan"],
			"Zelda": ["Default", "Red", "Blue", "Green", "White"],
			"Sheik": ["Default", "Red", "Blue", "Green", "White"],
			"Falco": ["Default", "Red", "Blue", "Green"],
			"Young_link": ["Default", "Red", "Blue", "White", "Black"],
			"Dr_mario": ["Default", "Red", "Blue", "Green", "Black"],
			"Roy": ["Default", "Red", "Blue", "Green", "Yellow"],
			"Pichu": ["Default", "Red", "Blue", "Green"],
			"Ganondorf": ["Default", "Red", "Blue", "Green", "Purple"]
		}
		self.setColor()

	def isHuman(self):
		return self.typeChar.name == "HUMAN"

	def getName(self):
		return self.name

	def setColor(self):
		self.color = self.charColors[self.name][self.colorIndex]

	def getColor(self):
		return self.color