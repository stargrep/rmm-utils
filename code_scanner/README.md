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

### Report
```
# get all lines of code
git ls-files | xargs wc -l

# code-scanner output

```

### Sample Output 
``` v0.2.0

$python -m code_scanner

$pwd 
can find the folder and .__scanned_result.txt

in .__scanned_result.txt

------------------------------------
------------------------------ start
Python Source Files

2020-06-12 17:22:43.459211

Source Lines (w/o Comments): 402 (251) Lines 62.0%
Total Lines (w/o Comments): 638 (383) Lines 60.0% 

Non-tests Ratio (w/o Comments): 63.0% (65.0%)
------------------------------ end
------------------------------------

```