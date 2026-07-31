UV=uv

all:

sync:
	$(UV) sync

test:
	$(UV) run pytest --showlocals -rA

lint:
	$(UV) run ruff check .

format:
	$(UV) run ruff format .

format-check:
	$(UV) run ruff format --check .

.PHONY: all sync test lint format format-check
