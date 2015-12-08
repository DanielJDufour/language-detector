from os.path import dirname, realpath
directory = dirname(realpath(__file__))

language_chars = {}
with open(directory + "/prep/language_chars.txt") as f:
    for line in f:
        if line:
            items = line.strip().split("\t")
            language = items[0]
            if language:
                language_chars[language] = [char.decode("utf-8") for char in items[1:] if char]

def detect_language(text):
    if isinstance(text, str):
        text = text.decode("utf-8")

    for n in range(1,5):
        number_of_uniques = n * 5
        for char in text:
            for i in range(number_of_uniques):
                for language, chars in language_chars.iteritems():
                    char_to_compare = chars[i]
                    if char == chars[i]:
                        return language
dl = detect_language
