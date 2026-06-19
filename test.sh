jf pipc --server-id-resolve=solenglatest --repo-resolve=alpha-pypi-virtual
jf pip install -r requirements.txt --no-cache-dir --force-reinstall --module=sample-py --build-name=testingpy --build-number=11
pip install setuptools wheel
python3 setup.py sdist bdist_wheel
jf rt u dist/ alpha-pypi-dev-local/pypi/ --module=sample-py --build-name=testingpy --build-number=11 --server-id solenglatest
jf rt bp testingpy 11 --server-id solenglatest
