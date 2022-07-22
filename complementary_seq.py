dna_seq = "TTCCTGACTATTGGGAAAGGGTGCTTCATAGATTTACATCGACATATCCATTCCAAACAAACGTTGGTACGGCAGCCCTTATACCTCAAAGGAGGTCGACCCAAGATAATAGTGGTGGACCTTGAGGCTAGGAAACTACGTGAACGAGCTTCAGACTTCTCAATGTTGATTTGTCACCCAAGATCATCAAGCCGGATTAAGATGGGAGGAACAATCCTGGGGCTTGTACACACTATGCTTCTCTCATCAATTATACTTAAAATTCTCTGTCCTAGAAGGAGCGTTTGGTCGTTTGGGACGGCCGGGACCGCTGGCCCGACTAAAATCAGACGATGATCGCCCCTCGGCATATGCCATTAGAGCACTTCCCTGAGGTCCTAAACTTACTGCACGACAGTGTGATTCTGTCTAGATGTCGTAACAAACTTAGCGTTGACGGTTAAAGACCGCGGACCTTAAACCATTGATAGATCCGAAAACATCCCCGCCCAAGAAAACTGTTGTAGCTCTGTCGCCTAACTGGAGCTATAGCCACGCGCATACTCGAT"
complementary_seq = ""

dnaSequence = list(dna_seq)
dnaSequence.reverse()

dna_seq = ''.join(dnaSequence)
complementary_key = {"C":"G", "G":"C","T":"A","A":"T"}

for base in dna_seq:
    complementary_seq += complementary_key[base]

print(complementary_seq)