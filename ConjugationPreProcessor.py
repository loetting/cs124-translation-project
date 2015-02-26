from Processor import Processor

class ConjugationPreProcessor(Processor):

	def apply(self, tokens):
		verbs = ['VLfin', 'VLfinf', 'VLfger', 'VEin', 'VEger', 'VEinf', 'VHin', 'VHger', 'VHinf', 'VLin', 'VLger', 'VLinf', 'VMfin', 'VMger', 'VMinf', 'VSfin', 'VSger', 'VSinf']
		for t in tokens:
			if t.pos[0] in verbs:
				verb = t.word
				infinitive = self.lemma
				inf_ending = infinitive[-2:]
				inf_root = infinitive[:-2]
				verb_ending = verb[len(inf_root):]

	            t.plurality = self.plurality_tag(verb, inf_ending, verb_ending)
	            t.mood = self.mood_tag(verb, inf_ending, verb_ending)
	            t.person = self.person_tag(verb, inf_ending, verb_ending)
	            t.tense = self.tense_tag(verb, inf_ending, verb_ending)
	            t.aspect = self.aspect_tag(verb, inf_ending, verb_ending)

		return tokens

	def plurality_tag(self, verb, inf_ending, verb_ending):
		boolean tag = false
	  	if (inf_ending == 'ar'):
	  		plural_endings = ['amos', 'an', 'emos', 'án', 'ábamos', 'aban', 'íamos', 'ían', 'amos', 'aron', 'emos', 'en', 'áramos', 'aran']
	        if verb_ending in plural_endings:
	        	return True
	  	elif (inf_ending == 'er'):
	  		plural_endings = ['emos', 'en', 'emos', 'án', 'íamos', 'ían', 'imos', 'ieron', 'amos', 'an', 'iéramos', 'ieran']
        	if verb_ending in plural_endings:
          		return True
  		elif inf_ending = 'ir':
  			plural_endings = ['imos', 'en',  'emos', 'án', 'íamos', 'ían', 'imos', 'ieron', 'amos', 'an', 'iéramos', 'ieran']
	        if verb_ending in plural_endings:
          		return True
	  	return False

	def mood_tag(self, verb, inf_ending, verb_ending):

	def person_tag(self, verb, inf_ending, verb_ending):

	def tense_tag(self, verb, inf_ending, verb_ending):

	def aspect_tag(self, verb, inf_ending, verb_ending):