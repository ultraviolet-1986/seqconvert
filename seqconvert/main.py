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

    # PyLint Directives
    # pylint: disable=no-self-use

    # PyLint Notes
    # - File handling may be converted to function instead of method in
    #   a future release. Disable warning temporarily.
    # - TODOs are left intact to help highlight where code needs to be
    #   changed in the next planned version of this software.

    # CLASS INITIALISATION METHOD

    def __init__(self, sequence="undefined"):
        """Initialisation class for 'seqconvert' program."""
        self.sequence = sequence


    # FILE HANDLING AND FORMATTING METHODS > TO MAKE PRIVATE

    def read_from_file(self, sequence):
        """Read a sequence from a specified file."""

        # PyLint Directives
        # pylint: disable=no-else-return

        # PyLint Notes
        # - This directive is a false positive as each condition is met
        #   regardless of the inclusion of 'return'.

        # Read first line of the sequence file.
        with open(sequence) as file:
            first_line = file.readline()

        # Check that first character of first line is '>'.
        # Primitive FASTA file check.
        if first_line[0] == '>':
            # Parse the 'sequence' file to generate output.
            with open(sequence , 'r') as file:
                output = file.readlines()

            # Remove index line from 'output'.
            output.pop(0)

            # Convert the contents of the file to a single string.
            output = ''.join(output)

            # Remove all newline characters.
            output = output.replace('\n', '')

            # Return the output.
            return output

        else:
            print("ERROR: File does not appear to be in FASTA format.")
            sys.exit(1)


    def write_to_file(self, sequence, contents):
        """Write a sequence to a specified file."""

        # Find filename extension.
        filename, extension = os.path.splitext(sequence)

        # Construct new filename.
        sequence = filename + "-converted" + extension

        # Write results to file.
        output = open(sequence, 'w+')
        output.write(contents)
        output.close()

        # Print status.
        print("\nSUCCESS: Sequence written to '", sequence, "'.", sep='')


    # SINGLE-STEP CONVERSION FUNCTIONS > PUBLIC METHODS

    def dna_to_mrna(self, sequence):
        """Convert DNA sequence to mRNA sequence."""

        # Define FASTA header.
        header = "> seqconvert.py | DNA > mRNA Translation\n"

        # Read data from the given file 'sequence' into the variable
        # 'contents'.
        contents = self.read_from_file(sequence)

        # TODO Replace swapping mechanism to use dictionary.
        # TODO Research means of swapping between two dictionaries.
        bases = {
            'A':'0', 'T':'1', 'G':'2', 'C':'3', 'U':'4',
            'a':'5', 't':'6', 'g':'7', 'c':'8', 'u':'9'
        }

        bases_swap = {value:key for key, value in bases.items()}

        # Substitution Bases.
        base_1 = '1'  # Adenine
        base_2 = '2'  # Thymine
        base_3 = '3'  # Guanine
        base_4 = '4'  # Cytosine
        base_5 = '5'  # Adenine (lower case)
        base_6 = '6'  # Thymine (lower case)
        base_7 = '7'  # Guanine (lower case)
        base_8 = '8'  # Cytosine (lower case)

        # DNA/RNA Bases.
        upper_adenine = 'A'   # Base 1
        upper_thymine = 'T'   # Base 2
        upper_guanine = 'G'   # Base 3
        upper_cytosine = 'C'  # Base 4
        upper_uracil = 'U'    # Base 5

        lower_adenine = 'a'   # Base 1
        lower_thymine = 't'   # Base 2
        lower_guanine = 'g'   # Base 3
        lower_cytosine = 'c'  # Base 4
        lower_uracil = 'u'    # Base 5

        # Replace DNA Bases with substitution string.
        contents = contents.replace(upper_adenine, base_1)   # A > 1
        contents = contents.replace(upper_thymine, base_2)   # T > 2
        contents = contents.replace(upper_guanine, base_3)   # G > 3
        contents = contents.replace(upper_cytosine, base_4)  # C > 4

        contents = contents.replace(lower_adenine, base_5)   # a > 5
        contents = contents.replace(lower_thymine, base_6)   # t > 6
        contents = contents.replace(lower_guanine, base_7)   # g > 7
        contents = contents.replace(lower_cytosine, base_8)  # c > 8

        # Replace substitution string with mRNA bases.
        contents = contents.replace(base_1, upper_uracil)    # 1 > U
        contents = contents.replace(base_2, upper_adenine)   # 2 > A
        contents = contents.replace(base_3, upper_cytosine)  # 3 > C
        contents = contents.replace(base_4, upper_guanine)   # 4 > G

        contents = contents.replace(base_5, lower_uracil)    # 1 > u
        contents = contents.replace(base_6, lower_adenine)   # 2 > a
        contents = contents.replace(base_7, lower_cytosine)  # 3 > c
        contents = contents.replace(base_8, lower_guanine)   # 4 > g

        # Format sequence to 60-columns FASTA-style.
        contents = re.sub("(.{60})", "\\1\n", contents, 0, re.DOTALL)

        # Insert FASTA header to mRNA sequence.
        contents = header + contents

        # Print translated sequence.
        print(contents)

        # Write updated version of 'contents' to a new file.
        self.write_to_file(sequence, contents)

        # Return translated sequence.
        return contents


    def mrna_to_trna(self, sequence):
        """Convert mRNA sequence to tRNA sequence."""

        # Define FASTA header.
        header = "> seqconvert.py | mRNA > tRNA Translation\n"

        # Read data from the given file 'sequence' into the variable
        # 'contents'.
        contents = self.read_from_file(sequence)

        # Substitution Bases.
        base_1 = '1'  # Adenine
        base_2 = '2'  # Uracil
        base_3 = '3'  # Guanine
        base_4 = '4'  # Cytosine

        # RNA Bases.
        adenine = 'A'   # Base 1
        uracil = 'U'    # Base 2
        guanine = 'G'   # Base 3
        cytosine = 'C'  # Base 4

        # Replace mRNA Bases with substitution string.
        contents = contents.replace(adenine, base_1)   # A > 1
        contents = contents.replace(uracil, base_2)    # U > 2
        contents = contents.replace(guanine, base_3)   # G > 3
        contents = contents.replace(cytosine, base_4)  # C > 4

        # Replace substitution string with tRNA bases.
        contents = contents.replace(base_1, uracil)    # 1 > U
        contents = contents.replace(base_2, adenine)   # 2 > A
        contents = contents.replace(base_3, cytosine)  # 3 > C
        contents = contents.replace(base_4, guanine)   # 4 > G

        # Format sequence to 60-columns FASTA-style.
        contents = re.sub("(.{60})", "\\1\n", contents, 0, re.DOTALL)

        # Insert FASTA header to mRNA sequence.
        contents = header + contents

        # Print translated sequence.
        print(contents)

        # Write updated version of 'contents' to a new file.
        self.write_to_file(sequence, contents)

        # Return translated sequence.
        return contents


    def trna_to_protein(self, sequence):
        """Convert tRNA sequence to Protein sequence."""

        # Define FASTA header.
        header = "> seqconvert.py | tRNA > Protein Translation\n"

        # Read data from the given file 'sequence' into the variable
        # 'contents'.
        contents = self.read_from_file(sequence)

        # TODO INSERT CONVERSION CODE HERE

        # Format sequence to 60-columns FASTA-style.
        contents = re.sub("(.{60})", "\\1\n", contents, 0, re.DOTALL)

        # Insert FASTA header to mRNA sequence.
        contents = header + contents

        # Print translated sequence.
        print(contents)

        # Write updated version of 'contents' to a new file.
        self.write_to_file(sequence, contents)

        # Return translated sequence.
        return contents


    def protein_to_trna(self, sequence):
        """Convert Protein sequence to tRNA sequence."""

        # Define FASTA header.
        header = "> seqconvert.py | Protein > tRNA Translation\n"

        # Read data from the given file 'sequence' into the variable
        # 'contents'.
        contents = self.read_from_file(sequence)

        # TODO INSERT CONVERSION CODE HERE

        # Format sequence to 60-columns FASTA-style.
        contents = re.sub("(.{60})", "\\1\n", contents, 0, re.DOTALL)

        # Insert FASTA header to mRNA sequence.
        contents = header + contents

        # Print translated sequence.
        print(contents)

        # Write updated version of 'contents' to a new file.
        self.write_to_file(sequence, contents)

        # Return translated sequence.
        return contents


    def trna_to_mrna(self, sequence):
        """Convert tRNA sequence to mRNA sequence."""

        # Define FASTA header.
        header = "> seqconvert.py | tRNA > mRNA Translation\n"

        # Read data from the given file 'sequence' into the variable
        # 'contents'.
        contents = self.read_from_file(sequence)

        # TODO INSERT CONVERSION CODE HERE

        # Format sequence to 60-columns FASTA-style.
        contents = re.sub("(.{60})", "\\1\n", contents, 0, re.DOTALL)

        # Insert FASTA header to mRNA sequence.
        contents = header + contents

        # Print translated sequence.
        print(contents)

        # Write updated version of 'contents' to a new file.
        self.write_to_file(sequence, contents)

        # Return translated sequence.
        return contents


    def mrna_to_dna(self, sequence):
        """Convert mRNA sequence to DNA sequence."""

        # Define FASTA header.
        header = "> seqconvert.py | mRNA > DNA Translation\n"

        # Read data from the given file 'sequence' into the variable
        # 'contents'.
        contents = self.read_from_file(sequence)

        # TODO INSERT CONVERSION CODE HERE

        # Format sequence to 60-columns FASTA-style.
        contents = re.sub("(.{60})", "\\1\n", contents, 0, re.DOTALL)

        # Insert FASTA header to mRNA sequence.
        contents = header + contents

        # Print translated sequence.
        print(contents)

        # Write updated version of 'contents' to a new file.
        self.write_to_file(sequence, contents)

        # Return translated sequence.
        return contents


    # MULTIPLE-STEP CONVERSION FUNCTIONS > PUBLIC METHODS

    def dna_to_protein(self, sequence):
        """Convert DNA sequence to Protein sequence."""

        # Define FASTA header.
        header = "> seqconvert.py | DNA > Protein Translation\n"

        # Read data from the given file 'sequence' into the variable
        # 'contents'.
        contents = self.read_from_file(sequence)

        # TODO INSERT CONVERSION CODE HERE

        # Format sequence to 60-columns FASTA-style.
        contents = re.sub("(.{60})", "\\1\n", contents, 0, re.DOTALL)

        # Insert FASTA header to mRNA sequence.
        contents = header + contents

        # Print translated sequence.
        print(contents)

        # Write updated version of 'contents' to a new file.
        self.write_to_file(sequence, contents)

        # Return translated sequence.
        return contents


    def protein_to_dna(self, sequence):
        """Convert Protein sequence to DNA sequence."""

        # Define FASTA header.
        header = "> seqconvert.py | Protein > DNA Translation\n"

        # Read data from the given file 'sequence' into the variable
        # 'contents'.
        contents = self.read_from_file(sequence)

        # TODO INSERT CONVERSION CODE HERE

        # Format sequence to 60-columns FASTA-style.
        contents = re.sub("(.{60})", "\\1\n", contents, 0, re.DOTALL)

        # Insert FASTA header to mRNA sequence.
        contents = header + contents

        # Print translated sequence.
        print(contents)

        # Write updated version of 'contents' to a new file.
        self.write_to_file(sequence, contents)

        # Return translated sequence.
        return contents


# End of File.
