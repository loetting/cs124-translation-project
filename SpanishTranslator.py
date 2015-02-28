# -*- coding: utf-8 -*-
from Processor import Processor
from PluralPreProcessor import PluralPreProcessor
from AdjectivePostProcessor import AdjectivePostProcessor
from PluralPostProcessor import PluralPostProcessor
from ArticlePostProcessor import ArticlePostProcessor
from ConjugationPreProcessor import ConjugationPreProcessor
from ConjugationPostProcessor import ConjugationPostProcessor
from QuePreProcessor import QuePreProcessor
from Dictionary import Dictionary
import snowballstemmer
import re
from StemHelper import StemHelper
from TaggedWord import TaggedWord
from FluencyProcessing import FluencyProcessing
import copy
import random
#import PostProcessor

class SpanishTranslator:
	def __init__(self):
		self.dict = Dictionary()
		#build CCAE dictionaries:
		bigram_filename = "CAE_bigrams.txt"
		trigram_filename = "CAE_trigrams.txt"
		# self.dict.build_english_bigrams(bigram_filename, "data")
		# self.dict.build_english_trigrams(trigram_filename, "data")
		self.dict.build_english_corpus("google_translate.txt", "data")
		# self.stem_helper_inst = StemHelper()
		# self.preProcessors = [ConjugationPreProcessor(), PluralPreProcessor(), QuePreProcessor()]
		self.preProcessors = [ConjugationPreProcessor(), PluralPreProcessor(), QuePreProcessor()]
		# self.preProcessors = []
		#add plural processor back in
		# self.postProcessors = [AdjectivePostProcessor(), ArticlePostProcessor(), ConjugationPostProcessor(), PluralPostProcessor()]
		self.postProcessors = [AdjectivePostProcessor(), ArticlePostProcessor(), ConjugationPostProcessor(), PluralPostProcessor()]
		# self.postProcessors = []

		corpusFilename = "Project_Dev_Sentences.txt"
		googleTranslate = "Translation_Strict_Keys.txt"
		self.dict.build_custom_dictionary(corpusFilename, "data", googleTranslate)
		self.spanish_stemmer = snowballstemmer.stemmer('spanish');
		self.fluency_processor_inst = FluencyProcessing()

	def translate(self, original):

		translated = ""

		#do all the tokenizing, POS-tagging, etc here
		tokens = TaggedWord.TagText(original)
		for t in tokens:
			t.lower()

		# apply preprocessing strategies
		for pre in self.preProcessors:
			tokens = pre.apply(tokens)

		#generate possible translations
		self.translations = []
		self.generateTranslations(tokens, 0)

		#post-processing
		# for i,translation in enumerate(self.translations):
		for i in xrange(0, len(self.translations)):
			for post in self.postProcessors:
				# translation = post.apply(translations)
				self.translations[i] = post.apply(self.translations[i])
				# self.translations[i] = translation

		# select best translation
		english_sentences = []
		for translation in self.translations:
			sentence = ""
			for token in translation:
				sentence += token.word.decode('utf-8') + " "
			sentence = sentence.replace(".","")
			english_sentences.append(sentence)

			# english_sentences.append(translation)

		for sentence in english_sentences:
			print sentence
			print

		# ccae_flag = True
		ccae_flag = False
		bigram_prob_list = self.fluency_processor_inst.find_fluent_translation_stupidbackoff(english_sentences, self.dict.custom_bigram_dict, self.dict.custom_bigram_dict_unigram_dict, ccae_flag)
		trigram_prob_list = self.fluency_processor_inst.find_fluent_translation_trigrams(english_sentences, self.dict.custom_trigram_dict, self.dict.custom_trigram_dict_unigram_dict, ccae_flag, self.dict.custom_bigram_dict, self.dict.custom_bigram_dict_unigram_dict)
		
		#can modify weight of each language model
		# bigram_weight = .5
		bigram_weight = .2
		trigram_weight = .8

		fluent_sentence = self.fluency_processor_inst.find_combined_fluency(english_sentences, bigram_prob_list, trigram_prob_list, bigram_weight, trigram_weight)

		return fluent_sentence
		#to test without the fluency_processor, comment out above line and add:
		# return english_sentences[0]

	def generateTranslations(self, tokens, position):
		# if (position == len(tokens)):
		if position == len(tokens):
			sentence = ""
			for token in tokens:
				sentence += token.word.decode('utf-8') + " "
			# print sentence
			print position

			self.translations.append(tokens)
		else:
			options = self.dict.custom_dict[tokens[position].word]
			newTokens = copy.deepcopy(tokens[:])
			# newTokens = tokens[:]

			match_options = []
			for opt in options:
				if tokens[position].posMatch(opt[1]):
					match_options.append(opt)

			if len(match_options) > 1:
				if random.random() <= .2:
					count = 0
					while (count < 2 and count < len(match_options)):

						newTokens[position].word = match_options[count][0]
						self.generateTranslations(newTokens, position + 1)
						count = count + 1
				else:
					newTokens[position].word = match_options[0][0]
					self.generateTranslations(newTokens, position + 1)

			elif match_options:
				newTokens[position].word = match_options[0][0]
				self.generateTranslations(newTokens, position + 1)
			else:
				self.generateTranslations(newTokens, position + 1)

			