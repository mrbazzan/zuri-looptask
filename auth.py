
import random

accountNumberFromUser = 0

database = {
    7369242920: ['Abdulwasiu', 'Apalowo', 'baz@hng.team', 'password', 0]
}


def register():
    print("*** Register ***")
    email = input('What is your email address? ')
    first_name = input('What is your first name? ')
    last_name = input('What is your last name? ')
    password = input('Password >>>  ')

    accountNumber = generateAccountNumber()
    database[accountNumber] = [first_name, last_name, email, password, 0]

    print('Your account number is {}'.format(accountNumber))
    login()


def login():
    print('**** Log in to your account ****')

    global accountNumberFromUser
    accountNumberFromUser = int(input("Enter your account number: "))

    password = input('Enter your password: ')

    for accountNumber, userDetails in database.items():
        if accountNumberFromUser == accountNumber:
            if userDetails[3] == password:
                bankOperation(userDetails)

    print('Invalid account or password')
    login()


def bankOperation(user):
    print('...Welcome {} {}............'.format(user[0], user[1]))
    isValid = True
    while isValid:
        selectedOption = int(input("""
What would you like to do?
1 - Check Balance
2 - Deposit
3 - Withdraw
4 - Logout
5 - Exit
"""))
        if selectedOption in [1, 2, 3, 4, 5]:
            isValid = False
        if selectedOption == 1:
            print('Current balance is {}'.format(getAccountBalance(database)))
            anotherOperation()
        elif selectedOption == 2:
            depositOperation()
        elif selectedOption == 3:
            withdrawalOperation()
        elif selectedOption == 4:
            login()
        elif selectedOption == 5:
            exit()
        else:
            print('Invalid option selected')


def withdrawalOperation():
    amountToWithdraw = int(input("Enter the amount you want to withdraw: "))
    if database[accountNumberFromUser][-1] >= amountToWithdraw:
        database[accountNumberFromUser][-1] -= amountToWithdraw
    else:
        print('Amount is more than current balance')
    print('Current balance is: {}'.format(database[accountNumberFromUser][-1]))
    anotherOperation()


def depositOperation():
    amountToDeposit = int(input("Enter the amount you want to deposit: "))
    database[accountNumberFromUser][-1] += amountToDeposit

    print('Current balance is: {}'.format(database[accountNumberFromUser][-1]))
    anotherOperation()


def generateAccountNumber():
    return random.randrange(1111111111, 9999999999)


def anotherOperation():
    another_operation = int(input("Do you want to perform another operation (1) yes (2) no: "))
    if another_operation == 1:
        login()
    elif another_operation == 2:
        exit()
    else:
        anotherOperation()


def getAccountBalance(data):
    return data[accountNumberFromUser][-1]


def init():

    print('Welcome to bankBaz')
    validOption = True
    while validOption:
        haveAccount = int(input("""Do you have an account with us?
1 (yes)
2 (no)
"""))
        if haveAccount in [1, 2]:
            validOption = False
        if haveAccount == 1:
            login()
        elif haveAccount == 2:
            print(register())
        else:
            print('You have selected an invalid option')


init()
