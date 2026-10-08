# How to Run BankForge

## Prerequisites

- Python 3.11+
- Docker and Docker Compose
- `pip install -r requirements.txt`

## Local setup

1. Create a virtual environment:
   python -m venv .venv
   source .venv/bin/activate
2. Install dependencies:
   pip install -r requirements.txt
3. Run the seeded demo:
   python run_local_demo.py

## Docker workflow

1. Build and start services:
   docker-compose up --build
2. Stop the stack:
   docker-compose down

## Useful scripts

- Seed account data: `python scripts/seed_accounts.py`
- Seed compliance data: `python scripts/seed_compliance.py`
- Seed products: `python scripts/seed_products.py`
- Run showcase scenario: `python showcase_scenario.py`
- Run stress tests: `python stress_tests.py`

## Notes

This repository is scaffolded to support demonstration, validation, and compliance workflows. Expand the service implementations in the `servers/` and `mcp/` folders to match your production needs.
