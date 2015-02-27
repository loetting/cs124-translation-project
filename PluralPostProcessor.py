from Processor import Processor
import pattern.en

class PluralPostProcessor(Processor):

	def apply(self, tokens):
		for t in tokens:
			if t.plural_noun:
				t.word = pattern.en.pluralize(t.word)
				t.plural_noun = False
				
		return tokens