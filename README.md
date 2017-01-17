# language-detector
language-detector detects the language of text

# Installation
```
pip install language-detector
```

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
| Farsi |
| French |
| German |
| Kurmanci (Kurdish) |
| Sorani (Kurdish) |
| Spanish|
| Turkish |

# Testing
To test the package run
```
python -m unittest language_detector.tests.test
```

# Comparison
| package | language-detector | langid |
| -------------------------------- |
| test-duration | 0.08 | 2.51 |
| accuracy | 93.55% | 67.74% |

# Excluding Languages
If you don't want language-detector to look for certain languages, you can monkey-patch the code.  For example, in order to exclude English:
```
import language_detector
language_detector.char_language = [cl for cl in char_language if cl[1] != "English"]

# proceed as normal
``` 
