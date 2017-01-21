from distutils.core import setup

setup(
  name = 'language-detector',
  packages = ['language_detector'],
  package_dir = {'language_detector': 'language_detector'},
  package_data = {'language_detector': ['prep/char_language.txt','tests/__init__.py','tests/test.py']},
  version = '3.1',
  description = 'Detect language of text',
  author = 'Daniel J. Dufour',
  author_email = 'daniel.j.dufour@gmail.com',
  url = 'https://github.com/DanielJDufour/language-detector',
  download_url = 'https://github.com/DanielJDufour/language-detector/tarball/download',
  keywords = ['arabic','farsi','french','kurdish','kurmanci','language','python','sorani','spanish','tagging','turkish'],
  classifiers = [],
)
