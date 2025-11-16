"""Tests for translator registry functions."""
import pytest
import sys
import os
from unittest.mock import patch, MagicMock
from typing import Type

# Add src to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from translator_registry import discover_schemas, discover_agents
from schemas.base_schema_translator import BaseSchemaTranslator
from inference.base_translator_agent import BaseTranslatorAgent


class MockSchemaTranslator(BaseSchemaTranslator):
    """Mock schema translator for testing."""

    def translate(self, sample: str) -> str:
        return "mock translation"

    @classmethod
    def name(cls) -> str:
        return "MockSchema"


class MockAgent(BaseTranslatorAgent):
    """Mock agent for testing."""

    def setup(self):
        pass

    def generate(self, prompt: str) -> str:
        return "mock response"

    @classmethod
    def name(cls) -> str:
        return "mock_agent"


class TestDiscoverSchemas:
    """Tests for discover_schemas function."""

    def test_discover_schemas(self):
        """Test discovering schema translators."""
        # This test verifies the actual discovery mechanism works
        schemas = discover_schemas()

        # Should discover the actual OCSF translator
        assert 'OCSF' in schemas
        assert issubclass(schemas['OCSF'], BaseSchemaTranslator)

    @patch('pkgutil.iter_modules')
    def test_discover_schemas_empty(self, mock_iter):
        """Test discovering schemas when none exist."""
        mock_iter.return_value = []
        schemas = discover_schemas()
        assert isinstance(schemas, dict)


class TestDiscoverAgents:
    """Tests for discover_agents function."""

    def test_discover_agents(self):
        """Test discovering AI agents."""
        # This test verifies the actual discovery mechanism works
        agents = discover_agents()

        # Should discover the actual Gemini agent
        assert 'gemini' in agents
        assert issubclass(agents['gemini'], BaseTranslatorAgent)

    @patch('pkgutil.iter_modules')
    def test_discover_agents_empty(self, mock_iter):
        """Test discovering agents when none exist."""
        mock_iter.return_value = []
        agents = discover_agents()
        assert isinstance(agents, dict)
