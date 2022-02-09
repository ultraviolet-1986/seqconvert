#!/usr/bin/env python3

"""
Filename: test_cli.py
Author:   William Whinn

Basic unit test file for the Command-line interface.
"""

###########
# Imports #
###########

import unittest
from os import path
from seqconvert import cli

##############
# Unit Tests #
##############

class TestStringMethods(unittest.TestCase):
    """Test cases for the 'cli.py' file."""

    def test_version_number(self):
        """Assert that the 'VERSION' variable equals '0.0.1'."""
        print("Assert that the 'VERSION' variable equals '0.0.1'.")
        print(cli.VERSION)
        self.assertTrue(cli.VERSION, '0.0.1')


    def test_sample_dna_file_exists(self):
        """Assert that the sample file exists."""
        print("Assert that the sample file exists.")
        print(path.exists("test_dna.fas"))
        self.assertTrue(path.exists("test_dna.fas"))


#############
# Kickstart #
#############

if __name__ == '__main__':
    unittest.main()

# End of File.
