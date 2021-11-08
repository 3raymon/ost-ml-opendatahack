""""
autor:  ramon.carlucci@ost.ch
date:   2021-08-11

Installer for OST-ML_OPENDATAHACK

just ensure that
`python3 -m pip install --upgrade pip setuptools wheel`
is working and run: `python3 -m install .`
in the root directory to install all required packages
"""

import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "OST-ML_OPENDATAHACK",
    version = "1.0",
    author = "Ramòn Carlucci",
    author_email = "ramon.carlucci@ost.ch",
    description = ("Solution and Work to the Open Data Hack St.Gallen"),
    url = "https://github.com/3raymon/ost-ml-opendatahack",
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'openpyxl',
        'pprintpp',
        'statsmodels',
        'sklearn',
    ],
    long_description=read('README.md'),
)