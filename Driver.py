# -*- coding: utf-8 -*-
from Dictionary import Dictionary
from FluencyProcessing import FluencyProcessing
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
        # for bigram in dict_inst.english_bigram_dict:
            # print bigram + ": " + str(dict_inst.english_bigram_dict[bigram])
        print len(dict_inst.english_bigram_dict_unigram_dict)
    elif dictionary_index == 3:
        # for trigram in dict_inst.english_trigram_dict:
            # print trigram + ": " + str(dict_inst.english_trigram_dict[trigram])
        print len(dict_inst.english_trigram_dict_unigram_dict)
    elif dictionary_index == 4:
        # for fourgram in dict_inst.english_fourgram_dict:
            # print fourgram + ": " + str(dict_inst.english_fourgram_dict[fourgram])
        print len(dict_inst.english_fourgram_dict_unigram_dict)
    elif dictionary_index == 5:
        # for fivegram in dict_inst.english_fivegram_dict:
            # print fivegram + ": " + str(dict_inst.english_fivegram_dict[fivegram])
        print len(dict_inst.english_fivegram_dict_unigram_dict)

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
This Driver call tests the fluency of n English sentences according to the CCAE dictionaries or custom dictonaries.
To use custom dictionaries, comment them in and put the ccae_flag = False. Also, custom dictionaries bigram and trigram
built from a custom document (novel, newspaper, etc.)
"""
def validate_fluency_processor(dict_inst, fluency_processing_inst):
    #use these with CCAE dictionary
    bigram_dict = dict_inst.english_bigram_dict
    bigram_dict_unigram_dict = dict_inst.english_bigram_dict_unigram_dict
    trigram_dict = dict_inst.english_trigram_dict
    trigram_dict_unigram_dict = dict_inst.english_trigram_dict_unigram_dict

    #use these with custom dictionary
    # bigram_dict = dict_inst.custom_bigram_dict
    # bigram_dict_unigram_dict = dict_inst.custom_bigram_dict_unigram_dict
    # trigram_dict = dict_inst.custom_trigram_dict
    # trigram_dict_unigram_dict = dict_inst.custom_trigram_dict_unigram_dict

    #TESITNG AREA:
    # test_english_sentences = ["The cat jumped over the fence", "The cat hopped over the fence", "The cat moved over the fence", "The cat skipped over the fence"]
    # test_english_sentences = ["The dog barks at the guy", "The dog barks at the fellow", "The dog barks at the male", "The dog barks at the man", "The dog barks at the human", "The dog barks at the homo sapien"]
    # test_english_sentences = ["The man is well read", "The man is literary", "The man is knowledgeable", "The man is erudite", "The man is smart", "The man is intelligent", "The man is a genius"]
    
    #EXAMPLE: chooses "The verdant witch"
    #Find possible English translations for: La bruja verde
    #Find most fluent translation
    test_english_sentences = ["The green witch", "The underdeveloped witch", "The verdant witch", "The greeny witch", "The green hag", "The green beldam", "The green crone", "The green sorceress", "The green night-hag", "The green hex", "The green harridan", "The green bitch", "The verdant hag", "The verdant beldam", "The verdant crone", "The verdant sorceress", "The verdant night-hag", "The verdant hex", "The verdant harridan", "The verdant bitch", "The underdeveloped hag", "The underdeveloped beldam", "The underdeveloped crone", "The underdeveloped sorceress", "The underdeveloped night-hag", "The underdeveloped hex", "The under-developed harridan", "The underdeveloped bitch"]
    

    ccae_flag = True
    # ccae_flag = False
    bigram_prob_list = fluency_processing_inst.find_fluent_translation_stupidbackoff(test_english_sentences, bigram_dict, bigram_dict_unigram_dict, ccae_flag)
    trigram_prob_list = fluency_processing_inst.find_fluent_translation_trigrams(test_english_sentences, trigram_dict, trigram_dict_unigram_dict, ccae_flag, bigram_dict, bigram_dict_unigram_dict)

    fluent_sentence = fluency_processing_inst.find_combined_fluency(test_english_sentences, bigram_prob_list, trigram_prob_list)
    print "Test English Sentences:"
    print test_english_sentences

    print "Most fluent sentence: " + fluent_sentence


"""
Initializer function to call other functions in Dictionary class
"""
def main(dir_name):
    dict_inst = Dictionary()
    bigram_filename = "CAE_bigrams.txt"
    dict_inst.build_english_bigrams(bigram_filename, sys.argv[1])

    trigram_filename = "CAE_trigrams.txt"
    dict_inst.build_english_trigrams(trigram_filename, sys.argv[1])

    # fourgram_filename = "CAE_fourgrams.txt"
    # dict_inst.build_english_fourgrams(fourgram_filename, sys.argv[1])

    # fivegram_filename = "CAE_fivegrams.txt"
    # dict_inst.build_english_fivegrams(fivegram_filename, sys.argv[1])

    # validate_dictionary(dict_inst, 2)
    # validate_dictionary(dict_inst, 3)
    # validate_dictionary(dict_inst, 4)
    # validate_dictionary(dict_inst, 5)
    
    custom_doc = "Test_English_Corpus_Read.txt"
    dict_inst.build_english_corpus(custom_doc, sys.argv[1])
    validate_custom_bigram_dict(dict_inst)
    validate_custom_trigram_dict(dict_inst)


    fluency_processing_inst = FluencyProcessing()
    validate_fluency_processor(dict_inst, fluency_processing_inst)


    # bilingual_dict_filename1 = "Bilingual_Dict1.txt"
    # bilingual_dict_filename2 = "Bilingual_Dict2.txt"
    # bilingual_filename_list = []
    # bilingual_filename_list.append(bilingual_dict_filename1)
    # bilingual_filename_list.append(bilingual_dict_filename2)
    # dict_inst.build_bilingual_dictionary(bilingual_filename_list, sys.argv[1])

    # validate_bilingual_dictionary(dict_inst)

    # working_corpus_filename = "Project_Corpus_Sentences.txt"
    # google_translate_doc = "Read_Automatic_Translation.txt"
    # dict_inst.build_custom_dictionary(working_corpus_filename, sys.argv[1], google_translate_doc)

    # validate_custom_dict(dict_inst)


"""
Put the directory of data files in argument 1, when calling "python Driver.py"
"""
if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print "Error in data directory input"
        sys.exit(0)
    main(sys.argv[1])