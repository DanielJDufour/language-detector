[![Build Status](https://travis-ci.org/DanielJDufour/language-detector.svg?branch=master)](https://travis-ci.org/DanielJDufour/language-detector)

# language-detector
language-detector detects the language of text

# Installation
```
pip install language-detector
```

# Python Version
Works with both Python 2 and 3

# Use
```
from language_detector import detect_language
text = "I arrived in that city on January 4, 1937"
language = detect_language(text)
# prints English
```

# Features
| Languages Supported |
| ------------------- |
| Arabic |
| English |
| Farsi |
| French |
| German |
| Khmer |
| Kurmanci (Kurdish) |
| Mandarin |
| Russian |
| Sorani (Kurdish) |
| Spanish |
| Turkish |

# Testing
To test the package run
```
python -m unittest language_detector.tests.test
```

# Comparison
Test is a comparison of how well language-detector and langid identify languages in the [data sources](language_detector/prep/sources). 
 
| package | language-detector | langid |
| ------- | ----------------- | ------ |
| test-duration (in seconds)| 0.10 | 3.83 |
| accuracy | 96.77% | 67.74% |


# Excluding Languages
If you don't want language-detector to look for certain languages, you can monkey-patch the code.  For example, in order to exclude English:
```
import language_detector
language_detector.char_language = [cl for cl in char_language if cl[1] != "English"]

# proceed as normal
``` 

# Datasets
The following is a list of datasets used for each language:  

| Language | Datasets |
| ------------------- | -------------------------- |
| Arabic | [UN Corpora](http://www.uncorpora.org/) |
| English |  [UN Corpora](http://www.uncorpora.org/) |
| Farsi | [BBC News Persian](https://www.bbc.com/persian) |
| French | [UN Corpora](http://www.uncorpora.org/) |
| German | [Deutsche Welle](https://www.dw.com/de) |
| Khmer | [Cambodia Daily](https://www.cambodiadaily.com) |
| Kurmanci (Kurdish) | [Rudaw](https://rudaw.net/kurmanci) |
| Mandarin | [UN Corpora](http://www.uncorpora.org/) |
| Russian | [UN Corpora](http://www.uncorpora.org/) |
| Sorani (Kurdish) | [Rudaw](https://www.rudaw.net/sorani) |
| Spanish | [UN Corpora](http://www.uncorpora.org/) |
| Turkish | [BBC News Türkçe](https://www.bbc.com/turkce) |

# How Does It Work?
When training the model, we scan all the data sources and compute the frequency of how often a character appears in each specific language.  We also compute the frequency of how often a characters appears in all of the data sources for all the languages.  For each language, we then calculate a score for each character as `frequency_in_language / frequency_in_all_languages`.  We then save the top ten highest scoring characters for each language.  
When detecting a language, we simply iterate through the saved characters (ten for each language), and add their score as a weighted-vote for each language.  Whichever, language has the highest score is selected as the winner.

# Contributing
If you'd like to contribute a new language, please consult [CONTRIBUTING.md](CONTRIBUTING.md)

# Support
Contact the package author, Daniel J. Dufour, at daniel.j.dufour@gmail.com
