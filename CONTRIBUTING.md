# Contributing
If you'd like to add another language, read on!

# How does it work?
Language Detector works by looking for characters that are nearly unique to a language's script.  For example, if we see `ß` in some text, the language is likely German because we almost never see this character in other languages.

# How to add another language?
1) Create a folder with the Language's Name in title-case in [./prep/sources](https://github.com/DanielJDufour/language-detector/tree/master/language_detector/prep/sources)
2) Add in at least five files of text in the new language in .txt format. For an example, see [Kurmanci](https://github.com/DanielJDufour/language-detector/tree/master/language_detector/prep/sources/Kurmanci).  Newspapers are great sources!
3) Add the Language and its corresponding code to [language_to_code in __init__.py](https://github.com/DanielJDufour/language-detector/blob/master/language_detector/__init__.py#L9)
3) Add a test for detecting the new language to [./test/test.py](https://github.com/DanielJDufour/language-detector/blob/master/language_detector/tests/test.py)
5) Make a Pull Request with changes to the master branch (the default)

# Questions
Reach out with questions to Daniel J. Dufour at daniel.j.dufour@gmail.com
