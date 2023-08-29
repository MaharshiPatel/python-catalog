#!/bin/sh

python3 setup.py sdist bdist_wheel

jf rt u dist/ alpha-pypi-virtual/pythonWithDockerEnvironment/ --build-name=${Build.DefinitionName} --build-number=${Build.BuildNumber} --module=jfrog-python-example --props=stage=dev
