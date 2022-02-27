import repetition

choice = 'y'
while choice == 'y':
    print('Homework 3 Menu')
    choice = int(input('\n1 Factorial \n2 Sum odd numbers \n3 Exit \n\n '))
    if choice == 1:
        num = int(input('enter number greater than 0 and less than 10: '))
        if num > 0 and num < 10:
            print(repetition.get_factorial(num))
        while num <= 0 or num >= 10:
            print('Invalid entry')
            num = int(input('enter number between 0 and 10: '))
            if num > 0 and num < 10:
                print(repetition.get_factorial(num))
    
    elif choice == 2:
        num = int(input('enter a number: '))
        print(repetition.sum_odd_numbers(num))

        
    elif choice == 3:
        print('Exiting')
    choice = str(input('Would you like to continue?'))