'''

   (c) 2024 Edwin Chengetai Nyamukapa

   Open account, login, show balance, transfer money,
   reset password.

'''

import os.path


def show_balance(balance):                        # show balance function - displays current balance to user
    print(f'Current balance: ${balance:.2f}')     # balance as float

def deposit():
    amount = float(input('Enter deposit amount...'))  # accept user input as float to prevent the user from entering a string

    if amount < 0:                                    # return error for negative deposits
        print('Invalid amount...')
        return 0
    else:
        return amount

# user withdrawal request
def withdraw(balance):
    amount = float(input('Enter withdrawal amount'))

    if amount > balance:                              # check if the withdrawal request is greater than current balance
        print('Insuffient available balance...')
        return 0
    elif amount < 1:
        print('Minimum withdraw amount is $1.00')     # minimum withdrawal amount required by the system
        return 0
    else:
        return amount

# create account process
def create_account():
    print('+-------------------------------+')
    print('+------- MyBank Limited --------+')
    print('+----- Bank of the People ------+')
    print('+-------------------------------+')

    # user details input
    l_name = input('Enter last name.')    # Last name
    f_name = input('Enter first name.')   # First name
    n_id = input('Enter ID number.')      # National registration number
    reg_pin = int(input('Enter pin.'))    # Preferred PIN

    # confirm if details are correct
    print('Confirm details for:')
    print(f'Last name: {l_name}')
    print(f'First name: {f_name}')
    print(f'ID: {n_id}')

    # create a text file with user details
    # last name, first name, national id, pin
    confirm = input('Next')
    if confirm == 'Next':
        file = open(f'{l_name}-{f_name}.txt', 'w')
        file.write('Account for: \n')
        file.write(f'Lastname: {l_name}\n')
        file.write(f'Firstname: {f_name}\n')
        file.write(f'ID: {n_id}\n')
        file.write(f'Pin: {reg_pin}')
        print('Account created successfully...')
    else:
        print('Error creating account....')

# log in function
def login():

    l_name = input('Enter Lastname...')
    f_name = input('Enter Firstname...')

    # check if user file exist
    if os.path.isfile(f'{l_name}-{f_name}.txt'):

        print('Account found for ' + l_name, f_name)

        vault = open(f'{l_name}-{f_name}.txt', 'r+')

        pin = input('Enter PIN to continue...')

        check = vault.read(500)

        # authenticate user if pin is correct
        if pin in vault:
            print('Success!')
        else:
            print('Access denied!')

    else:
        print('No User account found...') # display error if user file not found


# main function
def main():

    balance = 0          # global variable
    is_running = True

    while is_running:
        # display main menu to user
        print('+-------------------------------+')
        print('+------- MyBank Limited --------+')
        print('+----- Bank of the People ------+')
        print('+-------------------------------+')
        print('+-- 1. Create account')
        print('+-- 2. Login')
        print('+-- 3. Deposit')
        print('+-- 4. Withdraw')
        print('+-- 5. Reset password')
        print('+-- 6. Exit')
        print('+-------------------------------+')
        print('+----------- Hotline -----------+')
        print('+-----  +263-242-000-001  ------+')
        print('+-------------------------------+')

        # accept user option
        user_input = input('Enter choice to continue...')

        # display info from user input
        if user_input == '1':
           create_account()
        elif user_input == '2':
           login()
        elif user_input == '3':
           balance -= withdraw(balance)
        elif user_input == '4':
           withdraw()
        elif user_input == '5':
            reset_password()
        elif user_input == '6':
            is_running = False
        else:
           print('Invalid response...')

    print('Thank you for using MyBank Limited.')


main()