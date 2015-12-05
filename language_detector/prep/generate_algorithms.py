from collections import defaultdict, Counter
from os.path import dirname, realpath
from os import listdir
import os

directory = dirname(realpath(__file__))
print "directory is", directory
d = {}
directory_of_sources = directory + "/sources"
languages = listdir(directory_of_sources)
all_text = ""
for language in languages:
    print language

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

with open("language_chars.txt", "wb") as f:
    for language in languages:
        print "for language ", language
        char_score = []
        for char, frequency in d[language].iteritems():
            char_score.append((char, frequency / all_char_frequency[char]))
        char_score = sorted(char_score, key = lambda e: -1*e[1])[:30]
        print "char_score most common are", char_score[0], d[language][char]
        f.write("\n" + language + "\t")
        for char, score in char_score:
            f.write("\t" + char.encode("utf-8"))
