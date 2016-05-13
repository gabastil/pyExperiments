#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Name:     Document.py
# Version:  1.0.0
# Author:   Glenn Abastillas
# Date:     September 09, 2015
#
# Purpose: Allows the user to:
#           1.) Read in a document (.txt)
#           2.) Find a word in the loaded document (.txt)
#           3.) Save results of word search along with leading and trailing text whose length is controlled by the user.
#
# To see the script run, go to the bottom of this page.
#
# This class is directly inherited by the following classes:
#   - DocumentPlus.py
# 
# Updates:
# 1. [2016/02/29] - changed wording of notes in line 16 from '... class is used in the following ...' to '... class is directly inherited by the following ...'.
# 2. [2016/03/25] - removed methods: __pad(), load(), find(), saveFile()
# 3. [2016/03/25] - revised methods: save(), toString(), reset(), setSavePath()
# 4. [2016/03/25] - added methods: open(), initialize()
# - - - - - - - - - - - - -
"""	creates a manipulable document object from a text file.

The Document class is used to represent text files as objects for further
use by other classes. This is a base class and does not inherit from other
classes. Two methods exist in this class that can be used as static methods:
(1) open(doc): open a specified document and (2) save().

"""
__author__      = "Glenn Abastillas"
__copyright__   = "Copyright (c) September 9, 2015"
__credits__     = "Glenn Abastillas"

__license__     = "Free"
__version__     = "1.0.0"
__maintainer__  = "Glenn Abastillas"
__email__       = "a5rjqzz@mmm.com"
__status__      = "Deployed"

import os

class Document(object):

	def __init__(self, filePath = None, savePath = None):
		""" constructor for this class with two parameters
			@param	filePath: input file
			@param	savePath: output location
		"""
		
		self.filePath = filePath	# Store a String of the file path
		self.savePath = savePath	# Store a String of the save path
		
		self.textFile = list()		# Store a list of lines from initialized file
		self.dataList = list()		# 
		
		self.loaded   = False		# Is this object initialized

		if filePath is not None:
			self.initialize(filePath)
			
	def initialize(self, filePath = None):
		"""	opens indicated file and loads it into memory
			@param filePath: path to file to load
		"""
		self.textFile = self.open(self.filePath).split()
		self.filePath = filePath
		self.loaded   = True

	def open(self, filePath=None):
		"""	opens an indicated text file for processing
			@param	filePath: path of file to load.
			@return	String of opened text file
		"""
		fileIn1 = open(filePath, 'r')
		fileIn2 = fileIn1.read()
		fileIn1.close()

		return fileIn2

	def save(self, savePath=None, saveContent=None, saveType='w'):
		"""	write content out to a file
			@param	savePath: name of the file to be saved
			@param	saveContent: a string of the contents to be saved
			@param	saveType: indicate overwrite ('w') or append ('a')
		"""
		saveFile = open(savePath, saveType)
		saveFile.write(saveContent)
		saveFile.close()

	def getSavePath(self):
		"""	get the save path
			@return String of the save path
		"""
		return self.savePath

	def getFilePath(self):
		""" get the file path
			@return	String of the file path
		"""
		return self.filePath

	def getContents(self):
		"""	Get the file as lines in a list
			@return	List of lines from initialized file
		"""
		return self.textFile

	def setSavePath(self, savePath):
		"""	set the location for saved files
			@param	savePath: location to store saved files
		"""
		self.savePath = savePath

	def setFilePath(self, filePath):
		"""	set this object to a new file
			@param	filePath: location to new file
		"""
		self.initialize(filePath)

	def toString(self, textType = "text", returnToString = False):
		"""	prints the loaded text file or the data list onto the screen.
			@param	textType: indicate 'text' or 'data'
			@param	returnToString: return a String
			@return	String of the printed document
		"""

		if self.loaded:
			if textType == "text":
				print(self.textFile)
			elif textType == "data":
				print(str(self.dataList))
			else:
				print("Not a valid option.")
		else:
			print("No file loaded.")

		if returnToString:
			if textType == "text":
				return self.textFile
			elif textType == "data":
				return str(self.dataList)
			else:
				return None

	def reset(self):
		"""	reset all data in this class
		"""
		
		self.filePath = None	# Clear string
		self.savePath = None	# Clear string

		self.textFile = list()	# Assign to empty list
		self.dataList = list()	# Assign to empty list

		self.loaded   = False	# Reset state to False (i.e., not loaded)

if __name__ == "__main__":
	""" run as a script if this file is run as a stand-alone program
	"""
	
	d = Document("files/test.txt")

	d.find("the")
	d.save()
