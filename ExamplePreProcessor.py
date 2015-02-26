# -*- coding: utf-8 -*-
from Processor import Processor

class ExamplePreProcessor(Processor):

	def apply(self, tokens):
		newTokens = []
		for t in tokens:
			newTokens.append(t)
		return newTokens





