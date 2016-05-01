#-*- coding: utf-8 -*-
from collections import defaultdict, Counter
from os.path import dirname, realpath
from os import listdir
import os

# unfortunately, because have a small source base for Kurmanci, need to make sure doesn't used punctuation
excludes = [u":", u"“", u"…", u"”", u"?", u"'", u'"', u"_", u"!", u"\n", u"(", u")", u"/", u"\\", u"$", u"&", u",", u"-", u"+", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] + range(10) + [u"ـ", u"٠", u"@", u";", u"’", u"%", u"®", u"©"] + [unichr(1632+n) for n in range(10)] + [unichr(1632+n).encode("utf-8") for n in range(10)] + ["h", "J"]


directory = dirname(realpath(__file__))
d = {}
directory_of_sources = directory + "/sources"
filenames = listdir(directory_of_sources)
languages = [f for f in filenames if not f.startswith("_")]
all_text = ""
for language in languages:

    directory_of_language = directory_of_sources + "/" + language

    language_text = ""
    for name_of_file in sorted(listdir(directory_of_language))[:5]:
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
all_char_score = []
number = 10
for language in languages:

    language_char_score = []
    for char, frequency in d[language].iteritems():
        score = frequency / (all_char_frequency[char])
        if char not in excludes:
            language_char_score.append((char, score))
    language_char_score = sorted(language_char_score, key = lambda e: -1*e[1])[:number]
    for char, score in language_char_score:
        all_char_score.append((char, score, language))
all_char_score = sorted(all_char_score, key = lambda cs: -1*cs[1])

for char, score, language in all_char_score:
    text_to_write += "\n" + char.encode("utf-8").strip() + "\t" + language

with open(directory + "/char_language.txt", "wb") as f:
    f.write(text_to_write.strip())
