# -*- coding: utf-8 -*-
from Processor import Processor
from pattern.en import PAST, PRESENT, FUTURE, IMPERATIVE, SUBJUNCTIVE, INDICATIVE, INFINITIVE
import pattern.en
class ConjugationPreProcessor(Processor):

	def apply(self, tokens):
		verbs = ['VLfin', 'VLfinf', 'VLfger', 'VEin', 'VEger', 'VEinf', 'VHin', 'VHger', 'VHinf', 'VLin', 'VLger', 'VLinf', 'VMfin', 'VMger', 'VMinf', 'VSfin', 'VSger', 'VSinf']
		for t in tokens:
			if t.pos in verbs:
				verb = t.original
				t.verb = True
				infinitive = t.lemma
				inf_ending = infinitive[-2:]
				inf_root = infinitive[:-2]
				verb_ending = verb[len(inf_root):]

				t.plurality = self.plurality_tag(verb, inf_ending, verb_ending)
				t.mood = self.mood_tag(verb, inf_ending, verb_ending)
				t.person = self.person_tag(verb, inf_ending, verb_ending)
				t.tense = self.tense_tag(verb, inf_ending, verb_ending)
				t.aspect = self.aspect_tag(verb, inf_ending, verb_ending)
				t.participle = self.participle_tag(verb, inf_ending, verb_ending)

		return tokens

	def plurality_tag(self, verb, inf_ending, verb_ending):
		if (inf_ending == 'ar'):
			plural_endings = ['amos', 'an', 'emos', 'án', 'ábamos', 'aban', 'íamos', 'ían', 'amos', 'aron', 'emos', 'en', 'áramos', 'aran']
			if verb_ending in plural_endings:
				return True
		elif (inf_ending == 'er'):
			plural_endings = ['emos', 'en', 'emos', 'án', 'íamos', 'ían', 'imos', 'ieron', 'amos', 'an', 'iéramos', 'ieran']
			if verb_ending in plural_endings:
				return True
		elif (inf_ending == 'ir'):
			plural_endings = ['imos', 'en',  'emos', 'án', 'íamos', 'ían', 'imos', 'ieron', 'amos', 'an', 'iéramos', 'ieran']
			if verb_ending in plural_endings:
				return True
		return False

	def mood_tag(self, verb, inf_ending, verb_ending):
		if (inf_ending == 'ar'):
			sub_endings = ['e', 'es', 'emos', 'en', 'ara', 'aras', 'áramos', 'aran']
			imp_endings = ['a', 'e', 'emos', 'en']
			non_ind_endings = ['ando', 'ado']
			if verb_ending in sub_endings:  
				return SUBJUNCTIVE
			elif verb_ending in imp_endings:
				return IMPERATIVE
			elif verb_ending not in non_ind_endings:
				return INDICATIVE
		elif (inf_ending == 'er'):
			sub_endings = ['a', 'as', 'amos', 'an', 'iera', 'ieras', 'iéramos', 'ieran']
			imp_endings = ['e', 'a', 'amos', 'an']
			non_ind_endings = ['iendo', 'ido']
			if verb_ending in sub_endings:  
				return SUBJUNCTIVE
			elif verb_ending in imp_endings:
				return IMPERATIVE
			elif verb_ending not in non_ind_endings:
				return INDICATIVE
		elif (inf_ending == 'ir'):
			sub_endings = ['a', 'as', 'amos', 'an', 'iera', 'ieras', 'iéramos', 'ieran']
			imp_endings = ['e', 'a', 'amos', 'an']
			non_ind_endings = ['iendo', 'ido']
			if verb_ending in sub_endings:  
				return SUBJUNCTIVE
			elif verb_ending in imp_endings:
				return IMPERATIVE
			elif verb_ending not in non_ind_endings:
				return INDICATIVE
		return None
	
	def participle_tag(self, verb, inf_ending, verb_ending):
		if (inf_ending == 'ar'):
			part_endings = ['ando', 'ado']
			if verb_ending in part_endings:
				return True
		elif (inf_ending == 'er', inf_ending == 'ir'):
			part_endings = ['iendo', 'ido']
			if verb_ending in part_endings:
				return True
		return False

	def person_tag(self, verb, inf_ending, verb_ending):
		if (inf_ending == 'ar'):
			one_endings = ['o' or 'amos' or 'aré' or 'aremos' or 'ábamos' or 'aríamos' or 'é' or 'emos' or 'áramos']
			two_endings = ['as' or 'arás' or 'abas' or 'arías' or 'aste' or 'es' or 'aras']
			three_endings = ['a' or 'an' or 'ará' or 'arán' or 'aba' or 'aban' or 'aría' or 'arían' or 'ó' or 'aron' or 'e' or 'en' or 'ara' or 'aran']
			if verb_ending in one_endings:  
				return 1
			elif verb_ending in two_endings:
				return 2
			elif verb_ending in three_endings:
				return 3
		elif (inf_ending == 'er'):
			one_endings = ['o' or 'emos' or 'eré' or 'eremos' or 'íamos' or 'eríamos' or 'í' or 'imos' or 'amos' or 'iéramos']
			two_endings = ['es' or 'erás' or 'ías' or 'erías' or 'iste' or 'as' or 'ieras']
			three_endings = ['e' or 'en' or 'erá' or 'erán' or 'ía' or 'ían' or 'ería' or 'erían' or 'ió' or 'ieron' or 'an' or 'a' or 'iera' or 'ieran']
			if verb_ending in one_endings:  
				return 1
			elif verb_ending in two_endings:
				return 2
			elif verb_ending in three_endings:
				return 3
		elif (inf_ending == 'ir'):
			one_endings = ['o' or 'imos' or 'iré' or 'iremos' or 'íamos' or 'iríamos' or 'í' or 'amos' or 'iéramos']
			two_endings = ['es' or 'irás' or 'ías' or 'irías' or 'iste' or 'as' or 'ieras']
			three_endings = ['e' or 'en' or 'irá' or 'irán' or 'ía' or 'ían' or 'iría' or 'irían' or 'ió' or 'ieron' or 'an' or 'a' or 'iera' or 'ieran']
			if verb_ending in one_endings:  
				return 1
			elif verb_ending in two_endings:
				return 2
			elif verb_ending in three_endings:
				return 3
		return 3

	def tense_tag(self, verb, inf_ending, verb_ending):
		if (inf_ending == 'ar'):
			present_endings = ['o', 'as', 'a', 'aría', 'arías', 'aríamos', 'arían', 'e', 'emos', 'en', 'es', 'ando']
			future_endings = ['aré', 'arás', 'ará', 'aremos', 'arán']
			past_endings = ['aba', 'abas', 'aba', 'ábamos', 'aban', 'é', 'ó', 'amos', 'an', 'ara', 'aras', 'áramos', 'aran', 'ado']
			if verb_ending in present_endings:  
				return PRESENT
			elif verb_ending in future_endings:
				return FUTURE
			elif verb_ending in past_endings:
				return PAST
		elif (inf_ending == 'er'):
			present_endings = ['o', 'es', 'e', 'emos', 'en', 'ería', 'erías', 'eríamos', 'erían', 'a' 'amos', 'an', 'as', 'iendo']
			future_endings = ['eré', 'erás', 'erá', 'eremos', 'erán']
			past_endings = ['ía', 'ías', 'íamos', 'ían', 'imos', 'ieron', 'iera', 'ieras', 'iéramos', 'ieran', 'ido']
			if verb_ending in present_endings:
				return PRESENT
			elif verb_ending in future_endings:
				return FUTURE
			elif verb_ending in past_endings: 
				return PAST
		elif (inf_ending == 'ir'):
			present_endings = ['o', 'es', 'e', 'imos', 'en', 'iría', 'irías', 'iríamos', 'irían', 'a', 'amos', 'an', 'as', 'iendo']
			future_endings = ['iré', 'irás', 'irá', 'iremos', 'irán']
			past_endings = ['ía', 'ías', 'íamos', 'ían', 'ían', 'imos', 'ieron', 'iera', 'ieras', 'iéramos', 'ieran', 'ido']
			if verb_ending in present_endings:
				return PRESENT
			elif verb_ending in future_endings:
				return FUTURE
			elif verb_ending in past_endings:
				return PAST
		return INFINITIVE

	def aspect_tag(self, verb, inf_ending, verb_ending):
		if (inf_ending == 'ar'):
			imp_endings = ['aba', 'abas', 'ábamos', 'aban', 'ara', 'aras', 'áramos', 'aran']
			perf_endings = ['é', 'aste', 'ó', 'amos', 'aron']
			if verb_ending in imp_endings:  
				return 'IMPERFECTIVE'
			elif verb_ending in perf_endings:
				return 'PERFECTIVE'
		elif (inf_ending == 'er', inf_ending == 'ir'):
			imp_endings = ['ía', 'ías', 'íamos', 'ían', 'iera', 'ieras', 'iéramos', 'ieran']
			perf_endings = ['í', 'iste', 'ió', 'imos', 'ieron']
			if verb_ending in imp_endings:
				return 'IMPERFECTIVE'
			elif verb_ending in perf_endings:
				return 'PERFECTIVE'

		return None






