#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))
sys.path.insert(0, path.join(here, 'src'))

from harvest import (__version__, __author__, __author_email__, __license__)

with open(path.join(here, 'README.md')) as f:  # , encoding='utf-8'
    long_description = f.read()

setup(
    # Metadata
    name="harvest",
    version=__version__,
    description='A toolkit for extracting posts and post metadata from web forums',
    long_description=long_description,
    author=__author__,
    author_email=__author_email__,
    python_requires='>=3.5',
    license=__license__,
    package_dir={'': 'src'},

    # Package List
    packages=find_packages('src'),

    # Scripts
    scripts=[
        './src/harvest/main.py'
    ],

    # Requirements
    install_requires=[
        'lxml',
        'requests',
        'dateparser',
        'numpy',
        'inscriptis',
        'flask',
        'fuzzywuzzy'
    ]
)
