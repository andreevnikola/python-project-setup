check:
	uv run ruff format .
	uv run ruff check .
	uv run pyright

run-a: check
	uv run service-a

run-b: check
	uv run service-b