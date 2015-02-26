import os

class TaggedWord:

	def __init__(self, triple):
		self.original = triple[0]
		self.word = triple[0]
		self.pos = triple[1]
		self.lemma = triple[2]
		self.verb = False
		self.tense = 'present'
		self.plural_noun = False
		self.plurality = 0
		self.mood = 'indicative'
		self.aspect = 0
		self.person = 0
		self.gender = 0	


		self.dict_to_pos = {
			'noun' : ['NC', 'NP', 'NMEA'],
			'pronoun' : ['PPO', 'PPC', 'PPX', 'REL', 'DM', 'INT'],
			'conjunction' : ['CSUBI', 'CSUBF', 'CSUBX', 'CQUE'],
			'preposition' : ['PREP', 'PAL', 'PDEL'],
			'adjective' : ['ADJ', 'QU', 'VHadj', 'VEadj', 'VLadj', 'VMadj', 'VSadj'],
			'adverb' : ['ADV'],
			'particle' : ['SE'],
			'article' : ['ART'],
			'verb' : ['VLfin', 'VLfinf', 'VLfger', 'VEin', 'VEger', 'VEinf', 'VHin', 'VHger', 'VHinf', 'VLin', 'VLger', 'VLinf', 'VMfin', 'VMger', 'VMinf', 'VSfin', 'VSger', 'VSinf']
		}

	def lower(self):
		self.word = self.word.lower()

	def posMatch(self, pos):
		if pos == 'unknown':
			return True
		if not pos in self.dict_to_pos:
			return True
		posTags = self.dict_to_pos[pos]
		if self.pos in posTags:
			return True
		return False


	@staticmethod
	def formatTaggedWords(output):
		words = []
		for w in output:
			words.append(TaggedWord(w.split("\t")))
		return words

	@staticmethod
	def TagText(text):
		taggedWords = []
		command = "echo '" + text + "' | cmd/tree-tagger-spanish"
		result = os.popen(command).read()
		result = result.split("\n")
		for item in result:
			if not item:
				continue
			elems = item.split("\t")
			taggedWords.append(TaggedWord(elems))
		return taggedWords
