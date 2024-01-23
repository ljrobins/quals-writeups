.PHONY: init all

init:
	source bin/activate && pip install -r requirements.txt
	-rm -rf docs
	mkdir docs
	cd docs && sphinx-quickstart

all:
	python convert.py