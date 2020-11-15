py -m pip install --user --upgrade twine
py -m pip install --user --upgrade setuptools wheel
py setup.py sdist bdist_wheel
pause
py -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
pause