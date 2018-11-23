#! /usr/bin/env python3

class Game:
	def __init__ (self, cols = 7, rows = 6, requiredToWin = 4):   
		"""COMMENT"""
		self.cols = cols
		self.rows = rows
		self.win = requiredToWin
		self.board = self.printBoard(cols, rows)

	def insert (self, column, color):
		"""COMMENT"""
		self.color = color
		
	def checkForWin (self):
		w = self.getWinner()
		if w:
			self.printBoard()
			raise Exception(w+' won.')
			
	def getWinner (self):
		
		
	def printBoard (columns, rows):
		""" """
		for y in range(columns):
			for x in range (rows):
				print('---')

printBoard(7,6)
