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
```

# Features
| Languages Supported |
| ------------------- |
| Arabic |
| Farsi |
| French |
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
|package|language-detector|langid|
|--------------------------------|
|test-duration|0.0320|2.4251|
|accuracy|63.3%|70.0%|
