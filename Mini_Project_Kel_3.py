# THIS IS AN UPGRADED VERSION OF THE VENDING MACHINE
# NEW FEATURES INCLUDE THE BIG_STRINGS NO LONGER NEED TO BE FIXED LENGTH
# THE CODE WILL RECONFIGURE ITSELF TO MATCH THE LONGEST PRODUCT LINE !!!

# The longest line doesn't have to be at the top but do note that the longest
# line needs to give space for variables that will be auto written later like
# DEFAULT_PRODUCT_STOCK, DEFAULT_MONEY_STOCK when written can overflow if the
# longest line doesn't have enough space to fit that written data.

# lastly, longest lines must have a '*' at the end to serve as clear mark of being the longest
PRODUCTS = '''
-MAXIMALLY LONG-NAMED PRODUCT.200000|00000:100*
-Chatito.10500|0:10
-El Minerale.3800|0:10
-ReeCheez.11300|0:10
-SUPER FOOD.24700|000:10
-Cola Coca.5000|0:10
-Deez Peas.12300|0:10
-GiGaGlizzy.12400|0:10
'''
DEFAULT_PRODUCT_STOCK = 5 # THIS IS TO SET THE DEFAULT STOCK OF EVERY PRODUCT ITEM # TWEAK HERE !
DEFAULT_MONEY_STOCK = 100 # THIS IS TO SET THE DEFAULT STOCK OF THE PHYSICAL MONEY # TWEAK HERE !
MAX_IDR_PAYMENT = 200_000 # this prevents customers potentially breaking the vending machine by 
MAX_SGD_PAYMENT = 100_00 # overflowing the machine's bank "wallet" with absurdly large payments
# say $1 SGD dollar is Rp.12,800 IDR would be :
SGD_to_IDR_ratio = 128.0 # 1 SGD cent is 128 IDR # CHANGE THE RATIO HERE !!!!!!!!!!!!!!!!!!!!!!!!
# ------------------------------------------------ THIS IS THE BANK TO STORE THE MACHINE"S CASH!
# longest lines in these banks need to have enough space to store how much banknotes the machine 
# will have at the end of the day... otherwise it will overflow its length and break the program
BANK_IDR = '''
-Rp.100_000:000000*
-Rp.50_000:000
-Rp.20_000:000
-Rp.10_000:000
-Rp.5_000:000
-Rp.2_000:000
-Rp.1_000:100
-Rp.500:100
-Rp.200:100
-Rp.100:100
'''
# Notice SGD is stored in cents to avoid decimals because the machine's processes work best with integers
BANK_SGD = '''
-$.100_00:000000*
-$.50_00:000
-$.10_00:000
-$.5_00:000
-$.2_00:000
-$.1_00:000
-$.50:000
-$.20:100
-$.10:100
-$.5:100
-$.1:100
'''
# --------------------------------------------------------------------------------------------- THE BIG_STRING PREPARATOR
def prepare(big_string):
    lines = 0 # HOW MANY LINES INSIDE big_string this will be one extra for range(end) is exclusive
    longest = 0 # get the longest line
    char_count = 0
    for i in big_string:
        if i == '\n': # everytime it meets a line ending
            lines += 1 # count as one line of PRODUCTS
            if char_count > longest: # if this line has more characters
                longest = char_count # make this line as the longest
            char_count = 0 # reset the character counter
            continue # dont count newlines '\n'
        char_count += 1 # increment to count characters
    # now that we found the longest line, reconstruct the big_string to have all lines be just as long
    NEW = '\n'
    collect = ''
    for i in big_string:
        if i != '\n':
            collect += i
        else:
            current_length = len(collect) # that if current_length > 0 else '' is just for the case of the first \n in the big_string
            NEW += collect + ('*' * (longest - current_length)) + i if current_length > 0 else ''
            collect = ''
    return NEW, lines, longest
