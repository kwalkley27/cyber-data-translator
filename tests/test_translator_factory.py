"""Tests for translator factory functions."""
import pytest
import sys
import os
from unittest.mock import patch, MagicMock

# Add src to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from translator_factory import get_schema, get_agent
from schemas.base_schema_translator import BaseSchemaTranslator
from inference.base_translator_agent import BaseTranslatorAgent


class TestGetSchema:
    """Tests for get_schema function."""

    def test_get_valid_schema(self):
        """Test getting a valid schema."""
        with patch('translator_factory._schema_classes', {'OCSF': MagicMock(spec=BaseSchemaTranslator)}):
            schema = get_schema('OCSF')
            assert schema is not None

    def test_get_invalid_schema(self):
        """Test getting an invalid schema raises ValueError."""
        with patch('translator_factory._schema_classes', {}):
            with pytest.raises(ValueError, match="Schema with name InvalidSchema is not currently supported"):
                get_schema('InvalidSchema')


class TestGetAgent:
    """Tests for get_agent function."""

    def test_get_valid_agent(self):
        """Test getting a valid agent."""
        with patch('translator_factory._agent_classes', {'gemini': MagicMock(spec=BaseTranslatorAgent)}):
            agent = get_agent('gemini')
            assert agent is not None

    def test_get_invalid_agent(self):
        """Test getting an invalid agent raises ValueError."""
        with patch('translator_factory._agent_classes', {}):
            with pytest.raises(ValueError, match="Agent with name invalid is not currently supported"):
                get_agent('invalid')
