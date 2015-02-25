# -*- coding: utf-8 -*-
from PreProcessor import PreProcessor
from ExamplePreProcessor import ExamplePreProcessor
from Dictionary import Dictionary
import snowballstemmer
import re
#import PostProcessor

class SpanishTranslator:
	def __init__(self):
		self.dict = Dictionary()
		self.preProcessors = [ExamplePreProcessor()]
		corpusFilename = "Project_Corpus_Sentences.txt"
		googleTranslate = "Read_Automatic_Translation.txt"
		self.dict.build_custom_dictionary(corpusFilename, "data", googleTranslate)
		self.spanish_stemmer = snowballstemmer.stemmer('spanish');

	def translate(self, original):

		translated = ""

		#do all the tokenizing, POS-tagging, etc here
		original = original.lower()
		tokens = original.split()

		tokens = self.spanish_stemmer.stemWords(tokens);

		#apply preprocessing strategies
		for pre in self.preProcessors:
			tokens = pre.apply(tokens)

		#generate possible translations
		self.translations = []
		self.generateTranslations(tokens, 0)

		#post-processing

		#select best translation
				
		return self.translations[0]


	def generateTranslations(self, tokens, position):
		if (position == len(tokens)):
			self.translations.append(tokens)
		else:
			options = self.dict.custom_dict[tokens[position]]
			if not options:
				newTokens = tokens[:]
				newTokens[position] = "UNK"
				self.generateTranslations(newTokens, position + 1)
			else:
				newTokens = tokens[:]
				newTokens[position] = options[0][0]
				self.generateTranslations(newTokens, position + 1)

			