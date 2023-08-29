#!/bin/sh
python setup.py sdist
jf rt u dist/ alpha-pypi-virtual/pythonWithDockerEnvironment/ --build-name=${Build.DefinitionName} --build-number=${Build.BuildNumber} --module=jfrog-python-example --props=stage=dev
