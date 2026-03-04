# Expense Tracker Makefile
# Run `make help` to see available commands

PYTHON := python
PIP := pip
APP := expense_tracker.web.app:app

.PHONY: help install run test lint fmt check clean migrate revision

help:
	@echo "Available commands:"
	@echo "  make install     Install project + dev dependencies"
	@echo "  make run         Run the FastAPI server"
	@echo "  make test        Run tests"
	@echo "  make lint        Run Ruff linter"
	@echo "  make fmt         Format code (Ruff + Black)"
	@echo "  make check       Lint + format check + tests"
	@echo "  make clean       Remove caches and temp files"
	@echo ""
	@echo "Future database commands:"
	@echo "  make migrate     Apply database migrations"
	@echo "  make revision    Create new migration"

install:
	$(PIP) install -e ".[dev]"

run:
	$(PYTHON) -m uvicorn $(APP) --reload

test:
	$(PYTHON) -m pytest

lint:
	$(PYTHON) -m ruff check .

fmt:
	$(PYTHON) -m ruff check . --fix
	$(PYTHON) -m black .

check:
	$(PYTHON) -m ruff check .
	$(PYTHON) -m black --check .
	$(PYTHON) -m pytest

clean:
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	rm -rf *.egg-info
	find . -type d -name "__pycache__" -exec rm -rf {} +

# ---- migrations (we will enable once Alembic is installed) ----

revision:
	alembic revision --autogenerate -m "migration"

migrate:
	alembic upgrade head