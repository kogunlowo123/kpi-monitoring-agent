"""Test configuration for KPI Monitoring Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "kpi-monitoring-agent", "category": "Business Intelligence"}
