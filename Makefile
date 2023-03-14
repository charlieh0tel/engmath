PYTEST=pytest-3
PYLINT=pylint
PYFORMAT=black

all:

test:
	$(PYTEST) --showlocals -rA

lint:
	$(PYLINT) --reports=n --persistent=n --score=n *.py

format:
	$(PYFORMAT) *.py
