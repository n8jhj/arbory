"""This setup.py adapted from
https://github.com/kennethreitz/setup.py/blob/master/setup.py

Note: To use the 'upload' functionality of this file, you must:
$ pipenv install twine --dev
"""

import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup

# Package meta-data.
NAME = 'arbory'
DESCRIPTION = 'Nice directory trees.'
URL = 'https://github.com/n8jhj/arbory'
EMAIL = 'nathaniel.j.jones@wsu.edu'
AUTHOR = 'Nathaniel Jones'
REQUIRES_PYTHON = '>=3.5.0'
VERSION = '0.0.1'

REQUIRED = [
    # 'click',
]

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in the MANIFEST.in file.
try:
    with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    install_requires=REQUIRED,
    include_package_data=True,
    license='BSD',
    classifiers=[
        # Trove classifiers.
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Decelopment Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Topic :: System :: Filesystems',
        'Topic :: Utilities',
    ],
)
