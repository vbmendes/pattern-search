
.PHONY: tests
	
tests:
	nosetests

performance:
	python tests/performance.py ${q}

all:
	nosetests
	python tests/performance.py 100000
