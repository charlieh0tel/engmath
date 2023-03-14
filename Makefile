PYTEST=pytest-3
PYLINT=pylint


all:

test:
	$(PYTEST) --showlocals -rA --cache-clear

lint:
	$(PYLINT) --reports=n --persistent=n --score=n *.py
