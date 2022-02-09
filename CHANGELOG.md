# Changelog

## Table of Contents

- [Version 0.0.2](#version-002)
- [University Version 0.0.1](#university-version-001)

## Version 0.0.2

- To be available at <https://github.com/ultraviolet-1986/seqconvert> after the
  submission deadline.

## University Version 0.0.1

- **Thursday, 11th February 2021**
  - Began project on Newcastle University GitLab instance as part of CSC8330
    Assignment 2.
  - Removed `argparse` to favour `sys.argv` for better function execution.

- **Friday, 12th February 2021**
  - Began the process of including file-handling.
  - Managed to write a sequence to a given file.

- **Saturday, 13th February 2021**
  - Began scaffolding the unit testing files.
  - Introduced the `DNA > mRNA > tRNA > Protein` process.
  - Corrected argument flags in all locations where they are present.
  - Included DNA to mRNA to tRNA conversion.
  - Corrected filename management.
  - Created boilerplate code for other conversion functions. It should be
    possible to include conversion code at specific locations and have the
    results written to the renamed file.
  - Included primitive check that the file is FASTA format. Note that it does
    not check the file extension for validation, only the first character being
    `>`.
  - Updated documentation.
  - Began tidying for submission because of total program lines.
  - Implemented basic unit testing.
