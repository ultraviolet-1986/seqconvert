#!/usr/bin/env python3

"""
Filename: main.py
Author:   William Whinn

Main 'seqconvert' class for converting between sequence types.
"""

###########
# Imports #
###########

import re
import os
import sys

###########
# Classes #
###########

class SeqConvert():
    """Main 'seqconvert' class for converting between sequence types."""

    # CLASS VARIABLES > CODON DICTIONARIES

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


    # CLASS METHODS > CLASS INITIALISATION

    def __init__(self, sequence="undefined"):
        """Initialisation class for 'seqconvert' program."""
        self.sequence = sequence


    # PUBLIC METHODS > FILE MANAGEMENT

    def read_fasta_file(self, file):
        """Read a FASTA file and return its xNA sequence as a string."""

        with open (file, encoding="utf-8") as fasta_file:
            header = fasta_file.readline()

        if header[0] == '>':
            with open(file, 'r', encoding='utf-8') as fasta_file:
                sequence = fasta_file.readlines()

            sequence.pop(0)
            sequence = ''.join(sequence)
            sequence = sequence.replace('\n', '')

            return self.sequence

        print("ERROR: File does not appear to be FASTA format.")
        sys.exit(1)


    def write_fasta_file(self, file, contents):
        """Write a FASTA-formatted sequence to file."""

        # PyLint Directives
        # pylint: disable=no-self-use

        filename, extension = os.path.splitext(file)

        out_file = f"{filename} (converted){extension}"

        with open(out_file, 'w+', encoding='utf-8') as fasta_file:
            fasta_file.write(contents)
            fasta_file.close()

        print(f"\nSUCCESS: Sequence written to '{out_file}'.")


    # PUBLIC METHODS > SINGLE-STEP SEQUENCE CONVERSION

    def dna_to_mrna(self, file):
        """Convert DNA sequence to mRNA sequence."""

        header = "> seqconvert.py | DNA > mRNA Translation\n"

        sequence = self.read_fasta_file(file)

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

        contents = re.sub("(.{60})", "\\1\n", sequence, 0, re.DOTALL)
        contents = header + contents

        print(contents)

        self.write_fasta_file(file, contents)

        return contents


    def mrna_to_trna(self, file):
        """Convert mRNA sequence to tRNA sequence."""

        header = "> seqconvert.py | mRNA > tRNA Translation\n"

        sequence = self.read_fasta_file(file)

        mrna_bases = {
            'A':'0', 'U':'1', 'G':'2', 'C':'3',
            'a':'4', 'u':'5', 'g':'6', 'c':'7'
        }

        trna_bases = {
            'A':'1', 'U':'0', 'G':'3', 'C':'2',
            'a':'5', 'u':'4', 'g':'7','c':'6'
        }

        for key, value in mrna_bases.items():
            sequence = sequence.replace(key, value)

        for key, value in trna_bases.items():
            sequence = sequence.replace(value, key)

        contents = re.sub("(.{60})", "\\1\n", sequence, 0, re.DOTALL)
        contents = header + contents

        print(contents)

        self.write_fasta_file(file, contents)

        return contents


    def trna_to_protein(self, file):
        """Convert tRNA sequence to Protein sequence."""

        header = "> seqconvert.py | tRNA > Protein Translation\n"

        sequence = self.read_fasta_file(file)

        split_codons = []
        codon = 3

        for index in range(0, len(sequence), codon):
            split_codons.append(sequence[index : index + codon])

        string = ''
        for i in split_codons:
            string += str(self.codon_to_protein[i][0])

        contents = re.sub("(.{60})", "\\1\n", string, 0, re.DOTALL)

        contents = header + contents

        print(contents)

        self.write_fasta_file(file, contents)

        return contents


    def protein_to_trna(self, sequence):
        """Convert Protein sequence to tRNA sequence."""

        # Define FASTA header.
        header = "> seqconvert.py | Protein > tRNA Translation\n"

        # Read data from the given file 'sequence' into the variable
        # 'contents'.
        contents = self.read_fasta_file(sequence)

        # TODO INSERT CONVERSION CODE HERE

        # Format sequence to 60-columns FASTA-style.
        contents = re.sub("(.{60})", "\\1\n", contents, 0, re.DOTALL)

        # Insert FASTA header to mRNA sequence.
        contents = header + contents

        # Print translated sequence.
        print(contents)

        # Write updated version of 'contents' to a new file.
        self.write_fasta_file(sequence, contents)

        # Return translated sequence.
        return contents


    def trna_to_mrna(self, sequence):
        """Convert tRNA sequence to mRNA sequence."""

        # Define FASTA header.
        header = "> seqconvert.py | tRNA > mRNA Translation\n"

        # Read data from the given file 'sequence' into the variable
        # 'contents'.
        contents = self.read_fasta_file(sequence)

        # TODO INSERT CONVERSION CODE HERE

        # Format sequence to 60-columns FASTA-style.
        contents = re.sub("(.{60})", "\\1\n", contents, 0, re.DOTALL)

        # Insert FASTA header to mRNA sequence.
        contents = header + contents

        # Print translated sequence.
        print(contents)

        # Write updated version of 'contents' to a new file.
        self.write_fasta_file(sequence, contents)

        # Return translated sequence.
        return contents


    def mrna_to_dna(self, sequence):
        """Convert mRNA sequence to DNA sequence."""

        # Define FASTA header.
        header = "> seqconvert.py | mRNA > DNA Translation\n"

        # Read data from the given file 'sequence' into the variable
        # 'contents'.
        contents = self.read_fasta_file(sequence)

        # TODO INSERT CONVERSION CODE HERE

        # Format sequence to 60-columns FASTA-style.
        contents = re.sub("(.{60})", "\\1\n", contents, 0, re.DOTALL)

        # Insert FASTA header to mRNA sequence.
        contents = header + contents

        # Print translated sequence.
        print(contents)

        # Write updated version of 'contents' to a new file.
        self.write_fasta_file(sequence, contents)

        # Return translated sequence.
        return contents


    # MULTIPLE-STEP CONVERSION FUNCTIONS > PUBLIC METHODS

    def dna_to_protein(self, sequence):
        """Convert DNA sequence to Protein sequence."""

        # Define FASTA header.
        header = "> seqconvert.py | DNA > Protein Translation\n"

        # Read data from the given file 'sequence' into the variable
        # 'contents'.
        contents = self.read_fasta_file(sequence)

        # TODO INSERT CONVERSION CODE HERE

        # Format sequence to 60-columns FASTA-style.
        contents = re.sub("(.{60})", "\\1\n", contents, 0, re.DOTALL)

        # Insert FASTA header to mRNA sequence.
        contents = header + contents

        # Print translated sequence.
        print(contents)

        # Write updated version of 'contents' to a new file.
        self.write_fasta_file(sequence, contents)

        # Return translated sequence.
        return contents


    def protein_to_dna(self, sequence):
        """Convert Protein sequence to DNA sequence."""

        # Define FASTA header.
        header = "> seqconvert.py | Protein > DNA Translation\n"

        # Read data from the given file 'sequence' into the variable
        # 'contents'.
        contents = self.read_fasta_file(sequence)

        # TODO INSERT CONVERSION CODE HERE

        # Format sequence to 60-columns FASTA-style.
        contents = re.sub("(.{60})", "\\1\n", contents, 0, re.DOTALL)

        # Insert FASTA header to mRNA sequence.
        contents = header + contents

        # Print translated sequence.
        print(contents)

        # Write updated version of 'contents' to a new file.
        self.write_fasta_file(sequence, contents)

        # Return translated sequence.
        return contents


# End of File.
