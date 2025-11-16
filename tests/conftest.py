"""Pytest configuration and fixtures."""
import sys
import os

# Add src directory to Python path for all tests
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
