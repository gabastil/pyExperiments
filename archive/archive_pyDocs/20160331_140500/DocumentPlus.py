#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Name:     DocumentPlus.py
# Version:  1.0.1
# Author:   Glenn Abastillas
# Date:     September 14, 2015
#
# Purpose: Allows the user to:
#           1.) Read in a document (.txt)
#           2.) Find a word in the loaded document (.txt)
#           3.) Save results of word search along with leading and trailing text whose length is controlled by the user.
#           4.) Count descriptive features of the word find (i.e., count, BOS, EOS, etc.).
#
# To see the script run, go to the bottom of this page.
#
# This class is directly inherited by the following classes:
#   - SpreadsheetSearch.py
#	- FindDebrid.py
#
# Updates:
# 1. [2016/02/29] - changed wording of notes in line 17 from '... class is used in the following ...' to '... class is directly inherited by the following ...'.
# 2. [2016/02/29] - changed variable name 'text' to 'searchTerm' to match related variable name in parent class.
# 3. [2016/02/29] - changed import statement from 'import Document' to 'from Document import Document' to allow for this class to inherit 'Document' instead of 'Document.Document'. Version changed from 1.0.0 to 1.0.1.
# 
# - - - - - - - - - - - - -
""" builds on Document class to provide text manipulation and text search capabilities

DocumentPlus extends the Document class providing new functionality such as
searching documents for particular key words or tokens allowing for control
on how much leading and trailing context to include. In addition to this, the
DocumentPlus class contains methods for removing stop words and punctuation. 
The corpus of stop words and punctuation is flexible, which means that the 
words or punctuation may be added upon or deleted.

"""

__author__      = "Glenn Abastillas"
__copyright__   = "Copyright (c) September 14, 2015"
__credits__     = "Glenn Abastillas"

__license__     = "Free"
__version__     = "1.0.1"
__maintainer__  = "Glenn Abastillas"
__email__       = "a5rjqzz@mmm.com"
__status__      = "Deployed"

from Document import Document

