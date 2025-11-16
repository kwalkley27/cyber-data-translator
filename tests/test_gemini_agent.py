"""Tests for Gemini AI agent."""
import pytest
import sys
import os
from unittest.mock import patch, MagicMock

# Add src to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from inference.gemini_agent import GeminiAgent


class TestGeminiAgent:
    """Tests for GeminiAgent class."""

    @patch.dict(os.environ, {'GEMINI_API_KEY': 'test_key'})
    @patch('google.generativeai.GenerativeModel')
    def test_initialization_with_api_key(self, mock_model):
        """Test successful initialization with API key."""
        mock_model_instance = MagicMock()
        mock_model.return_value = mock_model_instance

        agent = GeminiAgent()

        assert agent is not None
        assert agent.model is not None
        mock_model.assert_called_once()

    @patch.dict(os.environ, {}, clear=True)
    def test_initialization_without_api_key(self):
        """Test initialization fails without API key."""
        with pytest.raises(KeyError, match="GEMINI_API_KEY"):
            GeminiAgent()

    @patch.dict(os.environ, {'GEMINI_API_KEY': 'test_key'})
    @patch('google.generativeai.GenerativeModel')
    def test_generate(self, mock_model_class):
        """Test generate method."""
        # Setup mock
        mock_response = MagicMock()
        mock_response.text = "  Generated response  "

        mock_model_instance = MagicMock()
        mock_model_instance.generate_content.return_value = mock_response
        mock_model_class.return_value = mock_model_instance

        agent = GeminiAgent()
        result = agent.generate("test prompt")

        assert result == "Generated response"
        mock_model_instance.generate_content.assert_called_once_with("test prompt")

    def test_name(self):
        """Test class name method."""
        assert GeminiAgent.name() == 'gemini'

    @patch.dict(os.environ, {'GEMINI_API_KEY': 'test_key'})
    @patch('google.generativeai.GenerativeModel')
    def test_setup(self, mock_model):
        """Test setup method."""
        mock_model_instance = MagicMock()
        mock_model.return_value = mock_model_instance

        agent = GeminiAgent()
        result = agent.setup("Custom instructions")

        assert result is not None
        # Verify it was called during initialization
        assert mock_model.call_count >= 1
