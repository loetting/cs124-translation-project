from Processor import Processor

class ConjugationPreProcessor(Processor):

	def apply(self, tokens):
		for t in tokens:
			if (t.pos[0] == 'V'):
				#token is a verb
				t.verb = True

		return tokens