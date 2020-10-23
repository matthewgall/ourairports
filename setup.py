"""A setuptools based setup module for ourairports
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path
import os, re

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# And get version information from the Makefile
version = os.getenv('VERSION')

setup(
    name='ourairports',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=version,

    description='ourairports is an excellent client side library for all your airport data needs',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/matthewgall/ourairports',

    # Author details
    author='Matthew Gall',
    author_email='complaints@matthewgall.com',

    # Choose your license
    license='MIT',

    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='linux,windows,macos',
    
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project?
        'Development Status :: 4 - Beta',

        # And environment
        'Environment :: Console',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    entry_points={},
    install_requires=['geopy'],
    data_files=[('', [
        'ourairports/data/airports.csv.gz',
        'ourairports/data/countries.csv.gz',
        'ourairports/data/frequencies.csv.gz',
        'ourairports/data/navaids.csv.gz',
        'ourairports/data/regions.csv.gz',
        'ourairports/data/runways.csv.gz'
    ])]
)
