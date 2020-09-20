import time
from tkinter import *

root = Tk()
root.geometry("600x400")
while True:
    try: 
        pin = int(input('Please input your pin! '))
        if pin in range(1000, 10000):
            break
        else:
            print('pin must be 4 digit')
    except ValueError:
        print('pin must be an integer')
# print('pin is now an integer')

password = pin
account_balance = 1000000

def transaction():
    global amount_withdraw 
    global amount_after_withdraw
    amount_after_withdraw = 0
    while True:
        if pin == password:
            print('correct pin...')
            print('Please select the mode of transaction you want to perform')
            selection = input("Select W for Withdrawal\nSelect B for Balance Enquiry\nSelect T for transfer\n")
            if selection == 'W' or selection == 'w':
                while True:
                    try:
                        amount_withdraw1 = int(input('Please input the amount you want to withdraw '))
                        if amount_withdraw1 < account_balance:
                            break
                        else:
                            print('insuffient funds')
                    except ValueError:
                        print('must be an integer')
                print('please wait while your transaction is processing...')
                time.sleep(3)
                print('You have successfully withdraw {} from your account'.format(amount_withdraw1))
                amount_after_withdraw = account_balance - amount_withdraw1

            if selection == 'B' or selection == 'b':
                print('Your acccount balance is {}'.format(account_balance))

            if selection == 'T' or selection == 't':
                while True:
                    try:
                        destination_account = int(input('Please input the destination account number '))
                        if destination_account in range(10000000000, 100000000000):
                            break
                        else:
                            print('account number must be 10 digit')
                    except ValueError:
                        print('The destination account number must be an integer')
                while True:
                    try:
                        amount_to_transfer = int(input('Please input the amount you want to transfer '))
                        if amount_to_transfer < account_balance:
                            break
                        else:
                            print("insufficent funds!")
                    except ValueError:
                        print('Amount must be an integer')
        reply = input("do you want to do another transaction? choose y for yes and n for no ")

    
        if reply == 'n' or reply == 'N':
            exit()
        elif reply == 'y' or reply == 'Y':
            transaction()
        
       
        
transaction()

root.mainloop()

