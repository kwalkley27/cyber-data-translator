import argparse
import utils
import translator_factory

AGENT='gemini'

def define_cli_arguments():
    parser = argparse.ArgumentParser(description='Takes a data sample as an argument and provides a mapping definition to the specifed cyber schema')

    parser.add_argument('--sample', help='Path to the sample file to translate')
    parser.add_argument('--schema', help='Name of the standard schema to translate to (e.g. OCSF)')

    return parser

def print_disclaimer():
    disclaimer = '''This content was generated using artificial intelligence. While we strive for accuracy, AI-generated content may contain errors or inaccuracies. The output of this model may vary from one request to another. We strongly recommend that you independently verify all information before making decisions. We disclaim any and all liability for any errors or omissions in the content produced by this technology. '''

    print(disclaimer)

def main():
    args = define_cli_arguments().parse_args()

    sample_text = utils.get_text_from_file(args.sample)
    agent = translator_factory.get_agent(AGENT)()
    schema_translator = translator_factory.get_schema(args.schema)(agent)

    print_disclaimer()

    schema_translator.translate(sample_text)


if __name__=='__main__':
    main()