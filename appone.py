
from datetime import datetime as dt

username = input("What is your name? \n")
allowedUsers = ["Seyi", "Mike", "Love"]
allowedPassword = ['passwordSeyi', 'passwordMike', 'passwordLove']
total = 0

if username in allowedUsers:
    password = input("Your password? \n")
    userId = allowedUsers.index(username)

    if password == allowedPassword[userId]:
        print('\nWelcome %s \n' % username)
        
        print(dt.strftime(dt.now(), '''Date: %D
Time: %T'''))

        print('\nPlease enter Numerical Digits')
        
        print('\nThese are the available options: ')
        print('1. Withdraw')
        print('2. Cash Deposit')
        print('3. Complaint')

        selectedOption = int(input('Please select an option:\n'))
        
        if selectedOption == 1:
            value = input('How much would you like to withdraw\n')
            print('take your cash')

        elif selectedOption == 2:
            value = float(input('How much would you like to deposit?\n'))
            print('Balance is ', (total + value))

        elif selectedOption == 3:
            value = input('What issue will you like to report?\n')
            print('Thank you for contacting us')

        else:
            print('Invalid Option selected, please try again')

    else:
        print('Password Incorrect, please try again')

else:
    print('Name not found, please try again')
