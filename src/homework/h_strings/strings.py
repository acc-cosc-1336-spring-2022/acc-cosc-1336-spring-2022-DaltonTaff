def get_hamming_distance(dna1 , dna2):
    li_dna1 = list(dna1)
    li_dna2 = list(dna2)
    count = 0
    for i in range(len(li_dna1)):
        if li_dna1[i] != li_dna2[i]:
            count += 1
        return count

def get_dna_complement(dna):
    
    complement = ''
    for n in dna:
        if n == 'A':
            complement += 'T'
        elif n == 'T':
            complement += 'A'
        elif n == 'C':
            complement += 'G'
        elif n == 'G':
            complement += 'C'
    return complement[::-1]



    