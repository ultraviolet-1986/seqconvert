#!/usr/bin/env python3

"""
Filename: main.py
Author:   William Whinn

Main 'seqconvert' class for converting between sequence types.
"""

###########
# Imports #
###########

import os
import re
import sys

###########
# Classes #
###########

class SeqConvert():
    """Main 'seqconvert' class for converting between sequence types."""

    ########################################
    # CLASS VARIABLES > CODON DICTIONARIES #
    ########################################

    protein_to_codon = {
        'A':['GCU', 'GCC', 'GCA', 'GCG'],                # A / Ala / Alanine
        'C':['UGU', 'UGC'],                              # C / Cys / Cysteine
        'D':['GAU', 'GAC'],                              # D / Asp / Aspartic Acid
        'E':['GAA', 'GAG'],                              # E / Glu / Glutamic Acid
        'F':['UUU', 'UUC'],                              # F / Phe / Phenylalanine
        'G':['GGU', 'GGC', 'GGA', 'GGG'],                # G / Gly / Glycine
        'H':['CAU', 'CAC'],                              # H / His / Histidine
        'I':['AUU','AUC', 'AUA'],                        # I / Ile / Isoleucine
        'K':['AAA', 'AAG'],                              # K / Lys / Lysine
        'L':['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],  # L / Leu / Leucine
        'M':['AUG'],                                     # M / Met / Methionine
        'N':['AAU', 'AAC'],                              # N / Asn / Asparagine
        'P':['CCU', 'CCC', 'CCA', 'CCG'],                # P / Pro / Proline
        'Q':['CAA', 'CAG'],                              # Q / Gln / Glutamine
        'R':['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],  # R / Arg / Arginine
        'S':['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],  # S / Ser / Serine
        'T':['ACU', 'ACC', 'ACA', 'ACG'],                # T / Thr / Threonine
        'V':['GUU', 'GUC', 'GUA', 'GUG'],                # V / Val / Valine
        'W':['UGG'],                                     # W / Trp / Tryptophan
        'Y':['UAU', 'UAC'],                              # Y / Tyr / Tyrosine
        '*':['UAA', 'UAG', 'UGA']                        # Stop Codon
    }

    codon_to_protein = {}
    for key, value in protein_to_codon.items():
        for val in value:
            if val in codon_to_protein:
                codon_to_protein[val].append(key)
            else:
                codon_to_protein[val] = [key]


    ########################################
    # CLASS METHODS > CLASS INITIALISATION #
    ########################################

    def __init__(self, sequence="undefined"):
        """Initialisation class for 'seqconvert' program."""
        self.sequence = sequence


    ####################################
    # PUBLIC METHODS > FILE MANAGEMENT #
    ####################################

    def read_fasta_file(self, file):
        """Read a FASTA file and return the contained sequence as a string."""

        with open (file, encoding="utf-8") as fasta_file:
            header = fasta_file.readline()

        if header[0] == '>':
            with open(file, 'r', encoding='utf-8') as fasta_file:
                sequence = fasta_file.readlines()

            sequence.pop(0)
            sequence = ''.join(sequence)
            sequence = sequence.replace('\n', '')

            self.sequence = sequence
            return sequence

        print("ERROR: File does not appear to be FASTA format.")
        sys.exit(1)


    def write_fasta_file(self, file, suffix, contents):
        """Write a FASTA-formatted sequence to file."""

        # PyLint Directives
        # pylint: disable=no-self-use

        filename, extension = os.path.splitext(file)

        out_file = f"{filename}_({suffix}){extension}"

        with open(out_file, 'w+', encoding='utf-8') as fasta_file:
            fasta_file.write(contents)
            fasta_file.close()

        print(f"\nSUCCESS: Sequence written to '{out_file}'.")


    ##############################################################
    # PRIVATE METHODS > SINGLE-STEP SEQUENCE FORWARDS CONVERSION #
    ##############################################################

    def __dna_to_mrna(self, sequence):
        """Convert DNA sequence to mRNA sequence."""

        dna_bases = {
            'A':'0', 'T':'1', 'G':'2', 'C':'3',
            'a':'4', 't':'5', 'g':'6', 'c':'7'
        }

        mrna_bases = {
            'A':'1', 'U':'0', 'G':'3', 'C':'2',
            'a':'5', 'u':'4', 'g':'7', 'c':'6'
        }

        for key, value in dna_bases.items():
            sequence = sequence.replace(key, value)

        for key, value in mrna_bases.items():
            sequence = sequence.replace(value, key)

        self.sequence = sequence
        return self.sequence


    def __xrna_to_xrna(self, sequence):
        """Convert mRNA sequence to tRNA sequence."""

        bases_1 = {
            'A':'0', 'U':'1', 'G':'2', 'C':'3',
            'a':'4', 'u':'5', 'g':'6', 'c':'7'
        }

        bases_2 = {
            'A':'1', 'U':'0', 'G':'3', 'C':'2',
            'a':'5', 'u':'4', 'g':'7','c':'6'
        }

        for key, value in bases_1.items():
            sequence = sequence.replace(key, value)

        for key, value in bases_2.items():
            sequence = sequence.replace(value, key)

        self.sequence = sequence
        return self.sequence


    def __trna_to_protein(self, sequence):
        """Convert tRNA sequence to Protein sequence."""

        split_codons = []
        codon = 3

        for index in range(0, len(sequence), codon):
            split_codons.append(sequence[index : index + codon])

        sequence = ''
        for i in split_codons:
            sequence += str(self.codon_to_protein[i][0])

        self.sequence = sequence
        return self.sequence


    ###############################################################
    # PRIVATE METHODS > SINGLE-STEP SEQUENCE BACKWARDS CONVERSION #
    ###############################################################

    def __protein_to_trna(self, sequence):
        """Convert Protein sequence to tRNA sequence."""

        # PyLint Directives
        # pylint: disable=unused-private-member

        # TODO: Placeholder method. Insert conversion code here.

        self.sequence = sequence
        return self.sequence


    def __trna_to_mrna(self, sequence):
        """Convert tRNA sequence to mRNA sequence."""

        # PyLint Directives
        # pylint: disable=unused-private-member

        # TODO: Placeholder method. Insert conversion code here.

        self.sequence = sequence
        return self.sequence


    def __mrna_to_dna(self, sequence):
        """Convert mRNA sequence to DNA sequence."""

        # PyLint Directives
        # pylint: disable=unused-private-member

        # TODO: Placeholder method. Insert conversion code here.

        self.sequence = sequence
        return self.sequence


    #############################################################
    # PUBLIC METHODS > SINGLE-STEP SEQUENCE FORWARDS CONVERSION #
    #############################################################

    def dna_to_mrna(self, file):
        """Convert DNA sequence to mRNA sequence."""

        header = "> seqconvert.py | DNA > mRNA Translation\n"
        suffix = "DNA-mRNA"

        sequence = self.read_fasta_file(file)
        sequence = self.__dna_to_mrna(sequence)

        contents = re.sub("(.{60})", "\\1\n", sequence, 0, re.DOTALL)
        contents = header + contents

        print(contents)
        self.write_fasta_file(file, suffix, contents)

        return sequence


    def mrna_to_trna(self, file):
        """Convert mRNA sequence to tRNA sequence."""

        header = "> seqconvert.py | mRNA > tRNA Translation\n"
        suffix = "mRNA-tRNA"

        sequence = self.read_fasta_file(file)
        sequence = self.__xrna_to_xrna(sequence)

        contents = re.sub("(.{60})", "\\1\n", sequence, 0, re.DOTALL)
        contents = header + contents

        print(contents)
        self.write_fasta_file(file, suffix, contents)

        return sequence


    def trna_to_protein(self, file):
        """Convert tRNA sequence to Protein sequence."""

        header = "> seqconvert.py | tRNA > Protein Translation\n"
        suffix = "tRNA-Protein"

        sequence = self.read_fasta_file(file)
        sequence = self.__trna_to_protein(sequence)

        contents = re.sub("(.{60})", "\\1\n", sequence, 0, re.DOTALL)

        contents = header + contents

        print(contents)
        self.write_fasta_file(file, suffix, contents)

        return sequence


    ##############################################################
    # PUBLIC METHODS > SINGLE-STEP SEQUENCE BACKWARDS CONVERSION #
    ##############################################################

    def protein_to_trna(self, file):
        """Convert Protein sequence to tRNA sequence."""

        header = "> seqconvert.py | Protein > tRNA Translation\n"
        suffix = "Protein-tRNA"

        sequence = self.read_fasta_file(file)
        sequence = self.__protein_to_trna(sequence)

        sequence = re.sub("(.{60})", "\\1\n", sequence, 0, re.DOTALL)
        contents = header + sequence

        print(contents)
        self.write_fasta_file(file, suffix, contents)

        return sequence


    def trna_to_mrna(self, file):
        """Convert tRNA sequence to mRNA sequence."""

        header = "> seqconvert.py | tRNA > mRNA Translation\n"
        suffix = "tRNA-mRNA"

        sequence = self.read_fasta_file(file)
        sequence = self.__xrna_to_xrna(sequence)

        sequence = re.sub("(.{60})", "\\1\n", sequence, 0, re.DOTALL)
        contents = header + sequence

        print(contents)
        self.write_fasta_file(file, suffix, contents)

        return sequence


    def mrna_to_dna(self, file):
        """Convert mRNA sequence to DNA sequence."""

        header = "> seqconvert.py | mRNA > DNA Translation\n"
        suffix = "mRNA-DNA"

        sequence = self.read_fasta_file(file)
        sequence = self.__mrna_to_dna(sequence)

        contents = re.sub("(.{60})", "\\1\n", sequence, 0, re.DOTALL)
        contents = header + sequence

        print(contents)
        self.write_fasta_file(file, suffix, contents)

        return sequence


    #######################################################
    # MULTIPLE-STEP CONVERSION FUNCTIONS > PUBLIC METHODS #
    #######################################################

    def dna_to_protein(self, file):
        """Convert DNA sequence to Protein sequence."""

        header = "> seqconvert.py | DNA > Protein Translation\n"
        suffix = "DNA-Protein"

        sequence = self.read_fasta_file(file)

        sequence = self.__dna_to_mrna(sequence)
        sequence = self.__xrna_to_xrna(sequence)
        sequence = self.__trna_to_protein(sequence)

        sequence = re.sub("(.{60})", "\\1\n", sequence, 0, re.DOTALL)

        contents = header + sequence

        print(contents)
        self.write_fasta_file(file, suffix, contents)

        return sequence


    def protein_to_dna(self, file):
        """Convert Protein sequence to DNA sequence."""

        header = "> seqconvert.py | Protein > DNA Translation\n"
        suffix = "Protein-DNA"

        sequence = self.read_fasta_file(file)

        sequence = self.__protein_to_trna(sequence)
        sequence = self.__trna_to_mrna(sequence)
        sequence = self.__mrna_to_dna(sequence)

        sequence = re.sub("(.{60})", "\\1\n", sequence, 0, re.DOTALL)
        contents = header + sequence

        print(contents)
        self.write_fasta_file(file, suffix, contents)

        return sequence


# End of File.
