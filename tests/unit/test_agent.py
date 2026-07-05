"""KPI Monitoring Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_track_kpi():
    """Test Track a KPI value with trend and status against target."""
    tools = AgentTools()
    result = await tools.track_kpi(kpi_name="test", period="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_detect_anomaly():
    """Test Detect anomalous changes in a KPI value."""
    tools = AgentTools()
    result = await tools.detect_anomaly(kpi_name="test", sensitivity="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_set_alert():
    """Test Set up threshold-based alerting for a KPI."""
    tools = AgentTools()
    result = await tools.set_alert(kpi_name="test", threshold="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_diagnose_change():
    """Test Diagnose root cause of a significant KPI change."""
    tools = AgentTools()
    result = await tools.diagnose_change(kpi_name="test", change_period="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.kpi_monitoring_agent_agent import KpiMonitoringAgentAgent
    agent = KpiMonitoringAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
