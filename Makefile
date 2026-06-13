all: init test

init:
	pip install -e .
	pip install tox coverage

test:
	coverage erase
	tox
	coverage html
