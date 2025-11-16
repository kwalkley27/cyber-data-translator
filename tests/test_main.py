"""Tests for main entry point."""
import pytest
import sys
import os
from unittest.mock import patch, MagicMock, mock_open
from argparse import Namespace

# Add src to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from main import define_cli_arguments, print_disclaimer, main as main_func


class TestDefineCliArguments:
    """Tests for CLI argument parser."""

    def test_parser_creation(self):
        """Test that parser is created correctly."""
        parser = define_cli_arguments()
        assert parser is not None

    def test_required_arguments(self):
        """Test that sample and schema are required."""
        parser = define_cli_arguments()
        with pytest.raises(SystemExit):
            parser.parse_args([])


class TestPrintDisclaimer:
    """Tests for disclaimer printing."""

    def test_disclaimer_prints(self, capsys):
        """Test that disclaimer is printed."""
        print_disclaimer()
        captured = capsys.readouterr()
        assert 'artificial intelligence' in captured.out.lower()
        assert 'errors or inaccuracies' in captured.out.lower()


class TestMain:
    """Tests for main function."""

    @patch('utils.get_text_from_file')
    @patch('translator_factory.get_agent')
    @patch('translator_factory.get_schema')
    @patch('sys.argv', ['main.py', '--sample', 'test.txt', '--schema', 'OCSF'])
    def test_main_success(self, mock_get_schema, mock_get_agent, mock_get_file):
        """Test successful execution of main."""
        # Setup mocks
        mock_get_file.return_value = "sample data"
        mock_agent_instance = MagicMock()
        mock_agent = MagicMock(return_value=mock_agent_instance)
        mock_get_agent.return_value = mock_agent

        mock_schema_instance = MagicMock()
        mock_schema = MagicMock(return_value=mock_schema_instance)
        mock_get_schema.return_value = mock_schema

        # Run main and expect SystemExit with code 0
        with pytest.raises(SystemExit) as exc_info:
            main_func()
        assert exc_info.value.code == 0

        # Verify calls
        mock_get_file.assert_called_once()
        mock_schema_instance.translate.assert_called_once_with("sample data")

    @patch('utils.get_text_from_file')
    @patch('sys.argv', ['main.py', '--sample', 'missing.txt', '--schema', 'OCSF'])
    def test_main_file_not_found(self, mock_get_file):
        """Test main handles FileNotFoundError."""
        mock_get_file.side_effect = FileNotFoundError("File not found")

        with pytest.raises(SystemExit) as exc_info:
            main_func()
        assert exc_info.value.code == 1

    @patch('utils.get_text_from_file')
    @patch('translator_factory.get_schema')
    @patch('sys.argv', ['main.py', '--sample', 'test.txt', '--schema', 'InvalidSchema'])
    def test_main_invalid_schema(self, mock_get_schema, mock_get_file):
        """Test main handles invalid schema."""
        mock_get_file.return_value = "sample data"
        mock_get_schema.side_effect = ValueError("Schema not supported")

        with pytest.raises(SystemExit) as exc_info:
            main_func()
        assert exc_info.value.code == 1

    @patch('utils.get_text_from_file')
    @patch('translator_factory.get_agent')
    @patch('sys.argv', ['main.py', '--sample', 'test.txt', '--schema', 'OCSF'])
    def test_main_missing_api_key(self, mock_get_agent, mock_get_file):
        """Test main handles missing API key."""
        mock_get_file.return_value = "sample data"
        mock_agent = MagicMock(side_effect=KeyError("GEMINI_API_KEY not set"))
        mock_get_agent.return_value = mock_agent

        with pytest.raises(SystemExit) as exc_info:
            main_func()
        assert exc_info.value.code == 1
