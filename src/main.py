import argparse
import logging
import sys
import os
from typing import NoReturn
import utils
import translator_factory

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

AGENT = 'gemini'
DISCLAIMER = '''This content was generated using artificial intelligence. While we strive for accuracy,
AI-generated content may contain errors or inaccuracies. The output of this model may vary from one
request to another. We strongly recommend that you independently verify all information before making
decisions. We disclaim any and all liability for any errors or omissions in the content produced by
this technology.'''

def define_cli_arguments() -> argparse.ArgumentParser:
    """Define command-line arguments for the translator.

    Returns:
        Configured argument parser
    """
    parser = argparse.ArgumentParser(
        description='Takes a data sample as an argument and provides a mapping definition to the specified cyber schema'
    )

    parser.add_argument(
        '--sample',
        required=True,
        help='Path to the sample file to translate'
    )
    parser.add_argument(
        '--schema',
        required=True,
        help='Name of the standard schema to translate to (e.g. OCSF)'
    )

    return parser

def print_disclaimer() -> None:
    """Print the AI-generated content disclaimer."""
    print(DISCLAIMER)

def main() -> NoReturn:
    """Main entry point for the cyber data translator."""
    try:
        parser = define_cli_arguments()
        args = parser.parse_args()

        logger.info(f"Starting translation with schema: {args.schema}")
        logger.info(f"Reading sample file: {args.sample}")

        # Read the sample file
        sample_text = utils.get_text_from_file(os.path.normpath(args.sample))

        # Initialize agent and schema translator
        logger.info(f"Initializing {AGENT} agent")
        agent = translator_factory.get_agent(AGENT)()
        schema_translator = translator_factory.get_schema(args.schema)(agent)

        # Print disclaimer
        print_disclaimer()
        print('\n')

        # Perform translation
        logger.info("Starting translation process")
        schema_translator.translate(sample_text)

        logger.info("Translation completed successfully")
        sys.exit(0)

    except FileNotFoundError as e:
        logger.error(f"File error: {e}")
        sys.exit(1)
    except ValueError as e:
        logger.error(f"Configuration error: {e}")
        sys.exit(1)
    except KeyError as e:
        logger.error(f"Environment configuration error: {e}")
        logger.error("Make sure GEMINI_API_KEY is set in your environment")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        sys.exit(1)


if __name__ == '__main__':
    main()