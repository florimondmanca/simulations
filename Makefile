.PHONY: wfc

sources = wfc

install:
	python3 -m venv venv
	venv/bin/pip install -U pip
	venv/bin/pip install -r requirements.txt

format:
	venv/bin/black ${sources}

wfc:
	venv/bin/python -m wfc.main

test:
	venv/bin/pytest
