# Cyber Data Translator

A command-line tool to translate raw cyber data into normalized schemas using generative AI.

## Overview

This tool takes a sample of raw data (e.g., a log file) and a target schema (e.g., OCSF) and uses a generative AI agent (like Google's Gemini) to infer the correct data mapping. It helps security analysts and engineers quickly understand and normalize diverse data formats.

## Features

*   **Dynamic Schema Translation:** Translates raw data to a specified schema.
*   **Extensible:** Easily add support for new schemas and AI agents.
*   **AI-Powered:** Leverages large language models for intelligent mapping.
*   **Currently Supported Schemas:** OCSF (Open Cybersecurity Schema Framework)
*   **Currently Supported Agents:** Gemini

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/cyber-data-translator.git
    cd cyber-data-translator
    ```

2.  Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3.  Set up your environment variables. For the Gemini agent, you'll need to set your API key:
    ```bash
    export GOOGLE_API_KEY='your_api_key_here'
    ```

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

## Disclaimer

This content was generated using artificial intelligence. While we strive for accuracy, AI-generated content may contain errors or inaccuracies. The output of this model may vary from one request to another. We strongly recommend that you independently verify all information before making decisions. We disclaim any and all liability for any errors or omissions in the content produced by this technology.