import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'language-detector',
    packages = ['language_detector'],
    package_dir = {'language_detector': 'language_detector'},
    package_data = {'language_detector': ['prep/char_language.txt','tests/__init__.py','tests/test.py']},
    version = '5.0.0',
    description = 'Detect language of text',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author = 'Daniel J. Dufour',
    author_email = 'daniel.j.dufour@gmail.com',
    url = 'https://github.com/DanielJDufour/language-detector',
    download_url = 'https://github.com/DanielJDufour/language-detector/tarball/download',
    keywords = ['arabic','farsi','french','kurdish','kurmanci','language','python','sorani','spanish','tagging','turkish'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
