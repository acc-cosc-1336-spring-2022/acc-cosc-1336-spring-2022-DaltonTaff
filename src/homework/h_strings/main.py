
from strings import get_hamming_distance,get_dna_complement


sel1 = ''
while sel1 != "3":
    sel1 = str(input('1 = Hammering Distance \n 2 = Dna Complement \n 3 = Exit\n'))
    if sel1 == "1":
        dna = str(input('Enter first Dna'))
        dna2 = str(input('Enter Second Dna'))
        print(get_hamming_distance(dna, dna2))
    elif sel1 == '2':
        dna = str(input('Enter Dna'))
        print(get_dna_complement(dna))
    elif sel1 == '3':
        exit('Exiting')
    else:
        print('Enter Valid Characters')
        sel1 = str(input('1 = Hammering Distance \n 2 = Dna Complement \n 3 = Exit\n'))