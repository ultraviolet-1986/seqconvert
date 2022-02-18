#!/usr/bin/env python3

"""
Filename: rna_codon_table.py
Author:   William Whinn

RNA Codon table for translating tRNA into Protein.
"""

dict_rna_proteins = {
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
    'stop':['UAA', 'UAG', 'UGA']                     # Stop Codons
}

# Reverse keys/values of 'dict_rna_proteins'.
dict_rna_codons = {}
for key,value in dict_rna_proteins.items():
    for val in value:
        if val in dict_rna_codons:
            dict_rna_codons[val].append(key)
        else:
            dict_rna_codons[val] = [key]

# Print items for verification.
print(dict_rna_proteins)
print()
print(dict_rna_codons)
print()

sequence = "IVGGWECEQHSQPWQAALYHFSTFQCGGILVHRQWVLTAAHCISDNYQLWLGRHNLFDDENTAQFVHVSESFPHPGFNMSLLENHTRQADEDYSHDLMLLRLTEPADTITDAVKVVELPTEEPEVGSTCLASGWGSIEPENFSFPDDLQCVDLKILPNDECKKAHVQKVTDFMLCVGHLEGGKDTCVGDSGGPLMCDGVLQGVTSWGYVPCGTPNKPSVAVRVLSYVKWIEDTIAENS"

# Break down a sequence into a parsable string.
def split_sequence(sequence):
    split_codons = []
    codon = 3

    for index in range(0, len(sequence), codon):
        split_codons.append(sequence[index : index + codon])

    print("\nReturned xNA sequence:")
    print(split_codons)


split_sequence(sequence)



def split_protein_sequence(sequence):
    split_codons = []
    n = 1

    for index in range(0, len(sequence), n):
        split_codons.append(sequence[index : index + n])

    # print("\nReturned Protein sequence:")
    # print(split_codons)

    return split_codons


split = split_protein_sequence(sequence)
print()
print(split)

string = ""

for i in split:
    # Print first matching codon, remove '[0]' for all possible combos.
    print(i, dict_rna_proteins[i][0])
    string += str(dict_rna_proteins[i][0])

print(string)


# End of File.
