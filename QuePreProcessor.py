# -*- coding: utf-8 -*-
from Processor import Processor

class QuePreProcessor(Processor):

	def apply(self, tokens):
		for i,t in enumerate(tokens):
			if (t.word == 'que'):
				if (i > 1 and tokens[i-1].word == 'en'):
					t.word = 'which'
				elif (i > 1 and tokens[i-1].pos == 'NP'):
					t.word = 'who'
				elif (i > 1 and tokens[i-1].pos == 'NC'):
					t.word = 'that'
			elif (t.word == 'en que'):
				t.word == 'in which'
			elif (t.word == 'así que'):
				t.word = 'so'
				
		return tokens