# These prepare the significant data for all big_strings
PRODUCTS, product_count, product_line_length = prepare(PRODUCTS)
BANK_IDR, idr_count, IDR_line_length = prepare(BANK_IDR)
BANK_SGD, sgd_count, SGD_line_length = prepare(BANK_SGD)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> GET ANY LINE FROM A BIG STRING
def get_line(line, big_string, big_length):
    data_buffer = '' # to store each character
    i = line + ((line-1)*big_length) # enables smart line jumping... tho sensitive...
    while (True):
        if big_string[i] == '*': # only return after it meets '*'
            return data_buffer + '*'
        data_buffer += big_string[i]
        i += 1


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> EXTRACT DATA BETWEEN 2 SEPARATORS
def read_data(product_line, separator1, separator2):
    extracted_data = ''
    x = 0 # this is just to count string index
    for i in product_line:
        if i == separator1: # START EXTRACTION
            x += 1 # skip the first separator1
            while product_line[x] != separator2: # EXTRACT UNTIL product[x] is the second separator2
                extracted_data += product_line[x]
                x += 1
            # After successful data extraction, RETURN
            return extracted_data
        x += 1 # keep looping until the first seperator1 is found


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> WRITE DATA BETWEEN 2 SEPARATORS
def write_data(product_line, big_length, separator1, value, separator2):
    updated_product = '' # a buffer for the updated product
    value = str(value) # make sure value is a string

    x = 0 # this is just to count string index
    # This for loop is just for copying the chars before seperator1
    # Until it finds separator 1 then proceed injecting
    for i in product_line:
        if i == separator1: # START WRITING
            updated_product += i + value # add the separator1 i then add the whole value
            # This skips the characters that are replaced by the value
            while product_line[x] != separator2:
                x += 1
            # add the rest of the original data that is unchanged
            while product_line[x] != '*':
                updated_product += product_line[x]
                x += 1
            # After successful writing, BREAK out of the for loop, no longer needed
            break
        else:
            updated_product += i
        x += 1

    # check if the updated product became more than the big_length char limit
    length = len(updated_product)
    if length > big_length:
        print(updated_product)
        float("VALUE IS TOO LARGE, THE WHOLE PRODUCT LINE EXCEEDS big_length")
    # after writing the updated_product can be less than big_length chars so gotta add fillers
    updated_product = updated_product + ('*' * (big_length - length)) if length < big_length else updated_product
    return updated_product + '\n' # FINALLY


# ---------------------------------------------------------------------------------------------------
NEW = '\n' # start with a newline sequence like the original
for i in range(1, product_count):
    line = get_line(i, PRODUCTS, product_line_length)
    IDR_value = float(read_data(line, '.', '|'))
    SGD_value = round(IDR_value / SGD_to_IDR_ratio)
    # write the SGD_value as the new data to update PRODUCTS
    # NEW += write_data(line, '|', SGD_value, ':') # >>>>>>>>>>>>>>>>>>>> SWAP WITH THIS AND GET RID BELOW TO ENABLE MANUALLY SETTING THE STOCK
    defined_sgd = write_data(line, product_line_length, '|', SGD_value, ':')
    # with the defined SGD now write the default product stock
    NEW += write_data(defined_sgd, product_line_length, ':', DEFAULT_PRODUCT_STOCK,'*')
PRODUCTS = NEW # >>>>>>>>>>>>>>>>>>>>>>>>>>>>> THIS OUTRIGHT REPLACES THE OLD PRODUCTS WITH THE UPDATED NEW

idr_initial = 0 # store the initial total in the bank for BUSINESS REPORT AT THE VERY END
NEW = '\n' # Reset the NEW buffer to store updated Bank IDR
for i in range(1, idr_count):
    line = get_line(i, BANK_IDR, IDR_line_length)
    idr_initial += int(read_data(line, '.', ':')) * DEFAULT_MONEY_STOCK
    NEW += write_data(line, IDR_line_length, ':', DEFAULT_MONEY_STOCK, '*')
BANK_IDR = NEW # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> REPLACE the manually set bank stocks with the NEW bank stocks set to default

