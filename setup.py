#!/usr/bin/env python
from distutils.core import setup

setup(
    name='ascii_art_generator',
    version='1.0',
    author='Your Name',
    license='MIT',
    long_description=open('README.md').read(),
    scripts=['projet.py'],
    install_requires=[
        'pyfiglet',
    ],
)
