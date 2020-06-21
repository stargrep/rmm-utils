# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build
TEST_PATH	  = tests
TEST_PY_FILES = $(TEST_PATH)/*.py

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

doc-clean:
	rm -rf _build/
	rm -rf _static/
	rm -rf _templates/
	@echo "cleaned _build, _static and _templates folders"

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	@echo "cleaned build/, dist/, egg-info/ and .pytest_cache/ folders"

test: clean
	@echo "Start py.test task"
	py.test --traceconfig --verbose --color=yes $(TEST_PY_FILES)
	@echo "Successfully completed py.test task"

build: clean test
	@echo "create shippable version"
	. env/bin/activate
	python setup.py sdist bdist_wheel
	@echo "sdist done"

install: build
	@echo "calling the main function"
	. env/bin/activate
	pip install dist/code_scanner-*-py3-none-any.whl
	python -m code_scanner
	@echo "main function of code_scanner executed"

.PHONY: install help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