sgd_initial = 0 # store the initial total in the bank for BUSINESS REPORT AT THE VERY END
NEW = '\n' # Reset again to store Bank SGD
for i in range(1, sgd_count):
    line = get_line(i, BANK_SGD, SGD_line_length)
    sgd_initial += int(read_data(line, '.', ':')) * DEFAULT_MONEY_STOCK
    NEW += write_data(line, SGD_line_length, ':', DEFAULT_MONEY_STOCK, '*')
BANK_SGD = NEW # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> REPLACE the manually set bank stocks with the NEW bank stocks set to default


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FORMAT INTEGER PRICES INTO READY PRINT STRING
def print_price(value, currency):
    return f'Rp.{value:,}' if currency == 'IDR' else f'${float(value)/100.0:.2f}'


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PRINT THE MENU FOR THE USER TO SEE
def display_menu():
    print("\n\n_-*_-*< Vending Machine >*-_*-_")
    for i in range(1, product_count):
        product = get_line(i, PRODUCTS, product_line_length) # get the line of the product !
        name = read_data(product, '-', '.')  # get the name of the current data
        price = int(read_data(product, '.', '|')) # get the price of the current data

        print(f'{i:<2}) {name:<13} -> {print_price(price, "IDR"):<9} |') # print them one by one
    print('Type in the number of your choice :) type "bye" to exit')


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> GET THE USER TO CHOOSE
def get_choice(): # WILSON
    while True:
        text = input('What can we serve you ? ') # prompt for input with str as what to ask
        valid = True # valid is set to True by default

        # this is in case the customer wants to exit quick
        if text == 'bye': 
            return 'bye' # kinda bad sudden change of return type but THIS IS PYTHON YAYYY
        

        # check for each character the customer inputted
        for i in text:
            # if a current character i is not one of "0123456789" then text CAN'T be converted into an integer
            if i not in "0123456789":
                valid = False # Therefore set the valid into False
                break # break the FOR LOOP since only one invalidity is all it takes to break the program
        
        # if text is not an empty input AND valid AND its a choice in the options
        if text and valid and 0 < int(text) < product_count:
            choice = int(text)
            # CHECK IF THIS CHOSEN PRODUCT IS STILL IN STOCK
            if int(read_data(get_line(choice, PRODUCTS, product_line_length), ':', '*')) < 1 :
                print("Unfortunately that product is out of stock, sorry :(\nCan we interest you in anything else ? ")
                continue # RESTART THE PROCESS
            return choice
        # invalid inputs will just cause the while loop to continue again and repeat asking for proper input


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> HELPING FUNCTION to prompt user to restart
def retry_purchase(error_message):
    print(f'<!> {error_message}')
    return True if input("Do you want to retry purchase ? (y/n) ") in 'YESyesYes' else False
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CHARGE PAYMENT WARNING THIS IS A HUGE FUNCTION
def charge_payment(choice):
    line = get_line(choice, PRODUCTS, product_line_length)
    name = read_data(line, '-', '.')
    billing_IDR = int(read_data(line, '.', '|'))
    billing_SGD = int(read_data(line, '|', ':'))
    str_idr = print_price(billing_IDR, 'IDR')
    str_sgd = print_price(billing_SGD, 'SGD')
    # Tell the user how much they have to pay
    print(f"{name} will cost you :\n{str_idr} IDR or {str_sgd} SGD")

    # payment checking
    while True:
        # ask the user wanna pay with IDR of SGD
        text = input("with IDR or SGD ? ")
        
        if not (text == 'IDR' or text == 'SGD'): # if the input given is invalid
            print("<!> choose type 'IDR' or 'SGD' please")
            continue # RETRY asking for input by continueing the while loop from the beginning

        # next check for value
        pay = input(f"{str_idr if text == 'IDR' else str_sgd} Enter Payment : ")
        decimal = 0
        for i in pay: # CHECK IF THE USER PAYMENT IS VALID CONVERTIBLE TO FLOAT
            if i not in '0123456789.':
                pay = '' # this is used to indicate invalidity because an empty string is falsy
                break
            elif i == '.':
                decimal += 1
        # not pay means it contains non digit characters, decimal points can only be 1 or none
        # for IDR payment, the payment must also have NO DECIMALS because its just integers
        if not pay or decimal > 1 or (text == 'IDR' and decimal > 0):
            if retry_purchase("INVALID PAYMENT - must be numbers or with valid decimal points"):
                continue # if the user agreed to retry, RESTART this while loop !
            else:
                return 0, '', True, 0 # Exit function and tell payment was cancelled !
        
        # At this point pay can be safely converted to int for IDR or SGD dollars as float into cents as int
        pay = int(pay) if text == 'IDR' else int(float(pay) * 100.0)
        # that int() will truncate any decimal point value !
        max_allowed_pay_sum = MAX_IDR_PAYMENT if text == 'IDR' else MAX_SGD_PAYMENT
        if pay > max_allowed_pay_sum:
            if retry_purchase(f"Sorry, your payment exceeds the maximum of {max_allowed_pay_sum}"):
                continue # if the user agreed to retry, RESTART this while loop !
            else:
                return 0, '', True, 0 # Exit function and tell payment was cancelled !
        # check if its enough to pay the bills lmao
        bill = billing_IDR if text == 'IDR' else billing_SGD
        if pay >= bill: # if payment is enough to pay the bill
            # even if the payment is enough to pay the bills...
            # MUST MAKE SURE ITS IN REPRESENTABLE WITH THE EXISTING BANKNOTES
            last_line = idr_count - 1 if text == 'IDR' else sgd_count - 1
            selected_bank = BANK_IDR if text == 'IDR' else BANK_SGD
            line_length = IDR_line_length if text == 'IDR' else SGD_line_length
            smallest = int(read_data(get_line(last_line, selected_bank, line_length), '.', ':'))
            if pay % smallest != 0:
                if retry_purchase(f"{pay} is not representable by the smallest banknote value of {smallest}"):
                    continue # if the user agreed to retry, RESTART this while loop !
                else:
                    return 0, '', True, 0 # Exit function and tell payment was cancelled !

            # RETURN THE PAY SUM, TYPE OF PAYMENT, AND payment is NOT canceled
            return pay, 'IDR' if text == 'IDR' else 'SGD', False, pay - bill # pay - bill is the change
        # Otherwise, if its not enough to pay the bills, ask for retry !
        elif retry_purchase(f"Sorry, that's not enough to pay the {name}"):
            continue # if the user agreed to retry, RESTART this while loop !
        else:
            return 0, '', True, 0 # Exit function and tell payment was cancelled !


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> TO ACCEPT OR GIVE OUT
def accounting(money, currency_type, refund, str):
    NEW = '\n'
    # get the bank and its size based from the currency type
    bank = BANK_IDR if currency_type == 'IDR' else BANK_SGD
    size = idr_count if currency_type == 'IDR' else sgd_count
    line_length = IDR_line_length if currency_type == 'IDR' else SGD_line_length
    print(f"{str} : ", end='') # SHOW WHAT's HAPPENING

    # Go through each currency value of the selected bank
    for i in range(1, size):
        line = get_line(i, bank, line_length) # get the data from the bank
        # get info of each bank_note value and its stock
        bank_note = int(read_data(line, '.', ':'))
        bank_note_stock = int(read_data(line, ':', '*'))

        # get how many bills of bank_note's value can money be divided without remainders
        new_bills = money // bank_note

        # if money CAN be divided by new_bills worth of bank_note's value
        # if its in refund mode, stock must NOT be less than what needs to be given,
        if new_bills > 0 and not (refund and bank_note_stock < new_bills):
            # HERE IS WHERE refund MODE DECIDES IF MONEY SHOULD BE RETURNED OR ACCEPTED
            bank_note_stock += new_bills if not refund else - new_bills
            # print to show how much money the user gave
            bill_str = print_price(bank_note, currency_type)
            print(f'{new_bills} x {bill_str} | ', end='')
            money = money % bank_note # here update money to be the remainder of what can be divided by bank_note's value
        # if new_bills > 0 then this updates the NEW big_string, otherwise it stays the same
        NEW += write_data(line, line_length, ':', bank_note_stock, '*')

    print() # a newline since that print up there has end=''
    return NEW # return the new and updated big_string

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PREDICT IF THE MACHINE CAN COMPLETELY RETURN THE MONEY OR NOT
def can_return_change(prediction, currency_type):
    bank = BANK_IDR if currency_type == 'IDR' else BANK_SGD
    size = idr_count if currency_type == 'IDR' else sgd_count
    line_length = IDR_line_length if currency_type == 'IDR' else SGD_line_length
    for i in range(1, size):
        line = get_line(i, bank, line_length)
        bank_note_stock = int(read_data(line, ':', '*')) # get the stock of this banknote
        bank_note = int(read_data(line, '.', ':')) # get the value of this banknote

        bills = prediction // bank_note # get how many bills should be given
        # only take out change if the bank stock has more than or equal bills to give
        if bills != 0 and bank_note_stock > bills:
            prediction = prediction % bank_note

    # predict == 0 means it can return the change completely,
    if prediction == 0:
        return True, 0
    else:
        return False, prediction # return predict in case its not zero to tell how much cant be returneds


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Take out the paid product out of the big_string and give it to the customer
def take_out(choice):
    # new has to have that "name.IDR:stock***********" format
    # PRODUCTS IS A STRING WHICH PYTHON SAYS ITS IMMUTABLE SO IMMA MAKE A WHOLE NEW COPY
    NEW = '\n' # this is just a buffer for the whole process
    for i in range(1, product_count):
        line = get_line(i, PRODUCTS, product_line_length) # get the chosen product's line
        stock = int(read_data(line, ':', '*')) # get its stock
        if i == choice:
            stock -= 1 # only decrease the stock of the product taken away
        NEW += write_data(line, product_line_length, ':', stock, '*')
    return NEW


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FINALLYYYY THIS IS MAIN !!!
while True:
    display_menu() # display the menu

    choice = get_choice()
    # check if the user wants to exit the vending machine
    if choice == 'bye':
        print("Thank you for your visit ! See ya next time :)\n\n")
        break

    # charge payment for the choice the user made
    payment, currency_type, cancelled, change = charge_payment(choice)

    # first, check if payment is cancelled or not
    if cancelled:
        continue # if it is cancelled, RESTART the whole process from the beginning


    # ACCEPT THAT MONEY FIRST but accept money to the right bank, otherwise leave it untouched
    BANK_IDR = accounting(payment, currency_type, False, 'Your Payment') if currency_type == 'IDR' else BANK_IDR
    BANK_SGD = accounting(payment, currency_type, False, 'Your Payment') if currency_type == 'SGD' else BANK_SGD

    # only give change if there is chage to give
    if change > 0:
        # check first if the machine has enough bank_notes to give change
        can_return, left_over_change = can_return_change(change, currency_type)

        if can_return:
            # reuse the accounting's refund mode to return the change
            BANK_IDR = accounting(change, currency_type, True, "Here's your change") if currency_type == 'IDR' else BANK_IDR
            BANK_SGD = accounting(change, currency_type, True, "Here's your change") if currency_type == 'SGD' else BANK_SGD
        else:
            # use refund mode to well.. refund the payment money
            BANK_IDR = accounting(payment, currency_type, True, "REFUND") if currency_type == 'IDR' else BANK_IDR
            BANK_SGD = accounting(payment, currency_type, True, "REFUND") if currency_type == 'SGD' else BANK_SGD
            print('\n\nUnfortunately we ran out of bank notes to give the change :(')
            print(f'<!> Cant return {print_price(left_over_change, currency_type)}')
            print('Sorry for the inconvenience, Please contact our operator to restock\nExact payment can still be done !\n')
            continue # RESTART THE MAIN LOOP
    else:
        print("That's exact payment, Thank you !")

    # AT THIS POINT, PAYMENT IS COMPLETE SO GIVE THE CUSTOMER THE PRODUCT
    PRODUCTS = take_out(choice) # decrease the chosen product's stock
    print(f'''\n
WE HEREBY PRESENT YOU

  ::____________::
  ::{read_data(get_line(choice, PRODUCTS, product_line_length), '-', '.'):^12}::
  ::************::

<THY PAID CONSUMABLE>''')
    if input("Wanna buy anything else ? (y/n) ") in 'YESyYesyes':
        continue # restart the whole process
    else:
        print("Thank you for your visit ! See ya next time :)\n\n")
        break # finally get out of here !
    

