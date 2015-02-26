import re
import collections


class StemHelper:
    """
    Stemming helper to find the dictionary entry that best matches our Spanish word
    """

    def find_dictionary_match(self, spanish_word, dict_inst):
        word_to_match = ""
        matching_dict_entries = []
        custom_dict = dict_inst.custom_dict

        dict_word_list = []

        if spanish_word in custom_dict:
            return spanish_word

        for word in custom_dict:
            if len(custom_dict[word]) > 0:
                dict_word_list.append(word)
        
        if len(spanish_word) > 2:
            for i in xrange(0, len(spanish_word)):
                word_to_match += spanish_word[i]
                for word in dict_word_list:
                    if word.startswith(word_to_match) and i > 1:
                        matching_dict_entries.append(word)

            length_match_dict = len(matching_dict_entries)
            
            if length_match_dict > 0:
                max_length = 0
                for word in matching_dict_entries:
                    if len(word) > max_length:
                        maximal_match = word

            else:
                maximal_match = "None"
        
        elif len(spanish_word) <= 2:
            maximal_match = spanish_word

        return maximal_match

            


        
