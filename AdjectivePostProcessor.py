from Processor import Processor

class AdjectivePostProcessor(Processor):

	def apply(self, tokens):
		leadingNoun = False
		newTokens = tokens[:]
		for i,t in enumerate(tokens):
			if ((t.pos == 'ADJ' or t.pos == 'QU' or t.pos == 'VLadj') and leadingNoun):
				#switch noun and adjective
				newTokens[i], newTokens[i-1] = newTokens[i-1], newTokens[i]
				leadingNoun = False
			elif (t.pos == 'NP' or t.pos == 'NC' or t.pos == 'NMEA'):
				leadingNoun = True
			else:
				leadingNoun = False

		return newTokens