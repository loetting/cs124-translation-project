# -*- coding: utf-8 -*-
from Processor import Processor
import pattern.en

class ConjugationPostProcessor(Processor):

	def apply(self, tokens):
		verbs = ['VLfin', 'VLfinf', 'VLfger', 'VEin', 'VEger', 'VEinf', 'VHin', 'VHger', 'VHinf', 'VLin', 'VLger', 'VLinf', 'VMfin', 'VMger', 'VMinf', 'VSfin', 'VSger', 'VSinf']
		for t in tokens:
			if t.pos in verbs:
				conjugation = t.word
				if (t.tense == pattern.en.PRESENT):
					if (t.participle):
						conjugation = pattern.en.conjugate(t.word, tense=pattern.en.PARTICIPLE)
					elif (t.plurality):
						conjugation = pattern.en.conjugate(t.word,'pl')
					elif (t.person == 1):
						conjugation = pattern.en.conjugate(t.word,'1sg')
					elif (t.person == 2):
						conjugation = pattern.en.conjugate(t.word,'2sg')
					elif (t.person == 3):
						conjugation = pattern.en.conjugate(t.word,'3sg')

				elif (t.tense == pattern.en.PAST):
					if (t.participle):
						conjugation = pattern.en.conjugate(t.word, tense=pattern.en.PAST+pattern.en.PARTICIPLE)
					elif (t.plurality):
						conjugation = pattern.en.conjugate(t.word,'ppl')
					elif (t.person == 1):
						conjugation = pattern.en.conjugate(t.word,'1sgp')
					elif (t.person == 2):
						conjugation = pattern.en.conjugate(t.word,'2sgp')
					elif (t.person == 3):
						conjugation = pattern.en.conjugate(t.word,'3sgp')

				t.word = conjugation
		return tokens
