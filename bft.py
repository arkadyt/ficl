from argparse import RawDescriptionHelpFormatter
from textwrap import dedent

import argparse


def main():
    available_commands = dedent('''
    available subcommands:
    \tclean              clean files out
    \trename             rename files
    '''.expandtabs(2))
    parser = argparse.ArgumentParser(prog='bft', description='batch file transformer.', 
        epilog=available_commands, formatter_class=RawDescriptionHelpFormatter)
    
    parser.add_argument('command', type=str, help='subcommand to run')
    parser.add_argument('path', type=str, help='path to target directory')

    parser.add_argument('-v', '--verbosity', 
                        action='store_true', help='increase output verbosity')
    parser.add_argument('-r', '--recursively', 
                        action='store_false', help='include subdirectories')
    parser.add_argument('-p', '--prefix', default='', metavar='',
                        type=str, help='filename prefix')
    parser.add_argument('-t', '--postfix', default='', metavar='',
                        type=str, help='filename postfix')

    parser.parse_args()


def clean():
    pass


def rename():
    pass


if __name__ == '__main__':
    main()
