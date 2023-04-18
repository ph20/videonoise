.PHONY: install build dist clean

install:
	pip install -e .

build:
	python -m build

clean:
	rm -rf dist
	find . -name "*.egg-info" -exec rm -rf {} +
	find . -name "*.pyc" -exec rm -f {} +
	find . -name "__pycache__" -exec rm -rf {} +
