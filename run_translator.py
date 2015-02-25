# -*- coding: utf-8 -*-
from SpanishTranslator import SpanishTranslator
import sys
import re

def loadList(path):
    # Loads text files as lists of lines
    lines = []
    with open(path) as f:
    	for line in f:
    		line = line.replace(".", "")
        	line = line.replace(",", "")
        	line = line.replace(";", "")
        	line = line.replace("(", "")
        	line = line.replace(")", "")
        	line = line.replace(":", "")
        	line = line.replace("!", "")
        	line = line.replace("\"", "")
        	line = line.strip('\n')
        	lines.append(line)
    for line in lines:
    	if not line:
    		lines.remove(line)
    return lines

def main():
	path = ""
	if (len(sys.argv) < 2 or sys.argv[1] == 'dev'):
		path = "data/Project_Corpus_Sentences.txt"
	elif (sys.argv[1] == 'test'):
		path = "data/test.txt"
	
	#load sentences into list
	sentences = loadList(path)

	#create translator
	tr = SpanishTranslator()

	#translate sentences
	trSentences = []
	for sentence in sentences:
		trSentences.append(tr.translate(sentence))

	baseline_translation = []
	for s in trSentences:
		sentence = ""
		for w in s:
			sentence += w + " "
		baseline_translation.append(sentence)
		# print sentence
		# print

	#show Spanish sentence originals with their naive English translations below
	for i in xrange(0, len(baseline_translation)):
		print sentences[i]
		print
		print baseline_translation[i]
		print
		print


if __name__ == '__main__':
    main()