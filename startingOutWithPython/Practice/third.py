#Functions and Lmbda Functions
username='nicky'
password='Nicholas@98'

userName=input('Enter username: ')
Password=input("Enter your password: ")

def login(userName, Password):

    if ((userName==username) and (Password==password)):
        print('Login successful')
    else:
        print("Invalid username or password")

login(userName, Password)