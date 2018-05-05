from argparse import RawDescriptionHelpFormatter
from textwrap import dedent

import argparse
import os


def main():
    available_commands = dedent('''
    available subcommands:
    \tclean              clean files out
    \trename             rename files
    '''.expandtabs(2))
    parser = argparse.ArgumentParser(prog='bft', description='batch file transformer.', 
        epilog=available_commands, formatter_class=RawDescriptionHelpFormatter)
    
    parser.add_argument('subcommand', type=str, help='subcommand to run')
    parser.add_argument('path', type=str, help='path to target directory')

    parser.add_argument('-v', '--verbosity', 
                        action='store_true', help='increase output verbosity')
    parser.add_argument('-r', '--recursively', 
                        action='store_false', help='include subdirectories')
    parser.add_argument('-n', '--no-special-files', 
                        action='store_false', help='exclude special files starting with a dot.')
    parser.add_argument('-p', '--prefix', default='', metavar='',
                        type=str, help='filename prefix')
    parser.add_argument('-t', '--postfix', default='', metavar='',
                        type=str, help='filename postfix')

    args = parser.parse_args()
    print(args)


def list_files(path, recursion=False):  
    filelist = []
    
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            filelist.append(os.path.join(dirpath, filename))
        if not recursion:
            break
    
    return filelist


def clean(args):
    filelist = list_files(args.path, args.recursively)
    successfully_cleaned = len(filelist)

    for filepath in filelist:
        if os.path.basename(filepath)[0] == '.' and args.no_special_files:
            # Stumbled onto special file starting with a dot and --no-special-files flag
            # was set.
            successfully_cleaned -= 1
        else:
            try:
                with open(filepath, 'w') as f:
                    f.write('')
            except PermissionError:
                successfully_cleaned -= 1
                if args.verbosity:
                    print('Could not clean out {}. Permission denied.'.format(filepath))

    if args.verbosity:
        print(f'Successfully cleaned out {successfully_cleaned}/{len(filelist)} files.')


def rename():
    pass


if __name__ == '__main__':
    main()
