#!/usr/bin/env python3

"""
Filename: rna_codon_table.py
Author:   William Whinn

RNA Codon table for translating tRNA into Protein and back again.
"""

DICT_PROTEIN_TO_CODON = {
    'A':['GCU', 'GCC', 'GCA', 'GCG'],                  # A / Ala / Alanine
    'C':['UGU', 'UGC'],                                # C / Cys / Cysteine
    'D':['GAU', 'GAC'],                                # D / Asp / Aspartic Acid
    'E':['GAA', 'GAG'],                                # E / Glu / Glutamic Acid
    'F':['UUU', 'UUC'],                                # F / Phe / Phenylalanine
    'G':['GGU', 'GGC', 'GGA', 'GGG'],                  # G / Gly / Glycine
    'H':['CAU', 'CAC'],                                # H / His / Histidine
    'I':['AUU','AUC', 'AUA'],                          # I / Ile / Isoleucine
    'K':['AAA', 'AAG'],                                # K / Lys / Lysine
    'L':['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],    # L / Leu / Leucine
    'M':['AUG'],                                       # M / Met / Methionine
    'N':['AAU', 'AAC'],                                # N / Asn / Asparagine
    'P':['CCU', 'CCC', 'CCA', 'CCG'],                  # P / Pro / Proline
    'Q':['CAA', 'CAG'],                                # Q / Gln / Glutamine
    'R':['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],    # R / Arg / Arginine
    'S':['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],    # S / Ser / Serine
    'T':['ACU', 'ACC', 'ACA', 'ACG'],                  # T / Thr / Threonine
    'V':['GUU', 'GUC', 'GUA', 'GUG'],                  # V / Val / Valine
    'W':['UGG'],                                       # W / Trp / Tryptophan
    'Y':['UAU', 'UAC'],                                # Y / Tyr / Tyrosine
    'stop':['UAA', 'UAG', 'UGA']                       # Stop Codons
}

# Reverse keys/values of 'dict_protein_to_codon'.
DICT_CODON_TO_PROTEIN = {}
for key,value in DICT_PROTEIN_TO_CODON.items():
    for val in value:
        if val in DICT_CODON_TO_PROTEIN:
            DICT_CODON_TO_PROTEIN[val].append(key)
        else:
            DICT_CODON_TO_PROTEIN[val] = [key]


def protein_to_trna(sequence):
    """Convert Protein sequence to tRNA sequence."""

    split_codons = []
    n = 1

    for index in range(0, len(sequence), n):
        split_codons.append(sequence[index : index + n])

    string = ""

    for i in split_codons:
        # Print first matching codon, remove '[0]' for all possible combos.
        string += str(DICT_PROTEIN_TO_CODON[i][0])

    print("\n{string}")
    return string


def trna_to_protein(sequence):
    """Convert tRNA sequence to Protein sequence."""
    split_codons = []
    codon = 3

    for index in range(0, len(sequence), codon):
        split_codons.append(sequence[index : index + codon])

    string = ""

    for i in split_codons:
        # Print first matching codon, remove '[0]' for all possible combos.
        string += str(DICT_CODON_TO_PROTEIN[i][0])

    print("\n{string}")
    return string


#############
# Kickstart #
#############

# Example sequence
protein_sequence = (
    "IVGGWECEQHSQPWQAALYHFSTFQCGGILVHRQWVLTAAHCISDNYQLWLGRHNLFDDENTAQFVHVSESFPHPGFNMSLLENHTRQADEDY"
    "SHDLMLLRLTEPADTITDAVKVVELPTEEPEVGSTCLASGWGSIEPENFSFPDDLQCVDLKILPNDECKKAHVQKVTDFMLCVGHLEGGKDTC"
    "VGDSGGPLMCDGVLQGVTSWGYVPCGTPNKPSVAVRVLSYVKWIEDTIAENS"
)

# Translated example sequence
codon_sequence = (
    "AUUGUUGGUGGUUGGGAAUGUGAACAACAUUCUCAACCUUGGCAAGCUGCUUUAUAUCAUUUUUCUACUUUUCAAUGUGGUGGUAUUUUAGUU"
    "CAUCGUCAAUGGGUUUUAACUGCUGCUCAUUGUAUUUCUGAUAAUUAUCAAUUAUGGUUAGGUCGUCAUAAUUUAUUUGAUGAUGAAAAUACU"
    "GCUCAAUUUGUUCAUGUUUCUGAAUCUUUUCCUCAUCCUGGUUUUAAUAUGUCUUUAUUAGAAAAUCAUACUCGUCAAGCUGAUGAAGAUUAU"
    "UCUCAUGAUUUAAUGUUAUUACGUUUAACUGAACCUGCUGAUACUAUUACUGAUGCUGUUAAAGUUGUUGAAUUACCUACUGAAGAACCUGAA"
    "GUUGGUUCUACUUGUUUAGCUUCUGGUUGGGGUUCUAUUGAACCUGAAAAUUUUUCUUUUCCUGAUGAUUUACAAUGUGUUGAUUUAAAAAUU"
    "UUACCUAAUGAUGAAUGUAAAAAAGCUCAUGUUCAAAAAGUUACUGAUUUUAUGUUAUGUGUUGGUCAUUUAGAAGGUGGUAAAGAUACUUGU"
    "GUUGGUGAUUCUGGUGGUCCUUUAAUGUGUGAUGGUGUUUUACAAGGUGUUACUUCUUGGGGUUAUGUUCCUUGUGGUACUCCUAAUAAACCU"
    "UCUGUUGCUGUUCGUGUUUUAUCUUAUGUUAAAUGGAUUGAAGAUACUAUUGCUGAAAAUUCU"
)

protein_to_trna(protein_sequence)
trna_to_protein(codon_sequence)

# End of File.
