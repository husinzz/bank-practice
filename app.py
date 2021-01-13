from time import sleep
from os import system


from bin.teller import *
from bin.customer import customer as cs
from bin.customer import *

system('clear')

customers = []

if not customers:
    print('List is empty.')
    exit();

for index in range(len(customers)):
    print('bank rumah'.center(20))
    name = input('Masukan nama : ')
    pin = input('Masukan pin : ')

    if (name == customers[index].name and pin == customers[index].pin):
        system('clear')
        break
    else:
        system('clear');
        print('Invalid account'.center(20))
        sleep(1)
        system('clear')

    
print(
    '''
    1. Withdraw
    2. Deposit
    3. Transfer
    '''
)

index = int(0)
choice = input()

if (choice == '1'):
    amount = input('Enter ammount : ');
    withdraw(float(amount), index, customers)
    print('Your current balance : ', str(customers[index].balance))
elif (choice == '2'):
    amount = input('Enter ammount : ');
    deposit(float(amount), index, customers)
    print('Your current balance : ', str(customers[index].balance))
elif (choice == '3'):
    transfer(0,customers);