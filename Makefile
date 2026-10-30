PYTHON := .venv/bin/python

.PHONY: install basis run

install:
	python3 -m venv .venv
	$(PYTHON) -m pip install -r requirements.txt

basis:
	$(PYTHON) basis.py

run:
	$(PYTHON) telephone.py
