#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Command Line Interface."""
from argparse import ArgumentParser
from sys import stderr
from typing import Dict

from project_name.definitions.error import PackageException
from project_name.project_name import run


def get_parser():
    """Add required fields to parser.

    Returns:
        ArgumentParser: Argeparse object.
    """
    package_description = 'Description'
    parser = ArgumentParser(description=package_description)

    arg1_help = 'Description'
    parser.add_argument('-f', '--first-arg', nargs='+', help=arg1_help)

    arg2_help = 'Description'
    parser.add_argument('-s', '--second-arg', nargs='+', help=arg2_help)

    out_help = ('Path to save output file. If not present, same directory of'
                'any input files passed will be used.')
    parser.add_argument('-o', '--outpath', help=out_help)

    return parser


def cli():
    """Command line interface for package.

    Side Effects: Executes program.

    Command Syntax:

    Examples:

    """
    parser = get_parser()
    kwargs = parser.parse_args()

    try:
        kwargs_dict: Dict = vars(kwargs)
        run(**kwargs_dict)
    except PackageException as err:
        err = 'An error occurred.\n\n' + str(err)
        print(err, file=stderr)


if __name__ == '__main__':
    cli()
