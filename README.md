# Cyber Data Translator

![CI](https://github.com/kwalkley27/cyber-data-translator/workflows/CI/badge.svg)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

A command-line tool to translate raw cyber data into normalized schemas using generative AI.

## Overview

This tool takes a sample of raw data (e.g., a log file) and a target schema (e.g., OCSF) and uses a generative AI agent (like Google's Gemini) to infer the correct data mapping. It helps security analysts and engineers quickly understand and normalize diverse data formats.

## Features

*   **Dynamic Schema Translation:** Translates raw data to a specified schema
*   **Extensible Architecture:** Easily add support for new schemas and AI agents through a plugin system
*   **AI-Powered:** Leverages large language models for intelligent mapping
*   **Type-Safe:** Full type hints for better IDE support and code quality
*   **Comprehensive Error Handling:** Robust error handling with informative messages
*   **Logging Support:** Built-in logging for debugging and monitoring
*   **Well-Tested:** Comprehensive unit test coverage with pytest
*   **Currently Supported Schemas:** OCSF (Open Cybersecurity Schema Framework)
*   **Currently Supported Agents:** Google Gemini

## Requirements

- Python 3.9 or higher
- Google Gemini API key

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/kwalkley27/cyber-data-translator.git
    cd cyber-data-translator
    ```

2.  Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3.  Set up your environment variables:
    ```bash
    # Copy the example environment file
    cp .env.example .env

    # Edit .env and add your actual API key
    # GEMINI_API_KEY=your_actual_api_key_here
    ```

    Alternatively, export the API key directly:
    ```bash
    export GEMINI_API_KEY='your_api_key_here'
    ```

    **Note:** You can get a Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey).

## Usage

To translate a data sample, run the `main.py` script with the path to your sample file and the desired schema.

```bash
python src/main.py --sample /path/to/your/sample.txt --schema OCSF
```

### Example

Given a sample file `sample.txt` with the following content:
```json
{
  "timestamp": "2025-08-09T10:00:00Z",
  "source_ip": "192.168.1.100",
  "destination_ip": "10.0.0.5",
  "action": "allowed"
}
```

The tool will output the inferred OCSF category, class, and the mapped fields.

## Development

### Setting Up Development Environment

1. Install development dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. The project uses the following development tools:
   - **pytest** for testing
   - **pytest-cov** for coverage reporting
   - **pytest-mock** for mocking in tests
   - **python-dotenv** for environment variable management

### Project Structure

```
cyber-data-translator/
├── src/
│   ├── inference/          # AI agent implementations
│   │   ├── base_translator_agent.py
│   │   └── gemini_agent.py
│   ├── schemas/            # Schema translator implementations
│   │   ├── definitions/    # Schema definitions and URL mappings
│   │   ├── base_schema_translator.py
│   │   └── ocsf_translator.py
│   ├── main.py            # CLI entry point
│   ├── translator_factory.py
│   ├── translator_registry.py
│   └── utils.py
├── tests/                 # Unit tests
├── .github/workflows/     # CI/CD configuration
└── requirements.txt
```

### Running Tests

Run the test suite:
```bash
python3 -m pytest tests/ -v
```

Run tests with coverage report:
```bash
python3 -m pytest tests/ --cov=src --cov-report=html
```

Or use the provided test script:
```bash
./run_tests.sh
```

For detailed testing instructions, see [TESTING.md](TESTING.md).

### Adding New Schemas

To add support for a new schema:

1. Create a new file in `src/schemas/` (e.g., `new_schema_translator.py`)
2. Inherit from `BaseSchemaTranslator`
3. Implement the required methods:
   - `translate(sample: str) -> None`
   - `name() -> str` (class method)

The schema will be automatically discovered and registered.

### Adding New AI Agents

To add a new AI agent:

1. Create a new file in `src/inference/` (e.g., `new_agent.py`)
2. Inherit from `BaseTranslatorAgent`
3. Implement the required methods:
   - `setup()` - Initialize the AI model
   - `generate(prompt: str) -> str` - Generate responses
   - `name() -> str` (class method)

The agent will be automatically discovered and registered.

## Continuous Integration

This project uses GitHub Actions for CI/CD:
- Runs tests on Python 3.9, 3.10, 3.11, and 3.12
- Generates coverage reports
- Runs on every push and pull request to main branch

## Security

- **Never commit `.env` files** - They are gitignored by default
- API keys should be stored as environment variables
- See `.env.example` for required configuration

## Contributing

Contributions are welcome! Please ensure:
1. All tests pass: `pytest`
2. Code includes type hints
3. New features include tests
4. Follow existing code style

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This content was generated using artificial intelligence. While we strive for accuracy, AI-generated content may contain errors or inaccuracies. The output of this model may vary from one request to another. We strongly recommend that you independently verify all information before making decisions. We disclaim any and all liability for any errors or omissions in the content produced by this technology.