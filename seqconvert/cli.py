#!/usr/bin/env python3

"""
Filename: cli.py
Author:   William Whinn

Command-line interface for the 'seqconvert' class.
"""

############################
# Global PyLint Directives #
############################

# PyLint Directives
# pylint: disable=relative-beyond-top-level

# PyLint Notes
# - False positive: Import is relative to current location.

###########
# Imports #
###########

import sys
from os import path
from . import main

####################
# Global Variables #
####################

# PACKAGE METADATA

AUTHOR = 'William Whinn'
VERSION = '0.1.0'
URL = 'https://github.com/ultraviolet-1986/seqconvert'

#############
# Functions #
#############

def cli():
    """Command-line interface for the 'seqconvert' class."""

    # PyLint Directives
    # pylint: disable=too-many-branches

    seq_convert = main.SeqConvert()

    if sys.argv[1] == '--help' or sys.argv[1] == '-h':
        print("Usage: seqconvert.py [OPTION] [SEQUENCE]\n",
              "  -h, --help\t\tDisplay this help and exit.",
              "  -v, --version\t\tDisplay version information and exit.\n",
              "  -dm, --dna-mrna\tConvert DNA sequence to mRNA sequence.",
              "  -mt, --mrna-trna\tConvert mRNA sequence to tRNA sequence.",
              "  -tp, --trna-prot\tConvert tRNA sequence to Protein sequence.",
              "  -pt, --prot-trna\tConvert Protein sequence to tRNA sequence.",
              "  -tm, --trna-mrna\tConvert tRNA sequence to mRNA sequence.",
              "  -md, --mrna-dna\tConvert mRNA sequence to DNA sequence.",
              "  -dp, --dna-prot\tConvert DNA sequence to Protein sequence.",
              "  -pd, --prot-dna\tConvert Protein sequence to DNA sequence.\n",
              sep="\n")

    elif sys.argv[1] == '--version' or sys.argv[1] == '-v':
        print(f"seqconvert {VERSION}",
              f"<{URL}>".format(URL),
              f"Copyright (C) 2021 {AUTHOR}\n",
              sep="\n")

    # Failure: Too many arguments.
    elif len(sys.argv) > 3:
        print("ERROR: Too many arguments provided.")
        sys.exit(1)

    # Failure: Not enough arguments.
    elif len(sys.argv) < 3:
        print("ERROR: An option and a sequence must be provided.")
        sys.exit(1)

    # Failure: Target is a directory.
    elif path.isdir(sys.argv[2]):
        print("ERROR: Target is a directory. Please provide a file.")
        sys.exit(1)

    # Failure: Target does not exist.
    elif not path.exists(sys.argv[2]):
        print("ERROR: Target", sys.argv[2], "does not exist.")
        sys.exit(1)

    # Success: Handle '--dna-mrna' argument.
    elif sys.argv[1] == '--dna-mrna' or sys.argv[1] == '-dm':
        seq_convert.dna_to_mrna(sys.argv[2])

    # Success: Handle '--mrna-trna' argument.
    elif sys.argv[1] == '--mrna-trna' or sys.argv[1] == '-mt':
        seq_convert.mrna_to_trna(sys.argv[2])

    # Success: Handle '--trna-protein' argument.
    elif sys.argv[1] == '--trna-prot' or sys.argv[1] == '-tp':
        seq_convert.trna_to_protein(sys.argv[2])

    # Success: Handle '--prot-trna' argument.
    elif sys.argv[1] == '--prot-trna' or sys.argv[1] == '-pt':
        seq_convert.protein_to_trna(sys.argv[2])

    # Success: Handle '--trna-mrna' argument.
    elif sys.argv[1] == '--trna-mrna' or sys.argv[1] == '-tm':
        seq_convert.trna_to_mrna(sys.argv[2])

    # Success: Handle '--mrna-dna' argument.
    elif sys.argv[1] == '--mrna-dna' or sys.argv[1] == '-md':
        seq_convert.mrna_to_dna(sys.argv[2])

    # Success: Handle '--dna-prot' argument.
    elif sys.argv[1] == '--dna-prot' or sys.argv[1] == '-dp':
        seq_convert.dna_to_protein(sys.argv[2])

    # Success: Handle '--prot-dna' argument.
    elif sys.argv[1] == '--prot-dna' or sys.argv[1] == '-pd':
        seq_convert.protein_to_dna(sys.argv[2])

    # Failure: Catch all.
    else:
        print("ERROR: An unknown error occurred.")
        sys.exit(1)

# End of File.
