#!/usr/bin/env bash

############
# Metadata #
############

# Author: William Whinn
# File Name: test_seqconvert.sh

#############
# Variables #
#############

# Constants

SEQCONVERT_ROOT="$( cd "$(dirname "${BASH_SOURCE[0]}")" && pwd )"
readonly SEQCONVERT_ROOT

#############
# Functions #
#############

run_seqconvert_unit_tests(){
  # Check for Python 3 installation.
  if ( ! command -v 'python3' > /dev/null ) ; then
    echo "ERROR: Python 3 was not detected."

    # End program and return failure code.
    return 1
  fi

  # Perform unit tests for each detected Python unit test file.
  for f in "$SEQCONVERT_ROOT"/test_*.py; do
    if [ -f "$f" ] ; then
      python3 "$f"
      echo
    fi
  done

  # End program and return success code.
  return 0
}

#############
# Kickstart #
#############

run_seqconvert_unit_tests

# End of File.