# BUSINESS REPORT
print("_-*_-* < BUSINESS REPORT > *-_*-_")
print(BANK_IDR)
print(BANK_SGD)
print(PRODUCTS)
idr_stonks = 0
sgd_stonks = 0
for i in range(1, idr_count):
    line = get_line(i, BANK_IDR, IDR_line_length)
    idr_stonks += int(read_data(line, '.', ':')) * int(read_data(line, ':', '*'))

for i in range(1, sgd_count):
    line = get_line(i, BANK_SGD, SGD_line_length)
    sgd_stonks += int(read_data(line, '.', ':')) * int(read_data(line, ':', '*'))
idr_profit = idr_stonks - idr_initial
sgd_profit = sgd_stonks - sgd_initial
print('-------------------------------------------------------')
print(f"PROFIT REPORT : IDR {print_price(idr_profit, 'IDR')} | SGD {print_price(sgd_profit, 'SGD')}")

# THIS IS A FAILED SYSTEM. UNABLE TO UPDATE THE PRODUCT_COPY = new for some reason we are out of ideas
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> RETURN A BIG STRING OF THE BOUGHT PRODUCTS
# def bought_products(choices_):
#     PRODUCTS_COPY = '\n' # make a temporary big_string to use for tracking what was bought
#     for i in range(1, product_count):
#         # reuse the stock area as counter for how many of this is bought
#         PRODUCTS_COPY += write_data(get_line(i, PRODUCTS), ':', 0, '*') 
    
