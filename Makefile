
.PHONY: tests

default: tests

tests:
	nosetests

performance:
	python tests/performance.py ${q}
