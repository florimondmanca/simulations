.PHONY: wfa

install:
	python3 -m venv venv
	venv/bin/pip install -U pip
	venv/bin/pip install -r requirements.txt

wfa:
	venv/bin/python -m wfa.main

test:
	venv/bin/pytest
