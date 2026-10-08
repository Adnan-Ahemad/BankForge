# Architecture

BankForge is structured around three service domains:

- Accounts service for customer and account operations
- Compliance communication service for reminders and alerts
- Product and loan service for lending workflows

The shared `common/` utilities capture database and policy patterns, while `mcp/` provides model-context integration to expose structured operations.
