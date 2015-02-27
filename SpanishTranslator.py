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
#import PostProcessor

class SpanishTranslator:
	def __init__(self):
		self.dict = Dictionary()
		#build CCAE dictionaries:
		bigram_filename = "CAE_bigrams.txt"
		trigram_filename = "CAE_trigrams.txt"
		self.dict.build_english_bigrams(bigram_filename, "data")
		self.dict.build_english_trigrams(trigram_filename, "data")

		# self.stem_helper_inst = StemHelper()
		self.preProcessors = [ConjugationPreProcessor(), PluralPreProcessor(), QuePreProcessor()]
		self.postProcessors = [AdjectivePostProcessor(), PluralPostProcessor(), ArticlePostProcessor(), ConjugationPostProcessor()]
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
		for post in self.postProcessors:
			for i,translation in enumerate(self.translations):
				self.translations[i] = post.apply(translation)

		# select best translation
		english_sentences = []
		for translation in self.translations:
			sentence = ""
			for token in translation:
				sentence += token.word.decode('utf-8') + " "
			english_sentences.append(sentence)


		
		#random characters to test fluency processor (this sentence addition is highly unlikely because of the b's)
		#so it should not be picked relative to our machine translation
		#PASS
		english_sentences.append("b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b")
		english_sentences.append("This sentence should win as fluent")
		ccae_flag = True
		bigram_prob_list = self.fluency_processor_inst.find_fluent_translation_stupidbackoff(english_sentences, self.dict.english_bigram_dict, self.dict.english_bigram_dict_unigram_dict, ccae_flag)
		trigram_prob_list = self.fluency_processor_inst.find_fluent_translation_trigrams(english_sentences, self.dict.english_trigram_dict, self.dict.english_trigram_dict_unigram_dict, ccae_flag, self.dict.english_bigram_dict, self.dict.english_bigram_dict_unigram_dict)
		
		#can modify weight of each language model
		bigram_weight = .5
		trigram_weight = .5

		fluent_sentence = self.fluency_processor_inst.find_combined_fluency(english_sentences, bigram_prob_list, trigram_prob_list, bigram_weight, trigram_weight)

		return fluent_sentence

		# return self.translations[0]


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

			