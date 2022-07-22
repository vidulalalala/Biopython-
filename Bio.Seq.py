import Bio

from Bio.Seq import Seq

dna = Seq("ATTCGGGGATACGTAGGCGCGCATTTGAGCTATAT")

print(dna[0:3])

print(dna.count("T"))

print(dna.count_overlap("CG"))

print(dna.transcribe())