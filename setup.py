#!/usr/bin/env python

from setuptools import setup

setup(
    name='jfrog-python-example',
    version='12.0',
    description='Project example for building Python project with JFrog products',
    author='JFrog',
    url='https://github.com/jfrog/project-examples',
    packages=['pythonExample'],
    install_requires=['PyYAML', 'nltk'],
)
