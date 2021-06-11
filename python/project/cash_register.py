
item_ids = ('001', '002', '003', '004')
item_details = {
    '001': {'name': 'Milk  ', 'price': '2.5', 'currency': '$'},
    '002': {'name': 'Egg   ', 'price': '2.0', 'currency': '$'},
    '003': {'name': 'Bread ', 'price': '1.5', 'currency': '$'},
    '004': {'name': 'Cheese', 'price': '5.5', 'currency': '$'}
}

prompt_message_previous_screen = 'Select p to go back to the previous screen: '
prompt_message_previous_screen_purchase = 'Make a selection - \n  p to go back to the previous screen\n  item number to make a purchase: '

# This function display the options for the Cashier 
def display_options():
    options_string = '''
    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    +                                                       +
    +   Select 1 to display all the items in store          +
    +   Select 2 to display the details for selected item   +
    +   Select 3 to make a new Sale                         +
    +   Select q to quit the program                        +
    +                                                       +
    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    '''
    print(options_string)
    selection = input('Please enter your selection: ')
    return selection

def display_items(list_item_ids):    
    print('+'*53)
    print('    Item Number         Item Name          Price      ')
    for id in list_item_ids:        
        print(' '*6, id, ' '*14, item_details[id]['name'], ' '*9, item_details[id]['currency'], item_details[id]['price'])
    print('+'*53)

def display_purchased_items(purchased_items):      
    print('+'*90)
    print('    Item Number         Item Name         Unit Price       Quantity      Total Price')
    for id in purchased_items: 
        total = float(item_details[id]['price']) * int(purchased_items[id])       
        print(' '*6, id, ' '*14, item_details[id]['name'], ' '*9, item_details[id]['currency'], item_details[id]['price'], ' '*11, purchased_items[id], ' '*12, total)
    print('+'*90)


def cashier_app():
    cashier_selection = ''
    while(cashier_selection != 'q'):
        cashier_selection = display_options()

        if cashier_selection == 'q':
            print('Quit the program')

        elif cashier_selection == '1':
            display_items(item_ids)
            while cashier_selection != 'p':                
                cashier_selection = input(prompt_message_previous_screen)
                print('Incorrect selection. ')

        elif cashier_selection == '2':
            # prompt the user to input the item id
            item_id = input('Select the item id: ')
            item_ids_list = [item_id]
            display_items(item_ids_list)
            while cashier_selection != 'p':                
                cashier_selection = input(prompt_message_previous_screen)
                print('Incorrect selection. ')

        elif cashier_selection == '3':
            cashier_selection = input(prompt_message_previous_screen_purchase)
            purchased_items = {}
            while cashier_selection != 'p': 
                if cashier_selection != 'p':
                    qty = input('Enter the quantity: ')
                    purchased_items[cashier_selection] = qty
                    display_purchased_items(purchased_items)
                    #for item in purchased_items:
                        #print('item = ', item, ', qty = ', purchased_items[item])
                    cashier_selection = qty
                cashier_selection = input(prompt_message_previous_screen_purchase)


                

                
    
cashier_app()

#def display_selected_item(item_id):





# print('Cashier has selected the option: ', cashier_selection)