#     print(PRODUCTS_COPY)
#     store_digits = '' # for choices_
#     # TRACK WHAT GETS BOUGHT
#     for i in choices_: # go through each choices string
#         if i != '.': # if i is not a '.' which is the separator
#             store_digits += i # store first before being converted
#         # when i is the separator
#         else :
#             choice = int(store_digits) # convert the stored digits

#             keep = '\n'
#             # painstakingly update PRODUCT_COPY before continueing...
#             new = '\n' # REBUILD FROM THE BEGINNING
#             print(f'CHOICE ------->{choice}')
#             for j in range(1, product_count):
#                 print(get_line(choice, PRODUCTS_COPY))
#                 stock = int(read_data(get_line(choice, PRODUCTS_COPY), ':', '*'))
#                 print(f"J -> {j}",end='')
#                 if j != choice:
#                     print(f"NOT: {stock}")
#                     new += write_data(get_line(j, PRODUCTS_COPY), ':', stock, '*') # just copy unchanged if not the taget choice
#                 else:
#                     stock += 1
#                     print(f"FOUND - > {stock}")
#                     new += write_data(get_line(j, PRODUCTS_COPY), ':', stock, '*') # add in the changed stock
            
#             PRODUCTS_COPY = new # This is an example of the downsides of this big string mechanism ...
#             print(PRODUCTS_COPY)
#             store_digits = '' # RESET after it finished scoring

#     return PRODUCTS_COPY # NEW is not a 
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> SUM UP THE PRICES
# def calc_billings(choices_):
#     store_digits = ''
#     IDR_total = 0
#     SGD_total = 0
#     for i in choices_: # go through each choices string
#         if i != '.': # if i is not a '.' which is the separator
#             store_digits += i # store first before being converted
#         # when i is the separator
#         else :
#             choice = int(store_digits) # convert the stored digits
#             IDR_total += int(read_data(get_line(choice, PRODUCTS), '.', '|')) # add the IDR prices
#             SGD_total += int(read_data(get_line(choice, PRODUCTS), '|', ':')) # add the SGD prices
#             store_digits = '' # RESET after it finished scoring
#     return IDR_total, SGD_total