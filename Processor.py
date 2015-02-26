# -*- coding: utf-8 -*-
import abc

class Processor():
	_metaclass_ = abc.ABCMeta

	@abc.abstractmethod
	def apply(self, tokens):
		print "This should not happen, make sure to implement a new subclass for your PreProcessing module."
		return tokens