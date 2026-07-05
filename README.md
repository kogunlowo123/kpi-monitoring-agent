# KPI Monitoring Agent

[![CI](https://github.com/kogunlowo123/kpi-monitoring-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/kpi-monitoring-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Business Intelligence | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

KPI monitoring agent that tracks business metrics in real-time, detects anomalies, sends threshold-based alerts, provides root cause analysis for metric changes, and manages KPI definitions across the organization.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `track_kpi` | Track a KPI value with trend and status against target |
| `detect_anomaly` | Detect anomalous changes in a KPI value |
| `set_alert` | Set up threshold-based alerting for a KPI |
| `diagnose_change` | Diagnose root cause of a significant KPI change |
| `define_kpi` | Define a new KPI with calculation formula and ownership |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/api/v1/kpis/{kpi_name}/track` | Track KPI |
| `GET` | `/api/v1/kpis/{kpi_name}/anomaly` | Detect anomaly |
| `POST` | `/api/v1/kpis/{kpi_name}/alert` | Set alert |
| `POST` | `/api/v1/kpis/{kpi_name}/diagnose` | Diagnose change |
| `POST` | `/api/v1/kpis/define` | Define KPI |

## Features

- Real Time Tracking
- Anomaly Alerts
- Threshold Management
- Root Cause Analysis
- Kpi Definitions

## Integrations

- Looker
- Dbt Metrics
- Cube Dev
- Datadog
- Pagerduty

## Architecture

```
kpi-monitoring-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── kpi_monitoring_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Metrics Layer + Alerting + Data Warehouse**

---

Built as part of the Enterprise AI Agent Platform.
