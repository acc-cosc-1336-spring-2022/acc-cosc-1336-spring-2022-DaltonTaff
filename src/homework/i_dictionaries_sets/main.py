import dictionary

def main_menu():
    print('[1]: Get Distance')
    print('[2]: Exit')
    user_input = input('Select an option: ')
    if user_input == '1':
        choice1()
    elif user_input == '2':
        choice2()
    
def choice1():
    print()
    dataset = []
    add_sequence = 'Y'
    while add_sequence == 'y' or add_sequence == 'Y':
        dna = input('Enter the sequence of DNA: ')
        dnal = list(dna)
        dataset.append(dnal)
        add_sequence = input('Additional data?: ')
    print()
    print('Data entered')
    for data in dataset:
        print('\t', data)
    print()
    print('The Distance is: ')
    p_distance_matrix = dictionary.get_p_distance_matrix(dataset)
    for row in p_distance_matrix:
        for e in row:
            print(format(e, '12.1f'), end=' ')
        print('')
    print()
    user_input = input('Additional data?')
    result = user_input
    if result == 'n' or result == 'N':
        main_menu()
    if result == 'y' or result == 'Y':
        choice1()

def choice2():
    print('Shutting down')
    quit()

main_menu()
#The Group helped me with the format