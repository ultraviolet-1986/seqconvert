#!/usr/bin/env python3

"""
Filename: seqconvert.py
Author:   William Whinn

Convert DNA to RNA to Protein in multiple combinations.

Usage: seqconvert.py [OPTION] [SEQUENCE]

Arguments:
  -h --help\t\tDisplay this help and exit.
  -v --version\t\tDisplay version information and exit.

  -dm --dna-mrna\tConvert DNA sequence to mRNA sequence.
  -mt --mrna-trna\tConvert mRNA sequence to tRNA sequence.
  -tp --trna-prot\tConvert tRNA sequence to Protein sequence.
  -pt --prot-trna\tConvert Protein sequence to tRNA sequence.
  -tm --trna-mrna\tConvert tRNA sequence to mRNA sequence.
  -rd --rna-dna\tConvert mRNA sequence to DNA sequence.
  -dp --dna-prot\tConvert DNA sequence to Protein sequence.
  -pd --prot-dna\tConvert Protein sequence to DNA sequence.
"""

##########
# Import #
##########

from seqconvert.cli import cli

#############
# Kickstart #
#############

if __name__ == '__main__':
    cli()

# End of File.
