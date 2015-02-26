from Processor import Processor

class ConjugationPreProcessor(Processor):

	def apply(self, tokens):
		verbs = ['VLfin', 'VLfinf', 'VLfger', 'VEin', 'VEger', 'VEinf', 'VHin', 'VHger', 'VHinf', 'VLin', 'VLger', 'VLinf', 'VMfin', 'VMger', 'VMinf', 'VSfin', 'VSger', 'VSinf']
		for t in tokens:
			if t.pos[0] in verbs:
				#token is a verb
				infinitive = self.lemma


		return tokens