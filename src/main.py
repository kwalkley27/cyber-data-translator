import argparse
import sys

def define_cli_arguments():
    parser = argparse.ArgumentParser(description='Takes a data sample as an argument and provides a mapping definition to the specifed cyber schema')

    parser.add_argument('--sample', help='Path to the sample file to translate')
    parser.add_argument('--schema', help='Name of the standard schema to translate to (e.g. OCSF)')

    return parser

def main():
    args = define_cli_arguments().parse_args()

    print('Sample file is: ', args.sample)
    print('Schema is: ', args.schema)

if __name__=='__main__':
    main()