class DocumentPlus(Document):

	def __init__(self, filePath = None, savePath = None):
		""" constructor for this class with two parameters
			@param	filePath: input file
			@param	savePath: output location
		"""

		self.super = super(DocumentPlus, self)	# Assign self.super the parent class Document
		self.super.__init__(filePath, savePath)	# Initialize the parent class Document
		
		self.stop_puncs   = ['\'', '\"', '`', '[', ']', '{', '}', '(', ')', '!', '.', ',', '?', ';', ':', '<', '>', '|', '\\', '/', '-', '_', '=', '+', '&', '^', '$', '%', '@', '~', '--', '#']
		self.stop_words   = ["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also", "although", "always", \
							 "am", "among", "amongst", "amoungst", "amount", "an", "and", "another", "any", "anyhow", "anyone", "anything", "anyway", "anywhere", "are", "around", "as", "at",\
							 "back", "be", "became", "because", "become", "becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between",  \
							 "beyond", "bill", "both", "bottom", "but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", 	  \
							 "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven", "else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone",  \
							 "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four",  \
							 "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", 		  \
							 "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its",   \
							 "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover",   \
							 "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", \
							 "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", 	  \
							 "ourselves", "out", "over", "own", "part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", 	  \
							 "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", 		  \
							 "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", 	  \
							 "thereby", "therefore", "therein", "thereupon", "these", "they", "thick", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru",  \
							 "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we",  \
							 "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", 	  \
							 "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours",     \
							 "yourself", "yourselves"]

	def find(self, text, term):
		"""	find the specified term in the text and return a list of indices
			@param	text: text String to search term in
			@param	term: String term to search for
			@return	List of tuples with start and end indices for search term
		"""
		listOfResults = list()

		currentIndex  = 0
		termLength	  = len(term)
		append		  = listOfResults.append

		while currentIndex >= 0:
			currentIndex = text.find(term, currentIndex+1)
			append((currentIndex, currentIndex+termLength))

		# Return listOfResults[:-1] because the last tuple contains -1 (negative one)
		return listOfResults[:-1]

	def findLines(self, text, term, scope = 75):
		"""	find the specified term in the text and return its surrounding context
			@param	text: text String to search term in
			@param	term: String term to search for
			@param	scope:	number of leading and trailing characters to include
			@return	List of tuples with start and end indices for search term
		"""
		listOfResults = list()

		currentIndex  = 0
		termLength	  = len(term)
		append		  = listOfResults.append
		text = text.lower()
		term = term.lower()

		while currentIndex >= 0:
			currentIndex = text.find(term, currentIndex+1)

			indexA = currentIndex - scope
			indexB = currentIndex + termLength + scope

			append(text[indexA:indexB].replace('\n', '_'))

		return listOfResults[:-1]

	def findTokens(self, text, term, scope = 7, sort = False):
		"""	find the specified term in the text and return its surrounding token context
			@param	text: text String to search term in
			@param	term: String term to search for
			@param	scope: number of leading and trailing tokens to include
			@return	List of tuples with start and end indices for search term
		"""
		listOfResults = list()

		append	= listOfResults.append
		tokens	= self.removeStopWords(self.removePunctuation(text.lower()), False)
		term	= term.lower()

		# Loop through all the tokens
		for token in tokens:

			# If this token matches the search term, add to list
			if term in token:
				indexOfToken = tokens.index(token)

				indexA = indexOfToken - scope
				indexB = indexOfToken + scope

				if sort:
					append(' '.join([token, tokens[indexOfToken+1], tokens[indexOfToken-1], \
											tokens[indexOfToken+2], tokens[indexOfToken-2], \
											tokens[indexOfToken+3], tokens[indexOfToken-3], \
											tokens[indexOfToken+4], tokens[indexOfToken-4]]))
				else:
					append(' '.join(tokens[indexA:indexB]))

		return listOfResults

	def addStopWord(self, newStopWord):
		""" Add a new stop word to this class's list
			@param	newStopWord: new stop word to add to this object
		"""
		newStopWord = newStopWord.lower()

		# If stop word is not in the list already, add it
		if newStopWord not in self.stop_words:
			self.stop_words.append(newStopWord)

	def getStopWords(self):
		"""	Get all stop words used in this class
			@return	List of stop words
		"""
		return self.stop_words

	def deleteStopWord(self, stopWordToRemove):
		""" Remove a stop word from this class's list
			@param	stopWordToRemove: stop word to remove from this object
		"""
		self.stop_words.remove(stopWordToRemove.lower())

	def removeStopWords(self, text=None, sort=True):
		"""	Remove all stop words from an input list of tokens
			@param	text: List of Strings with stop words to remove
			@return	List of tokens without stop words
		"""

		if type(text) == type(str()):
			text = text.split()

		textWithStopWords    = text
		textWithoutStopWords = list()

		if sort:
			textWithStopWords = sorted(textWithStopWords)

		append = textWithoutStopWords.append

		# Loop through all the words in the text
		for word in textWithStopWords:

			# If the word is not a stop word, add it to textWithoutStopWords
			if word.lower() not in self.stop_words:
				append(word)

		return textWithoutStopWords

	def addStopPunctuation(self, newStopPunctuation):
		""" Add a new stop punctuation to this class's list
			@param	newStopPunctuation: new stop punctuation to add to this object
		"""
		newStopPunctuation = newStopPunctuation.lower()

		# If stop punctuation is not in the list already, add it
		if newStopPunctuation not in self.stop_puncs:
			self.stop_puncs.append(newStopPunctuation)

	def getStopPunctuation(self):
		"""	Get all stop punctuation used in this class
			@return	List of stop punctuation
		"""
		return self.stop_puncs

	def removePunctuation(self, text):
		""" Remove all punctuation from an input text
			@text	text: text String with punctuation to remove
			@return	List of tokens without punctuation
		"""
		# Loop through all the punctuation in self.stop_puncs
		for punctuation in self.stop_puncs:

			# Replace punctuation with leading and trailing spaces
			text = text.replace(" " + punctuation, " ")
			text = text.replace(punctuation + " ", " ")

			# Replace punctuation within the first and last 5 characters of the text
			text = text[:5].replace(punctuation, "") + text[5:]
			text = text[:-5] + text[-5:].replace(punctuation, "")

			# Otherwise, remove the punctuation if not in list specified
			if punctuation not in [".", ",", "-", "--"]:
				text = text.replace(punctuation, "")

		return text

if __name__ =="__main__":
	""" run as a script if this file is run as a stand-alone program
	"""

	d = DocumentPlus("files/archive/test.txt","data/")
	#d.find("This and th:at and ,ever$ything- spice @$%!@is wha#######t makes the world feel about right. in-s$pa@ce.")
	t = d.find("This is a test for this thing, right, test?", "test")
	t = d.findLines(d.open(d.filePath), "american")
	print t

	t = d.findTokens(d.open(d.filePath), "american")
	print t

	a = d.removePunctuation("This and th:at and ,ever$ything- spice @$%!@is wha#######t makes the world feel about right. in-s$pa@ce.")
	b = d.removeStopWords(a.split())
	print "\n.removePunctuation()\t", a
	print ".removeStopWords()\t", b
