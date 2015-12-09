from os.path import dirname, realpath
directory = dirname(realpath(__file__))

char_language = []
with open(directory + "/prep/char_language.txt") as f:
    for line in f:
        if line:
            char_language.append(line.decode("utf-8").strip().split(u"\t"))

def detect_language(text):
    if isinstance(text, str):
        text = text.decode("utf-8")

    for char, language in char_language:
        if char in text:
            return language
