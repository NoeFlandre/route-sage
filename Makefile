.PHONY: lint format type-check check

#Run everything to ensure the code is "binary clean"
check: lint type-check

lint:
	uv run ruff check .

format:
	uv run ruff format .

type-check:
	uv run mypy .