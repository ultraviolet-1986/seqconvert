#!/usr/bin/env python3

"""
Filename: test_main.py
Author:   William Whinn

Basic unit test file for the main 'seqconvery' class.
"""

###########
# Imports #
###########

import unittest
from os import path
import seqconvert.main as sc

##############
# Unit Tests #
##############

class TestStringMethods(unittest.TestCase):
    """Test cases for the 'seqconvert.py' file."""

    def test_sample_dna_file_exists(self):
        """Assert that the sample file exists."""

        print("Assert that the sample file exists.")

        print(path.exists("test_dna.fas"))

        self.assertTrue(path.exists("test_dna.fas"))


    def test_sample_dna_file_is_fasta(self):
        """Assert that the sample DNA file is in FASTA format."""

        print("Assert that the sample DNA file is in FASTA format.")

        with open("test_dna.fas", encoding="utf-8") as file:
            first_line = file.readline()

        print(first_line)

        self.assertTrue(first_line[0] == '>')


    def test_dna_mrna_results(self):
        """Assert that the results of a conversion mimic known results."""

        print("Assert that the results of a conversion mimic known results.")

        test_sequence = (
            "AAUCAAAACUAACUUACGUUGUCACUUUUUCGCGUGUAUUUGCGUCAUCGAAGUAGAUUU"
            "UUACCUUGUGACUAAAUUCAAAAAACGGACGCACGUUUUCGGAUAUACGCCGGCCGGUGC"
            "GUCGCCGCUCUUAUAUGUUCGCCAGGUUGGUGCGUUAAGAGGCAUCCUCAUUCCUCCGUA"
            "CGCUAGAGAUGUUCUAGCUAUCUCACUAUAGACAUGGGAAUAUACUAAAAAUGGCAAAAC"
            "UGAUGCCCUGGUCCUCACUAGCUCCCGAGUAUCGCACUGCCGGUGUAAAGAUUUGUGUGU"
            "AGAAUUUAGUGGCCAAGACUCAACUCGUUCACUAAUUGGCGCGUGGACCUAGUAACAUGU"
            "UAUCUGCUAGCUUACAAUAGGGGAAAGGCAAGUAAUUCUUAUGCUGGGUAAUUAGUAGAA"
            "GCUAGGCAUAGGGCGUUGGACGACUGACUCAGAUGCGCGAGUGGCUUGAAACCGAAUAUG"
            "AUCGUCAUCAUUUGCCGGUGCUUUACCCUGACUCGAUCACAAUUACGCAUUUAGCAGUGC"
            "UUUUAGAACGACUUUAUGAAUAUAGUAUCGUAGCAUCCGACAUCGCCCAAUACCGUUAUC"
        )

        sequence = sc.SeqConvert.dna_to_mrna(file="test_dna.fas")

        self.assertTrue(sequence == test_sequence)

#############
# Kickstart #
#############

if __name__ == '__main__':
    unittest.main()

# End of File.
