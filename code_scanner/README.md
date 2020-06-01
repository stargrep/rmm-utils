## Project setup
https://github.com/navdeep-G/samplemod

### Running commands
```
$ python -m venv env
$ source env/bin/activate

move to the util folder
$ cd code_scanner
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
python -m unittest tests.test_proj
```