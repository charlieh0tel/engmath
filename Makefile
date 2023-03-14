PYTEST=pytest-3
PYLINT=pylint


all:

test:
	$(PYTEST) --showlocals

lint:
	$(PYLINT) --reports=n --persistent=n --score=n *.py
