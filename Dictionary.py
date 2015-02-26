# -*- coding: utf-8 -*-
import sys
import os
import re
import collections
import urllib2
import snowballstemmer
from sets import Set

class Dictionary:
    
    """
    English Dictionaries:
    bigram dictionary is structured as: bigram - count, part of speech
    word1 word2 : [count, [part of speech tag word 1, part of speech tag word 2]]

    trigram dictionary is structured as: trigram - count, part of speech
    word1 word2 word3 : [count, [pos tag word1, pos tag word2, pos tag word3]

    four-gram dictionary follows same pattern

    five-gram dictionary follows same pattern

    Spanish-English dictionary:
    uses http request to call translation function from Google translate
    parses results and stores translation and part of speech pairs (English-Spanish)
    """



    def __init__(self):
        """
        Initialize the dictionaries to use for translation:
        1) English bigram, trigram, four-gram, and five-gram (Corpus of Contemporary American English)
        2) Custom bigram, trigram dictionary built from any English text of sentences
        3) Spanish-English word to word/phrase translator (Google Translate and WordReference)
        """
        
        """
        1) CCAE Dictionaries
        """
        self.english_bigram_dict = collections.defaultdict(lambda:[])
        self.english_bigram_dict_unigram_dict = collections.defaultdict(lambda:0)
        self.english_trigram_dict = collections.defaultdict(lambda:[])
        self.english_trigram_dict_unigram_dict = collections.defaultdict(lambda:0)
        self.english_fourgram_dict = collections.defaultdict(lambda:[])
        self.english_fourgram_dict_unigram_dict = collections.defaultdict(lambda:0)
        self.english_fivegram_dict = collections.defaultdict(lambda:[])
        self.english_fivegram_dict_unigram_dict = collections.defaultdict(lambda:0)

        """
        2) Custom bigram/trigram dictionaries (in English)
        """
        self.custom_bigram_dict = collections.defaultdict(lambda:0)
        self.custom_bigram_dict_unigram_dict = collections.defaultdict(lambda:0)
        self.custom_trigram_dict = collections.defaultdict(lambda:0)
        self.custom_trigram_dict_unigram_dict = collections.defaultdict(lambda:0)

        """
        Extra dictionary, we will probably not use this one
        """
        self.spanish_dict = collections.defaultdict(lambda:[])
        
        """
        3) Spanish-English dictionary (corpus of 15 sentences)
           Built using Google Translate and Word Reference
        """
        self.custom_dict = collections.defaultdict(lambda:[])

    
    """
    Description: Read in bigrams, trigrams, four-grams, and five-grams from
    Corpus of Contemporary American English for English n-gram language model

    Evaluation: Will likely use for fluency ranking in post-processing
    """

    def build_english_bigrams(self, filename, dir_name):
        path = os.path.join(dir_name, filename)
        file_stream = open(path, 'r')
        #in bigram file
        for line in file_stream:
            
            line = line.replace("\r", "")
            line = line.replace("\n", "")
            indexed_line = re.split("[\t]", line)

            bigram = indexed_line[1].lower() + " " + indexed_line[2].lower()
            info_list = []
            count = indexed_line[0]
            pos_tag = [indexed_line[3], indexed_line[4]]
            info_list.append(count)
            info_list.append(pos_tag)

            self.english_bigram_dict[bigram] = info_list

            self.english_bigram_dict_unigram_dict[indexed_line[1].lower()] += 1
            self.english_bigram_dict_unigram_dict[indexed_line[2].lower()] += 1


    def build_english_trigrams(self, filename, dir_name):
        path = os.path.join(dir_name, filename)
        file_stream = open(path, 'r')
        #in trigram file
        for line in file_stream:
            
            line = line.replace("\r", "")
            line = line.replace("\n", "")
            indexed_line = re.split("[\t]", line)

            trigram = indexed_line[1].lower() + " " + indexed_line[2].lower() + " " + indexed_line[3].lower()
            info_list = []
            count = indexed_line[0]
            pos_tag = [indexed_line[4], indexed_line[5], indexed_line[6]]
            info_list.append(count)
            info_list.append(pos_tag)

            self.english_trigram_dict[trigram] = info_list
            self.english_trigram_dict_unigram_dict[indexed_line[1].lower()] += 1
            self.english_trigram_dict_unigram_dict[indexed_line[2].lower()] += 1
            self.english_trigram_dict_unigram_dict[indexed_line[3].lower()] += 1

        

    def build_english_fourgrams(self, filename, dir_name):
        path = os.path.join(dir_name, filename)
        file_stream = open(path, 'r')
        #in trigram file
        for line in file_stream:
            
            line = line.replace("\r", "")
            line = line.replace("\n", "")
            indexed_line = re.split("[\t]", line)

            fourgram = indexed_line[1].lower() + " " + indexed_line[2].lower() + " " + indexed_line[3].lower() + " " + indexed_line[4].lower()
            info_list = []
            count = indexed_line[0]
            pos_tag = [indexed_line[5], indexed_line[6], indexed_line[7], indexed_line[8]]
            info_list.append(count)
            info_list.append(pos_tag)

            self.english_fourgram_dict[fourgram] = info_list

            self.english_fourgram_dict_unigram_dict[indexed_line[1].lower()] += 1
            self.english_fourgram_dict_unigram_dict[indexed_line[2].lower()] += 1
            self.english_fourgram_dict_unigram_dict[indexed_line[3].lower()] += 1
            self.english_fourgram_dict_unigram_dict[indexed_line[4].lower()] += 1


    def build_english_fivegrams(self, filename, dir_name):
        path = os.path.join(dir_name, filename)
        file_stream = open(path, 'r')

        #in trigram file
        for line in file_stream:
            
            line = line.replace("\r", "")
            line = line.replace("\n", "")
            indexed_line = re.split("[\t]", line)

            fivegram = indexed_line[1].lower() + " " + indexed_line[2].lower() + " " + indexed_line[3].lower() + " " + indexed_line[4].lower() + " " + indexed_line[5].lower()
            info_list = []
            count = indexed_line[0]
            pos_tag = [indexed_line[6], indexed_line[7], indexed_line[8], indexed_line[9], indexed_line[10]]
            info_list.append(count)
            info_list.append(pos_tag)

            self.english_fivegram_dict[fivegram] = info_list

            self.english_fivegram_dict_unigram_dict[indexed_line[1].lower()] += 1
            self.english_fivegram_dict_unigram_dict[indexed_line[2].lower()] += 1
            self.english_fivegram_dict_unigram_dict[indexed_line[3].lower()] += 1
            self.english_fivegram_dict_unigram_dict[indexed_line[4].lower()] += 1
            self.english_fivegram_dict_unigram_dict[indexed_line[5].lower()] += 1


        
    """
    Description: Reads from any English corpus delimited by sentences. Extracts bigrams and trigrams
    Evaluation: Runs slowly for large corpus. May use for fluency ranking in post-processing
    """
    
    def build_english_corpus(self, filename, dir_name):
        path = os.path.join(dir_name, filename)
        file_stream = open(path, 'r')

        sentence_word_list = []
        sentences = []
        for line in file_stream:
            # print line
            line = line.replace(",", "")
            line = line.replace(";", "")
            line = line.replace("(", "")
            line = line.replace(")", "")
            line = line.replace(":", "")
            line = line.replace("!", "")
            line = line.replace("?", "")
            line = line.replace("\n", "")
            line = line.replace("\"", "")

            #assumption: abbreviations are relatively rare, so just ignore them and their ".", e.g. "Mr."
            line = re.sub(" [A-Z][a-z0-9]*?\.", "", line)
            sentences_in_line = re.split("\.", line)


            for sentence in sentences_in_line:
                # print sentence
                # print "#"
                sentences.append(sentence)

        for sentence in sentences:
            # print sentence
            # print "#"
            if re.findall("[A-Za-z0-9]", sentence):
                sentence_word_list_temp = re.split(" ", sentence)
                sentence_word_list = []
                for word in sentence_word_list_temp:
                    if re.findall("[A-Za-z0-9]", word):
                        sentence_word_list.append(word.lower())

                #make bigram dictionary of custom corpus
                if len(sentence_word_list) >= 2:
                    self.build_english_corpus_bigram_helper(sentence_word_list)
                #make trigram dictionary of custom corpus
                if len(sentence_word_list) >= 3:
                    self.build_english_corpus_trigram_helper(sentence_word_list)


    """
    Helper functions for build_english_corpus, to extract bigrams and trigrams
    """
    def build_english_corpus_bigram_helper(self, sentence_word_list):
        
        for i in xrange(0, len(sentence_word_list)-1):
            word1 = sentence_word_list[i]
            word2 = sentence_word_list[i+1]
            bigram = word1 + " " + word2
            self.custom_bigram_dict[bigram] = self.custom_bigram_dict[bigram] + 1
                        
            self.custom_bigram_dict_unigram_dict[word1]

        bigram1 = "-" + " " + sentence_word_list[0]
        bigram2 = sentence_word_list[len(sentence_word_list)-1] + " " + "-"
                    
        self.custom_bigram_dict[bigram1] = self.custom_bigram_dict[bigram1] + 1
        self.custom_bigram_dict[bigram2] = self.custom_bigram_dict[bigram2] + 1

        self.custom_bigram_dict_unigram_dict[len(sentence_word_list)-1]


    def build_english_corpus_trigram_helper(self, sentence_word_list):
        
        for i in xrange(0, len(sentence_word_list)-2):
            word1 = sentence_word_list[i]
            word2 = sentence_word_list[i+1]
            word3 = sentence_word_list[i+2]
            trigram = word1 + " " + word2 + " " + word3
            self.custom_trigram_dict[trigram] = self.custom_trigram_dict[trigram] + 1
            self.custom_trigram_dict_unigram_dict[word1]
                        

        trigram1 = "-" + " " + "-" + " " + sentence_word_list[0]
        trigram2 = "-" + " " + sentence_word_list[0] + " " + sentence_word_list[1]
        trigram3 = sentence_word_list[len(sentence_word_list)-2] + " " + sentence_word_list[len(sentence_word_list)-1] + " " + "-"
        trigram4 = sentence_word_list[len(sentence_word_list)-1] + " " + "-" + " " + "-"

        self.custom_trigram_dict[trigram1] = self.custom_trigram_dict[trigram1] + 1
        self.custom_trigram_dict[trigram2] = self.custom_trigram_dict[trigram2] + 1
        self.custom_trigram_dict[trigram3] = self.custom_trigram_dict[trigram3] + 1
        self.custom_trigram_dict[trigram4] = self.custom_trigram_dict[trigram4] + 1

        self.custom_trigram_dict_unigram_dict[len(sentence_word_list)-2]
        self.custom_trigram_dict_unigram_dict[len(sentence_word_list)-1]


    """
    Description: General Spanish-English dictionary before adding particular words from corpus
    Evaluation: Probably will not need this function for the project, just an extra

    Needs custom files to read in data
    """
    
    def build_bilingual_dictionary(self, filename_list, dir_name):
        #in 4K Spanish-English bilingual list
        path = os.path.join(dir_name, filename_list[0])
        file_stream = open(path, 'r')
        line_stream = []
        for line in file_stream:
            if not re.findall("[A-Za-z0-9]", line):
                continue
            else:
                line_stream.append(line)

        for i in xrange(0, len(line_stream)-2,2):
            clean_english_line = line_stream[i]
            clean_english_line = re.sub("\(.*?\)", "", clean_english_line)
            clean_english_line = clean_english_line.replace(" \n","")
            clean_english_line = clean_english_line.replace("\n","")
            # if re.findall(".*?[a-z] [^A-Za-z]", clean_english_line):
                # clean_english_line = clean_english_line.replace(" ", "")
            # print clean_english_line

            clean_spanish_line = line_stream[i+1].replace(".", ",")
            clean_spanish_line = clean_spanish_line.replace("\n", "")
            clean_spanish_line = re.sub("\(.*?\)", "", clean_spanish_line)
            clean_spanish_line = clean_spanish_line.replace("--","")
            clean_spanish_line = re.sub(", ", ",", clean_spanish_line)
            # print clean_spanish_line

            english_word_list = []
            english_word_list.append(clean_english_line)

            spanish_word_many = clean_spanish_line
            spanish_word_list = re.split(",", spanish_word_many)
            # print spanish_word_list

            for word in spanish_word_list:
                if re.findall("[A-Za-z]", word):
                    self.spanish_dict[word] = english_word_list


        #in categorical 1K Spanish-English bilingual list
        path = os.path.join(dir_name, filename_list[1])
        file_stream = open(path, 'r')
        line_stream = []
        for line in file_stream:
            if not re.findall("[A-Za-z0-9]", line):
                continue
            else:
                # print line

                line_in = line.replace("\n", "")
                split_english_spanish = line_in.split("\t")
                # print split_list
                spanish_word = split_english_spanish[0]
                english_list = split_english_spanish[1].split(", ")

                if "/" in spanish_word:
                    split_spanish_word = spanish_word.split(" ")
                    spanish_word_masc = "el " + split_spanish_word[1]
                    spanish_word_fem = "la " + split_spanish_word[1]

                    dict_word_list_masc = self.spanish_dict[spanish_word_masc]
                    # print dict_word_list

                    #masculine words
                    for eng_word in english_list:
                        if eng_word in dict_word_list:
                            continue
                        elif eng_word != "" and eng_word != None:
                            dict_word_list_masc.append(eng_word)

                    self.spanish_dict[spanish_word_masc] = dict_word_list_masc

                    #feminine words
                    dict_word_list_fem = self.spanish_dict[spanish_word_fem]
                    for eng_word in english_list:
                        if eng_word in dict_word_list:
                            continue
                        elif eng_word != "" and eng_word != None:
                            dict_word_list_fem.append(eng_word)

                    self.spanish_dict[spanish_word_fem] = dict_word_list_fem

                else:
                    dict_word_list = self.spanish_dict[spanish_word]
                    # print dict_word_list

                    for eng_word in english_list:
                        if eng_word in dict_word_list:
                            continue
                        elif eng_word != "" and eng_word != None:
                            dict_word_list.append(eng_word)

                    self.spanish_dict[spanish_word] = dict_word_list


    """
    Build custom dictionary from working corpus based on novel.
    Tried Google Translate for automated translsation, but API only gives one translation per word
    So this cusotm dictionary is partially hand-built, doing Spanish word search on Google Translate and WordReference

    Custom Spanish dictionary maps:
    key: Spanish word (stemmed)
    list: [[word1, part of speech1], [word2, part of speech2], ... , [wordn, part of speechn]]
    """

    def build_custom_dictionary(self, filename, dir_name, google_translate_file):
        # word = "verde"
        # page = urllib2.urlopen("https://translate.google.com/#es/en").read()
        # print page
        #es/en/verde

        spanish_stemmer = snowballstemmer.stemmer('spanish');

        path = os.path.join(dir_name, filename)
        file_stream = open(path, 'r')
        exact_spanish_words = Set()

        for sentence in file_stream:
            if re.findall("[A-Za-z0-9]", sentence):
                sentence = sentence.replace("!", "")
                sentence = sentence.replace(".", "")
                sentence = sentence.replace(",", "")
                sentence = sentence.replace(";", "")
                sentence = sentence.replace("(", "")
                sentence = sentence.replace(")", "")
                sentence = sentence.replace(":", "")
                sentence = sentence.replace("?", "")
                sentence = sentence.replace("\n", "")
                sentence = sentence.replace("\"", "")
                sentence = sentence.lower()

                sentence_word_list_temp = re.split(" ", sentence)
                sentence_word_list = []

                for word in sentence_word_list_temp:
                    if re.findall("[A-Za-z0-9]", word):
                        sentence_word_list.append(word)

                for word in sentence_word_list:
                #     self.custom_dict[word] = []
                    exact_spanish_words.add(word)

        path = os.path.join(dir_name, google_translate_file)
        file_stream = open(path, 'r')
        spanish_word = ""
        word_type = ""
        translation_list = []
        even_odd_line = 0

        for sentence in file_stream:
            if "Translations" in sentence:
                word_list = re.split(" ", sentence)
                spanish_word = word_list[2]
                spanish_word = spanish_word.replace("\n", "")
                translation_list = []
            elif "pronoun\n" in sentence:
                word_type = "pronoun"
                even_odd_line = 1
            elif "adjective\n" in sentence:
                word_type = "adjective"
                even_odd_line = 1
            elif "adverb\n" in sentence:
                word_type = "adverb"
                even_odd_line = 1
            elif "preposition\n" in sentence:
                word_type = "preposition"
                even_odd_line = 1
            elif "abbreviation\n" in sentence:
                word_type = "abbreviation"
                even_odd_line = 1
            elif "noun\n" in sentence:
                word_type = "noun"
                even_odd_line = 1
            elif "article\n" in sentence:
                word_type = "article"
                even_odd_line = 1
            elif "verb\n" in sentence:
                word_type = "verb"
                even_odd_line = 1
            elif "conjunction\n" in sentence:
                word_type = "conjunction"
                even_odd_line = 1
            elif "prefix\n" in sentence:
                word_type = "prefix"
                even_odd_line = 1


            elif even_odd_line%2 == 0 and "Translations" not in sentence and "prefix\n" not in sentence and "conjunction\n" not in sentence and "verb\b" not in sentence and "pronoun\n" not in sentence and "article\n" not in sentence and "abbreviation\n" not in sentence and "noun\n" not in sentence and "adjective\n" not in sentence and "adverb\n" not in sentence and "preposition\n" not in sentence:
                translation = sentence
                translation = translation.replace("\n", "")
                translation_list.append([translation, word_type])
                self.custom_dict[spanish_word] = translation_list

            even_odd_line += 1
            # print sentence

        self.build_custom_dictionary_manual()

        return list(exact_spanish_words)

    """
    Custom Entry for sparse Translations
    """
    def build_custom_dictionary_manual(self):
        self.custom_dict["Úrsula"] = [["Úrsula", "noun"]]
        self.custom_dict["aureliano"] = [["Aureliano", "noun"]]
        self.custom_dict["quienes"] = [["who", "pronoun"], ["nobody", "pronoun"]]
        self.custom_dict["otro"] = [["other", "adjective"], ["another", "adjective"], ["one more", "adjective"], ["a second", "adjective"], ["next", "adjective"], ["following", "adjective"]]
        self.custom_dict["pulido"] = [["polished", "adjective"], ["well-polished", "adjective"], ["refined", "adjective"], ["polishing", "noun"]]
        self.custom_dict["soldado"] = [["soldier", "noun"]]
        self.custom_dict["fláccido"] = [["flaccid", "adjective"], ["flabby", "adjective"]]
        self.custom_dict["buendía"] = [["Buendía", "noun"]]
        self.custom_dict["encías"] = [["gum", "noun"]]
        # self.custom_dict["gitano"] = [["gypsy", "noun"], ["gypsy", "adjective"], ["conniver", "noun"], ["trickster", "noun"]]
        self.custom_dict["asombroso"] = [["astonishing", "adjective"], ["amazing", "noun"]]
        self.custom_dict["bicloruro"] = [["bichloride", " noun"]]
        self.custom_dict["piedra"] = [["stone", "noun"], ["rock", "noun"], ["hailstone", "noun"], ["hail", "noun"]]
        self.custom_dict["imantar"] = [["magnetize", "verb"]]
        self.custom_dict["imantados"] = [["magnetized", "adjective"]]
        self.custom_dict["josé"] = [["José", "noun"]]
        self.custom_dict["haber"] = [["be", "verb"], ["there is", "verb"], ["there are", "verb"]]
        self.custom_dict["arcadio"] = [["Arcadio", "noun"]]
        self.custom_dict["cascote"] = [["piece of rubble", "noun"], ["rubble", "noun"]]
        self.custom_dict["marchitos"] = [["withered", "adjective"], ["shriveled", "adjective"], ["faded", "adjective"], ["wizened", "adjective"]]
        self.custom_dict["calabazo"] = [["calabazo", "unknown"]]
        self.custom_dict["iguarán"] = [["Iguarán", "noun"]]
        self.custom_dict["enemigo"] = [["enemy", "noun"], ["opponent", "noun"], ["adversary", "noun"], ["enemy forces", "noun"], ["enemy", "adjective"], ["opposing", "adjective"]]
        self.custom_dict["xv"] = [["XV", "abbreviation"]]
        self.custom_dict["cotidiano"] = [["daily", "adjective"], ["quotidian", "adjective"], ["everyday", "adjective"], ["routine", "adjective"]]
        self.custom_dict["aguas"] = [["waters", "noun"]]
        self.custom_dict["cuánto"] = [["how many", "pronoun"], ["how much", "pronoun"], ["how long", "pronoun"], ["what a lot of", "unknown"], ["so many", "unknown"], ["how many", "adjective"]]
        self.custom_dict["disuadir"] = [["dissuade", "verb"]]
        self.custom_dict["melquíades"] = [["Melquíades", "noun"]]
        self.custom_dict["del"] = [["from the", "preposition"], ["of the", "preposition"]]
        self.custom_dict["minúsculo"] = [["tiny", "adjective"], ["minor", "adjective"], ["trivial", "adjective"]]
        self.custom_dict["inmenso"] = [["immense", "adjective"], ["great", "adjective"], ["enormous", "adjective"], ["huge", "adjective"], ["gigantic", "adjective"], ["humungous", "adjective"], ["obese", "adjective"]]
        self.custom_dict["desmedrado"] = [["impaired", "adjective"], ["reduced", "adjectie"], ["puny", "adjective"], ["feeble", "adjective"]]
        self.custom_dict["gigantesco"] = [["gigantic", "adjective"]]
        self.custom_dict["cañabrava"] = [["reed", "unknown"]]
        self.custom_dict["seca"] = [["dry", "adjective"]]
        self.custom_dict["animal"] = [["animal", "noun"], ["beast", "noun"], ["brute", "noun"], ["violent", "adjective"], ["wild", "adjective"], ["crazy", "adjective"], ["lunatic", "noun"]]
        self.custom_dict["macondo"] = [["Macondo", "noun"]]
        self.custom_dict["a la"] = [["on the", "preposition"]]




