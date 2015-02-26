from Processor import Processor
import pattern.en

class ArticlePostProcessor(Processor):

	def apply(self, tokens):
		for i,t in enumerate(tokens):
			if (t.pos == 'ART' and t.word == 'a'):
				t.word = pattern.en.article(tokens[i+1].word)
				
		return tokens