from TaggedWord import TaggedWord
from subprocess import call
import os

class posTagger:

	@staticmethod
	def TagWord(text):
		taggedWord = ""
		command = "echo '" + text + "' | cmd/tree-tagger-spanish"
		result = os.popen(command).read()
		result = result.split("\n")
		for item in result:
			if not item:
				continue
			elems = item.split("\t")
			return TaggedWord(elems)