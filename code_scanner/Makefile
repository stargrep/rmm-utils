TEST_PATH=tests
TEST_PY_FILES=$(TEST_PATH)/*.py

.PHONY: run-all
run-all: clean-build py-test

clean-build:
	rm -rf build/
	rm -rf dist
	rm -rf *.egg-info
	@echo "cleaned build and dist folders"

py-test: clean-build
	@echo "Start py.test task"
	py.test --verbose --color=yes $(TEST_PY_FILES)
	@echo "Successfully completed py.test task"

