# seqconvert

A Python application for converting DNA to RNA to Protein in multiple
combinations.

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Unit Testing](#unit-testing)
- [Functionality](#functionality)
- [Project Submission Status](#project-submission-status)

## Introduction

The intent of this project is to create an unbiased nucleotide/protein sequence
converter which uses minimal libraries and is fully-compatible with FASTA format
files.

Once a sequence has been converted, it should be possible to identify the result
using other tools such as BLAST, LOMETS, PSIPRED, etc.

## Usage

By default, `seqconvert` must be given an option and a file-name. All options
available for use may be seen below:

```bash
# Print help information and exit.
python3 seqconvert.py -h
python3 seqconvert.py --help

# Print version information and exit.
python3 seqconvert.py -v
python3 seqconvert.py --version

# Convert a DNA sequence to an mRNA sequence.
python3 seqconvert.py -dm "<FILENAME>"
python3 seqconvert.py --dna-mrna "<FILENAME>"

# Convert an mRNA sequence to a tRNA sequence.
python3 seqconvert.py -mt "<FILENAME>"
python3 seqconvert.py --mrna-trna "<FILENAME>"

# Convert an tRNA sequence to a Protein sequence.
python3 seqconvert.py -tp "<FILENAME>"
python3 seqconvert.py --trna-prot "<FILENAME>"

# Convert a Protein sequence to a tRNA sequence.
python3 seqconvert.py -pt "<FILENAME>"
python3 seqconvert.py --prot-trna "<FILENAME>"

# Convert a tRNA sequence to a mRNA sequence.
python3 seqconvert.py -tm "<FILENAME>"
python3 seqconvert.py --trna-mrna "<FILENAME>"

# Convert an mRNA sequence to a DNA sequence.
python3 seqconvert.py -md "<FILENAME>"
python3 seqconvert.py --mrna-dna "<FILENAME>"

# Directly convert a DNA sequence to a Protein sequence.
python3 seqconvert.py -dp "<FILENAME>"
python3 seqconvert.py --dna-prot "<FILENAME>"

# Directly convert a Protein sequence to a DNA sequence.
python3 seqconvert.py -pd "<FILENAME>"
python3 seqconvert.py --prot-dna "<FILENAME>"
```

For basic testing, a randomly-generated file `test_dna.fas` is included and this
can be converted to `mRNA` by using the following command:

```bash
python3 seqconvert.py --dna-mrna "test_dna.fas"
```

`seqconvert` will create a new file called `test_dna-converted.fas`, which can
be converted to `tRNA` by using the following command:

```bash
python3 seqconvert.py --mrna-trna "test_dna-converted.fas"
```

The user should name their files manually to identify them correctly at each
step of the process so that sequences will not be erroneously converted.

## Unit Testing

A test script named `test_seqconvert.sh` is included within this repository, it
will detect and execute any and all Python scripts which contain a filename
beginning with `test_` and ending with a `.py` extension. At present, these unit
tests are basic, but show that it is possible to test from the project's root
directory. The testing script can be launched with the following command:

```bash
bash test_seqconvert.sh
```

## Functionality

Although this program cannot determine whether or not a sequence is `DNA`,
`mRNA` etc., `seqconvert` can take a sequence from a FASTA file for processing
and output the results in FASTA format to a new file.

At present, FASTA file validation is discovered by scanning the first line of a
file, and checking that the first character is a `>` character. Processed
sequences will have the string `-converted` appended to the filename, leaving
the file extension intact.

During conversion for `DNA`, `mRNA`, and `tRNA`, each of these bases are
translated to a number so that conversion can be completed without creating
duplicate base entries within the sequence.

## Project Submission Status

Because of the assignment restriction of approximately 500 total lines of code,
the following functionality is not completely implemented (but planned for
future versions):

- tRNA > Protein Conversion.
- Protein > tRNA Conversion.
- tRNA > mRNA Conversion.
- mRNA > DNA Conversion.
- DNA > Protein Conversion.
- Protein > DNA Conversion.
- Public/Private class method implementation.
- Output testing with BLAST.

At present, the following functionality is implemented and as stable as possible
within the assignment time limit.

- Argument validation using `sys.argv` instead of `argparse` so arguments could
  perform function calls directly.
- Completed help argument.
- Completed version argument.
- Project metadata stored as variables within the `cli.py` file.
- DNA > mRNA Conversion.
- mRNA > tRNA Conversion.
- Detect whether or not a file exists.
- Detect whether or not a file is in FASTA format.
- Break down the contents of a file into a single string for processing and
  sequence conversion, stripping the FASTA header.
- Create a FASTA format output file from the results generated at the standard
  length of 60 columns.
- Unit testing files for both `main.py` and `cli.py` within the `seqconvert`
  project directory.
