from setuptools import setup
from os.path import abspath, dirname, join

root_dir = abspath(dirname(__file__))

with open(join(root_dir, "README.md")) as f:
    long_description = f.read()

setup(
    name = 'language-detector',
    packages = ['language_detector'],
    package_dir = {'language_detector': 'language_detector'},
    package_data = {'language_detector': ['prep/char_language.txt','tests/__init__.py','tests/test.py']},
    version = '5.0.1',
    description = 'Detect language of text',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author = 'Daniel J. Dufour',
    author_email = 'daniel.j.dufour@gmail.com',
    url = 'https://github.com/DanielJDufour/language-detector',
    download_url = 'https://github.com/DanielJDufour/language-detector/tarball/download',
    keywords = ['arabic','farsi','french','kurdish','kurmanci','language','nlp','python','sorani','spanish','tagging','turkish'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ]
)
