#!/usr/bin/env python

from setuptools import setup

setup(
    name='jfrog-python-example',
    version='4.0',
    description='Project example for building Python project with JFrog products',
    author='JFrog',
    author_email='jfrog@jfrog.com',
    url='https://github.com/jfrog/project-examples',
    packages=['pythonExample'],
    install_requires=['PyYAML==5.2', 'nltk'],
)
