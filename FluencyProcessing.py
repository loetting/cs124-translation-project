# -*- coding: utf-8 -*-
from Dictionary import Dictionary
import collections
import math
import sys
import re

class FluencyProcessing:

    def __init__(self):
        print ""
    
    """
    Takes in a list of English sentences and finds the most fluent sentence.
    Important note: bigram_dict parameter can be from CCAE bigram dictionary or custom built bigram dictionary
                    bigram_dict_unigram_dict is the unigram dictionary of all words in the bigram dictionary
                    ccae_flag is to tell this function whether reading from CCAE bigram dictionary or custom bigram dictionary
    """
    def find_fluent_translation_stupidbackoff(self, english_sentences, bigram_dict, bigram_dict_unigram_dict, ccae_flag):
        #starts with bigrams and does stupid backoff if needed
        index = 0
        max_prob = float("-inf")
        max_index = 0
        bigram_prob_list = []

        for sentence in english_sentences:
            # print sentence
            sentence = sentence.replace(",", "")
            sentence = sentence.replace(";", "")
            sentence = sentence.replace("(", "")
            sentence = sentence.replace(")", "")
            sentence = sentence.replace(":", "")
            sentence = sentence.replace("!", "")
            sentence = sentence.replace("\n", "")
            sentence = sentence.replace("\"", "")

            if re.findall("[A-Za-z0-9]", sentence):
                sentence_word_list_temp = re.split(" ", sentence)
                sentence_word_list = []
                for word in sentence_word_list_temp:
                    if re.findall("[A-Za-z0-9]", word):
                        sentence_word_list.append(word)

                if len(sentence_word_list) >= 2:
                    prob_log_sum = 0
                    for i in xrange(0, len(sentence_word_list)-1):
                        word1 = sentence_word_list[i]
                        word2 = sentence_word_list[i+1]
                        bigram = word1 + " " + word2
                        
                        if ccae_flag == True:
                            bigram_list = bigram_dict[bigram]

                            if len(bigram_list) > 0:
                                numer = int(bigram_list[0])
                            else:
                                numer = 0

                            denom = bigram_dict_unigram_dict[word1] + len(bigram_dict_unigram_dict)

                        elif ccae_flag == False:
                            numer = bigram_dict[bigram]
                            denom = bigram_dict_unigram_dict[word1] + len(bigram_dict_unigram_dict)

                        prob = float(numer)/float(denom)
                        # print numer
                        # print denom

                        if prob == 0:
                            numer = bigram_dict_unigram_dict[word2] + 1
                            denom = len(bigram_dict_unigram_dict)
                            prob = float(numer)/float(denom)

                        log_prob = math.log(prob)
                        prob_log_sum += log_prob

                    #take care of edge cases for the bigram beginning and end of sentence
                    bigram1 = "-" + " " + sentence_word_list[0]
                    bigram2 = sentence_word_list[len(sentence_word_list)-1] + " " + "-"
                    bigram_edge = []
                    bigram_edge.append(bigram1)
                    bigram_edge.append(bigram2)

                    if ccae_flag == False:

                        for bigram in bigram_edge:
                            split_bigram = re.split(" ", bigram)
                            numer = bigram_dict[bigram]
                            denom = bigram_dict_unigram_dict[split_bigram[0]] + len(bigram_dict_unigram_dict)


                            prob = float(numer)/float(denom)
                            # print numer
                            # print denom

                            if prob == 0:
                                numer = bigram_dict_unigram_dict[word2] + 1
                                denom = len(bigram_dict_unigram_dict)
                                prob = float(numer)/float(denom)

                            log_prob = math.log(prob)
                            prob_log_sum += log_prob

                    if prob_log_sum > max_prob:
                        max_prob = prob_log_sum
                        max_index = index

                    # print " "
                    # print prob_log_sum
                    # print max_prob
                    # print " "

                    bigram_prob_list.append(prob_log_sum)

                index += 1

        # return english_sentences[max_index]
        return bigram_prob_list


    """
    Function finds the trigram probability score using Laplace smoothing and the bigram dictionary.
    Can take CCAE dictionaries or custom dictionaries, but both trigram and bigram dictionaries must be
    either CCAE or custom.
    """
    def find_fluent_translation_trigrams(self, english_sentences, trigram_dict, trigram_dict_unigram_dict, ccae_flag, bigram_dict, bigram_dict_unigram_dict):
        index = 0
        max_prob = float("-inf")
        max_index = 0
        trigram_prob_list = []

        for sentence in english_sentences:
            # print sentence
            sentence = sentence.replace(",", "")
            sentence = sentence.replace(";", "")
            sentence = sentence.replace("(", "")
            sentence = sentence.replace(")", "")
            sentence = sentence.replace(":", "")
            sentence = sentence.replace("!", "")
            sentence = sentence.replace("\n", "")
            sentence = sentence.replace("\"", "")

            if re.findall("[A-Za-z0-9]", sentence):
                sentence_word_list_temp = re.split(" ", sentence)
                sentence_word_list = []
                for word in sentence_word_list_temp:
                    if re.findall("[A-Za-z0-9]", word):
                        sentence_word_list.append(word)

                if len(sentence_word_list) >= 3:
                    prob_log_sum = 0
                    for i in xrange(0, len(sentence_word_list)-2):
                        word1 = sentence_word_list[i]
                        word2 = sentence_word_list[i+1]
                        word3 = sentence_word_list[i+2]
                        trigram = word1 + " " + word2 + " " + word3
                        bigram = word1 + " " + word2
                            
                        if ccae_flag == True:
                            trigram_list = trigram_dict[trigram]
                            if len(trigram_list) > 0:
                                numer = int(trigram_list[0]) + 1
                            else:
                                numer = 1

                            bigram_list = bigram_dict[bigram]
                            if len(bigram_list) > 0:
                                denom = int(bigram_list[0]) + len(bigram_dict_unigram_dict)
                            else:
                                denom = len(bigram_dict_unigram_dict)
                            
                        elif ccae_flag == False:
                            numer = trigram_dict[trigram] + 1
                        
                            denom = bigram_dict[word1 + " " + word2] + len(bigram_dict_unigram_dict)

                        prob = float(numer)/float(denom)

                        prob_log_sum += math.log(prob)
    

                    if ccae_flag == False:
                        trigram1 = "-" + " " + "-" + " " + sentence_word_list[0]
                        trigram2 = "-" + " " + sentence_word_list[0] + " " + sentence_word_list[1]
                        trigram3 = sentence_word_list[len(sentence_word_list)-2] + " " + sentence_word_list[len(sentence_word_list)-1] + " " + "-"
                        trigram4 = sentence_word_list[len(sentence_word_list)-1] + " " + "-" + " " + "-"

                        trigram_edge = []
                        trigram_edge.append(trigram1)
                        trigram_edge.append(trigram2)
                        trigram_edge.append(trigram3)
                        trigram_edge.append(trigram4)

                        for trigram in trigram_edge:
                            numer = trigram_dict[trigram] + 1
                            trigram_split = re.split(" ", trigram)
                            bigram = trigram_split[0] + " " + trigram_split[1]
                            denom = bigram_dict[bigram] + len(bigram_dict_unigram_dict)

                            prob = float(numer)/float(denom)
                            prob_log_sum += math.log(prob)
                    
                    trigram_prob_list.append(prob_log_sum)

        return trigram_prob_list

    """
    Function combines scores from bigram with stupid backoff and trigram with Laplace smoothing for an overall score
    Combines probability score for each English sentence: bigram with stupid backoff and for trigram with Laplace smoothing.
    """
    def find_combined_fluency(self, english_sentences, bigram_prob_list, trigram_prob_list):
        max_score = float("-inf")
        max_index = 0

        for i in xrange(0, len(english_sentences)):
            print english_sentences[i]

            bigram_score = bigram_prob_list[i]
            trigram_score = trigram_prob_list[i]

            print bigram_score
            print trigram_score

            combined_score = bigram_score + trigram_score
            print combined_score

            if combined_score > max_score:
                max_score = combined_score
                max_index = i

        combined_fluent_sentence = english_sentences[max_index]
        return combined_fluent_sentence


                    
                    
