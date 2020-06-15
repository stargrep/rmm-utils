TEST_PATH=tests
TEST_PY_FILES=$(TEST_PATH)/*.py

.PHONY: run-all
run-all: clean test

clean:
	rm -rf build/
	rm -rf dist
	rm -rf *.egg-info
	@echo "cleaned build/, dist/ and egg-info/ folders"

test: clean
	@echo "Start py.test task"
	py.test --traceconfig --verbose --color=yes $(TEST_PY_FILES)
	@echo "Successfully completed py.test task"

build: clean test
	@echo "create shippable version"
	. env/bin/activate
	python setup.py sdist
	@echo "sdist done"

install: build
	@echo "calling the main function"
	. env/bin/activate
	pip install dist/code_scanner-*.tar.gz
	python -m code_scanner
	@echo "main function of code_scanner executed"
