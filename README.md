
![Python Tests](https://github.com/hamadliaqat682/python-fastapi-automation/actions/workflows/tests.yml/badge.svg)

# Python & FastAPI Lead Qualification Automation

A runnable demonstration API that validates incoming sales leads, applies a transparent scoring rule, and returns a CRM-ready JSON payload.

> **Portfolio demo:** Uses sample data. No live CRM integration, external API calls, lead scraping, or claimed client outcomes.

## Features

- Validates names, email addresses, employee count, and service interest using Pydantic.
- Scores leads with a clear rule and classifies them as high, medium, or low priority.
- Returns normalized contact information, tags, and structured CRM-ready JSON.
- Includes health endpoint, auto-generated OpenAPI documentation, and automated tests.

## Tech stack

Python · FastAPI · Pydantic · pytest · REST APIs

## Workflow

`Form / Webhook → POST /leads/process → Validate → Score & Tag → CRM-ready JSON`

The output can be connected to n8n, GoHighLevel, HubSpot or another CRM **after** adding an authenticated connector.

## Run locally

```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Visit `http://127.0.0.1:8000/docs` to test the API through Swagger UI.

## Example request

```bash
curl -X POST http://127.0.0.1:8000/leads/process \
  -H 'Content-Type: application/json' \
  -d '{"name":"Jane Doe","email":"jane@example.com","company":"Example Co","phone":"+15550102030","employees":35,"interested_in":"ai-agent"}'
```

Expected score: `100`, priority: `high`. The response contains a `crm_payload` object ready for mapping to your CRM fields.

## Run tests

```bash
python -m pytest -q
```

## API endpoints

| Method | Path | Purpose |
|---|---|---|
| GET | `/health` | Service health check |
| POST | `/leads/process` | Validate, qualify, tag, and map a lead |

## Limitations and security

This educational demo contains no database, authentication, rate limiting, persistence, deduplication, or live CRM connection. Before production deployment, add appropriate authentication, data protection, monitoring and privacy controls. Do not commit API tokens, personal customer information, or client assets to a public repository.

## Portfolio context

Created as a self-contained public technical demonstration of Python API and automation design.
