#-*- coding: utf-8 -*-
from collections import defaultdict, Counter
from os.path import dirname, realpath
from os import listdir
import os

# unfortunately, because have a small source base for Kurmanci, need to make sure doesn't used punctuation
excludes = [u"“", u"…", u"”", u"?", u"'", u'"', u"_", u"!", u"\n"] 

directory = dirname(realpath(__file__))
d = {}
directory_of_sources = directory + "/sources"
filenames = listdir(directory_of_sources)
languages = [f for f in filenames if not f.startswith("_")]
all_text = ""
for language in languages:

    directory_of_language = directory_of_sources + "/" + language

    language_text = ""
    for name_of_file in listdir(directory_of_language):
        path_to_file = directory_of_language + "/" + name_of_file
        with open(path_to_file) as f:
            text = f.read().decode("utf-8")
            language_text += text
            all_text += text
    
    number_of_chars = len(language_text)
    language_char_frequency = {}
    for char, count in Counter(language_text).iteritems():
        language_char_frequency[char] = float(count) / float(number_of_chars)
   
    d[language] = language_char_frequency

all_char_frequency = {}
number_of_chars = len(all_text)
for char, count in Counter(all_text).iteritems():
    all_char_frequency[char] = float(count) / float(number_of_chars)

text_to_write = ""
for language in languages:
    char_score = []
    for char, frequency in d[language].iteritems():
        char_score.append((char, frequency / (2*all_char_frequency[char])))
    char_score = sorted(char_score, key = lambda e: -1*e[1])[:50]
    char_score = [(char, score) for char, score in char_score if char not in excludes][:30]
    text_to_write += "\n" + language + "\t"
    for char, score in char_score:
        text_to_write += "\t" + char.encode("utf-8").strip()

with open("language_chars.txt", "wb") as f:
    f.write(text_to_write.strip())
