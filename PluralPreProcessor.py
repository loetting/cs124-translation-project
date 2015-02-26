from Processor import Processor

class PluralPreProcessor(Processor):

	def apply(self, tokens):
		for t in tokens:
			if (t.pos == 'NP' or t.pos == 'NC' or t.pos == 'NMEA'):
				if (t.word != t.lemma and t.word[-1] == 's'):
					t.plural_noun = True			

		return tokens