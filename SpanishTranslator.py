# -*- coding: utf-8 -*-
from Processor import Processor
from ConjugationPreProcessor import ConjugationPreProcessor
from PluralPreProcessor import PluralPreProcessor
from AdjectivePostProcessor import AdjectivePostProcessor
from PluralPostProcessor import PluralPostProcessor
from ArticlePostProcessor import ArticlePostProcessor
from Dictionary import Dictionary
import snowballstemmer
import re
from StemHelper import StemHelper
import treetaggerwrapper
from TaggedWord import TaggedWord
#import PostProcessor

class SpanishTranslator:
	def __init__(self):
		self.dict = Dictionary()
		self.stem_helper_inst = StemHelper()
		self.preProcessors = [ConjugationPreProcessor(), PluralPreProcessor()]
		self.postProcessors = [AdjectivePostProcessor(), PluralPostProcessor(), ArticlePostProcessor()]
		corpusFilename = "Project_Dev_Sentences.txt"
		googleTranslate = "Translation_Strict_Keys.txt"
		self.dict.build_custom_dictionary(corpusFilename, "data", googleTranslate)
		self.spanish_stemmer = snowballstemmer.stemmer('spanish');

	def translate(self, original):

		translated = ""

		#do all the tokenizing, POS-tagging, etc here
		tokens = TaggedWord.TagText(original)
		for t in tokens:
			t.lower()

		#apply preprocessing strategies
		for pre in self.preProcessors:
			tokens = pre.apply(tokens)

		#generate possible translations
		self.translations = []
		self.generateTranslations(tokens, 0)

		#post-processing
		for post in self.postProcessors:
			for i,translation in enumerate(self.translations):
				self.translations[i] = post.apply(translation)

		#select best translation
				
		return self.translations[0]


	def generateTranslations(self, tokens, position):
		if (position == len(tokens)):
			self.translations.append(tokens)
		else:
			options = self.dict.custom_dict[tokens[position].word]
			newTokens = tokens[:]

			match_options = []
			for opt in options:
				if tokens[position].posMatch(opt[1]):
					match_options.append(opt)

			if match_options:
				newTokens[position].word = match_options[0][0]
			elif options:
				newTokens[position].word = options[0][0]

			self.generateTranslations(newTokens, position + 1)

			