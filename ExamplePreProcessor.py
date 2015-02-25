# -*- coding: utf-8 -*-
from PreProcessor import PreProcessor

class ExamplePreProcessor(PreProcessor):

	def apply(self, tokens):
		newTokens = []
		for t in tokens:
			newTokens.append(t)
		return newTokens





