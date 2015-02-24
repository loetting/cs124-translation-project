# cs124-translation-project

____
Author: Gilbert Doan

COMMIT/PUSH NAME: Testing 123
This commit includes the dictionary class and the driver class to use dictionary class' functions. The dictionary class has a function that builds a language model from the Corpus of Contemporary American English (bigram, trigram, fourgram, and fivegram). It also has a generic function to parse a text document of English sentences to build our own custom language model (bigrams, trigrams). That is, we can look at other types of text to augment the first language model if we want. Finally, it also builds our custom dictionary for the 15 Spanish sentences we chose. For each Spanish word, this function parses translations from Google Translate and Word Reference. The translations are sometimes stemmed to the generic adjective or verb.

The Driver class has functions I use to test the Dictionary class. It shows some use-cases for the Dictionary class and its objects.

Note: There is a function built for a 4.8k Spanish-English dictionary too, but we probably will not use it.


COMMIT/PUSH NAME: Input Data Needed to Build Dictionaries
This commits the data files needed to build our custom dictionary and the language models. Files are called in the Driver class, showing each files use case.


COMMIT/PUSH NAME: Added Fluency Processor, Updated Dictionary, Updated Driver
This commit includes a fluency processor (of English sentences) that uses bigram probability scoring with stupid backoff. It also uses trigram probability scoring with Laplace smoothing. Both probability scores are combined, and the highest score is the most fluent English sentence.

The Dictionary class was also updated to reflect necessary data items needed to build the fluency processor. No changes aside from those discussed with Alessandro, were made to the custom dictionary (our corpus of 15 Spanish sentences).

Driver was updated to show how to use the fluency processor.


COMMIT/PUSH NAME: Refactored Dictionary and Fluency Processing. Added Bleu Score Evaluator given by CS124 Staff for translation evaluation.
___