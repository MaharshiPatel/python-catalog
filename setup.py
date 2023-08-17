#!/usr/bin/env python

from setuptools import setup

setup(
    name='catalog-py',
    version='1.0',
    description='Project example for building Python project with JFrog products',
    author='JFrog',
    url='https://github.com/jfrog/project-examples',
    packages=['catalog-py'],
    install_requires=['PyYAML>3.11', 'nltk'],
)
