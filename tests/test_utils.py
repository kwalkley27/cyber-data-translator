"""Tests for utility functions."""
import pytest
from unittest.mock import Mock, patch, mock_open
from requests.exceptions import ConnectionError, Timeout, HTTPError, RequestException
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from utils import get_text_from_file, get_text_from_url


class TestGetTextFromFile:
    """Tests for get_text_from_file function."""

    def test_successful_file_read(self):
        """Test successfully reading a file."""
        content = "Sample file content"
        with patch('builtins.open', mock_open(read_data=content)):
            result = get_text_from_file('/path/to/file.txt')
            assert result == content

    def test_file_not_found(self):
        """Test handling of non-existent file."""
        with patch('builtins.open', side_effect=FileNotFoundError("File not found")):
            with pytest.raises(FileNotFoundError, match="File '/path/to/file.txt' not found"):
                get_text_from_file('/path/to/file.txt')

    def test_permission_denied(self):
        """Test handling of permission errors."""
        with patch('builtins.open', side_effect=PermissionError("Permission denied")):
            with pytest.raises(PermissionError, match="Permission denied to read file"):
                get_text_from_file('/path/to/file.txt')

    def test_io_error(self):
        """Test handling of I/O errors."""
        with patch('builtins.open', side_effect=IOError("I/O error")):
            with pytest.raises(IOError, match="Error reading file"):
                get_text_from_file('/path/to/file.txt')


class TestGetTextFromUrl:
    """Tests for get_text_from_url function."""

    @patch('requests.get')
    def test_successful_url_fetch(self, mock_get):
        """Test successfully fetching content from a URL."""
        mock_response = Mock()
        mock_response.text = '<html><body><p>Test content</p></body></html>'
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = get_text_from_url('https://example.com', 'html.parser')

        assert 'Test content' in result
        mock_get.assert_called_once_with('https://example.com', timeout=30)

    @patch('requests.get')
    def test_connection_error(self, mock_get):
        """Test handling of connection errors."""
        mock_get.side_effect = ConnectionError("Connection failed")

        with pytest.raises(ConnectionError, match="Failed to connect to the server"):
            get_text_from_url('https://example.com', 'html.parser')

    @patch('requests.get')
    def test_timeout_error(self, mock_get):
        """Test handling of timeout errors."""
        mock_get.side_effect = Timeout("Timeout")

        with pytest.raises(Timeout, match="Request to https://example.com timed out"):
            get_text_from_url('https://example.com', 'html.parser')

    @patch('requests.get')
    def test_http_error(self, mock_get):
        """Test handling of HTTP errors."""
        mock_response = Mock()
        mock_response.status_code = 404
        http_error = HTTPError("404 Not Found")
        http_error.response = mock_response
        mock_get.side_effect = http_error

        with pytest.raises(HTTPError, match="HTTP error occurred"):
            get_text_from_url('https://example.com', 'html.parser')
