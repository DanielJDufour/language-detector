from os.path import dirname, realpath
from collections import Counter

directory = dirname(realpath(__file__))

char_language = []
with open(directory + "/prep/char_language.txt") as f:
    for line in f:
        if line:
            char_language.append(line.decode("utf-8").strip().split(u"\t"))

def detect_language_text(text):
    if isinstance(text, str):
        text = text.decode("utf-8")

    for char, language in char_language:
        if char in text:
            return language

# just returns the most common language of an iterable of string values
# an example of this can be a list of names
def detect_language_iterable(iterable):
    # may be able to speed this up with out using counter
    # hmmm nvm.. it's so freaking quick anyway, that probably don't worry about this now
    counter = Counter([detect_language(iteration) for iteration in iterable])
    most_common_language = counter.most_common(1)[0][0] or counter.most_common(2)[1][0]
    return most_common_language

def detect_language(inpt):
    if isinstance(inpt, str) or isinstance(inpt, unicode):
        return detect_language_text(inpt)
    elif isinstance(inpt, set) or isinstance(inpt, list):
        return detect_language_iterable(inpt)
