import files

inv = {}
menu_select = 'y'

while menu_select == 'y':
    print('1 Add or Update file\n2 Display File\n3 Exit')
    select = int(input('Select an option'))

    if select == 1:
        while menu_select == "y":  
            print('\n1-Add or update\n2-Display Items\n3-Exit')
    select = int(input('Please select menu item 1, 2 or 3: ')) 

    if select == 1:   
        print('Add or update your inventory.')
        widget_name = input('Enter name: ')
        try:
          widget_quantity = int(input('Enter number of inventory '))
          files.add_inventory(inv, widget_name, widget_quantity)
        except ValueError:
             print('Error.')
        
    elif select == 2: 
         files.write_to_file(inv)
         files.read_from_file()

    elif select == 3:   
         exit('Exiting')