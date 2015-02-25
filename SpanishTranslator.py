# -*- coding: utf-8 -*-
from PreProcessor import PreProcessor
from ExamplePreProcessor import ExamplePreProcessor
from Dictionary import Dictionary
import snowballstemmer
import re
from StemHelper import StemHelper
#import PostProcessor

class SpanishTranslator:
	def __init__(self):
		self.dict = Dictionary()
		self.stem_helper_inst = StemHelper()

		self.preProcessors = [ExamplePreProcessor()]
		corpusFilename = "Project_Corpus_Sentences.txt"
		googleTranslate = "Read_Automatic_Translation.txt"
		self.dict.build_custom_dictionary(corpusFilename, "data", googleTranslate)

		for word in self.dict.custom_dict:
			print word
		# print self.dict.custom_dict["quienes"]

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

				#augmenting automated stemmer to help us find matching Spanish words in our dictionary
				matching_dict_word = self.stem_helper_inst.find_dictionary_match(tokens[position], self.dict)
				options = self.dict.custom_dict[matching_dict_word]
				
				if not options:
					newTokens[position] = "UNK"
				else:
					newTokens[position] = options[0][0]
				

				# newTokens[position] = options[0][0]
				self.generateTranslations(newTokens, position + 1)
			else:
				newTokens = tokens[:]
				newTokens[position] = options[0][0]
				self.generateTranslations(newTokens, position + 1)

			