#Count nucleotides in a DNA sequence

def countfrequency(seq):
    nucleotides = {'A': 0, 'G': 0, 'T': 0, 'C': 0}
    for base in seq:
        nucleotides[base] += 1
    return nucleotides
        
DNA_seq = "ATGACGATGATACG"
base_freq = countfrequency(DNA_seq)
print(base_freq)