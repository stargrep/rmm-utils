## Project setup
https://github.com/navdeep-G/samplemod

## RUN
to build, simply go with:
```
make
```

to use, simply starts:
```
pip install dist/code_scanner-{version}.tar.gz
```


### Useful Commands
```
$ python -m venv env
$ source env/bin/activate

move to the util folder, install according to the requirement.txt
$ cd code_scanner
$ pip install -r requirements.txt
$ python setup.py build
$ python setup.py sdist

install
$ pip install dist/code_scanner-1.0.1.tar.gz

use
python -m code_scanner
OR
python -m code_scanner.$file

analyze
python -v -m code_scanner 2>&1 | grep '^import'

unit test
pytest --fixtures # find all fixture info
```