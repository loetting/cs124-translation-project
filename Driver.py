# -*- coding: utf-8 -*-
from Dictionary import Dictionary
import sys


"""
Driver class showing how to use the functions in Dictionary class
All print functions and one initializer function (main)
"""

"""
Corpus of Contemporary American English: dictionary_index: (2, bigram), (3, trigram), (4, fourgram), (5, fivegram)
"""
def validate_dictionary(dict_inst, dictionary_index):

    if dictionary_index == 2:
        for bigram in dict_inst.english_bigram_dict:
            print bigram + ": " + str(dict_inst.english_bigram_dict[bigram])
    elif dictionary_index == 3:
        for trigram in dict_inst.english_trigram_dict:
            print trigram + ": " + str(dict_inst.english_trigram_dict[trigram])
    elif dictionary_index == 4:
        for fourgram in dict_inst.english_fourgram_dict:
            print fourgram + ": " + str(dict_inst.english_fourgram_dict[fourgram])
    elif dictionary_index == 5:
        for fivegram in dict_inst.english_fivegram_dict:
            print fivegram + ": " + str(dict_inst.english_fivegram_dict[fivegram])

"""
Extra dictionary
"""
def validate_bilingual_dictionary(dict_inst):
    for spanish_word in dict_inst.spanish_dict:
        print spanish_word + ": " + str(dict_inst.spanish_dict[spanish_word])
    
    print len(dict_inst.spanish_dict)

"""
Custom English bigram dictionary
"""
def validate_custom_bigram_dict(dict_inst):
    for word in dict_inst.custom_bigram_dict:
        print word + ": " + str(dict_inst.custom_bigram_dict[word])

"""
Custom English trigram dictionary
"""
def validate_custom_trigram_dict(dict_inst):
    for word in dict_inst.custom_trigram_dict:
        print word + ": " + str(dict_inst.custom_trigram_dict[word])

"""
Corpus of 15 sentences: Custom dictionary for project
"""
def validate_custom_dict(dict_inst):
    for word in dict_inst.custom_dict:
        # if len(dict_inst.custom_dict[word]) == 0:
        print word + ": " + str(dict_inst.custom_dict[word])
        print ""

"""
Corpus of 15 sentences: Show words
"""

def validate_word_custom_dict(dict_inst, spanish_word):
    print spanish_word + ": " + str(dict_inst.custom_dict[spanish_word])


"""
Initializer function to call other functions in Dictionary class
"""
def main(dir_name):
    dict_inst = Dictionary()
    # bigram_filename = "CAE_bigrams.txt"
    # dict_inst.build_english_bigrams(bigram_filename, sys.argv[1])

    # trigram_filename = "CAE_trigrams.txt"
    # dict_inst.build_english_trigrams(trigram_filename, sys.argv[1])

    # fourgram_filename = "CAE_fourgrams.txt"
    # dict_inst.build_english_fourgrams(fourgram_filename, sys.argv[1])

    # fivegram_filename = "CAE_fivegrams.txt"
    # dict_inst.build_english_fivegrams(fivegram_filename, sys.argv[1])

    # validate_dictionary(dict_inst, 5)

    # euro_parl_doc = "europarl-v7.es-en.en"
    # dict_inst.build_english_corpus(euro_parl_doc, sys.argv[1])

    # custom_doc = "Test_English_Corpus_Read.txt"
    # dict_inst.build_english_corpus(custom_doc, sys.argv[1])
    # validate_custom_bigram_dict(dict_inst)
    # validate_custom_trigram_dict(dict_inst)

    # bilingual_dict_filename1 = "Bilingual_Dict1.txt"
    # bilingual_dict_filename2 = "Bilingual_Dict2.txt"
    # bilingual_filename_list = []
    # bilingual_filename_list.append(bilingual_dict_filename1)
    # bilingual_filename_list.append(bilingual_dict_filename2)
    # dict_inst.build_bilingual_dictionary(bilingual_filename_list, sys.argv[1])

    # validate_bilingual_dictionary(dict_inst)

    working_corpus_filename = "Project_Corpus_Sentences.txt"
    google_translate_doc = "Read_Automatic_Translation.txt"
    dict_inst.build_custom_dictionary(working_corpus_filename, sys.argv[1], google_translate_doc)

    validate_custom_dict(dict_inst)


"""
Put the directory of data files in argument 1, when calling "python Driver.py"
"""
if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print "Error in data directory input"
        sys.exit(0)
    main(sys.argv[1])