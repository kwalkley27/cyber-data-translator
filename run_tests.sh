#!/bin/bash
# Script to run tests with proper environment setup

set -e  # Exit on error

echo "Cyber Data Translator - Test Runner"
echo "===================================="
echo ""

# Check if pytest is installed
if ! python3 -c "import pytest" 2>/dev/null; then
    echo "pytest not found. Installing test dependencies..."
    python3 -m pip install --user pytest pytest-cov pytest-mock
    echo ""
fi

# Check if we're in a virtual environment
if [ -z "$VIRTUAL_ENV" ]; then
    echo "⚠️  Warning: Not running in a virtual environment"
    echo "   Consider running: python3 -m venv venv && source venv/bin/activate"
    echo ""
fi

# Run tests
echo "Running tests..."
echo ""
python3 -m pytest tests/ -v --cov=src --cov-report=term-missing --cov-report=html

echo ""
echo "✅ Test run complete!"
echo "   View HTML coverage report: htmlcov/index.html"
echo ""
