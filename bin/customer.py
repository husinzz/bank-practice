from time import sleep
from os import system


class customer:
    def __init__(self, name, pin, id, balance):
        self.name = name;
        self.pin = pin;
        self.id = id;
        self.balance = balance;


def withdraw(ammount, accountid, list):
    if (list[accountid].balance - ammount) > 0:
        list[accountid].balance -= ammount;
        system('clear')
        print("Success".center(20))
        sleep(1)
    else:
        print("Insufficient Balance");

def deposit(amount, accountid, list):
    list[accountid].balance += amount

def transfer(accountid, list):
    index = 0;
    resid = input('Input recivers ID : '.center(20));

    
    while (resid != list[index].id) and (index <= len(list)-1):
        if (resid == list[index].id):
            print('found')
            # break;      
        index += 1;
    if (resid != list[index].id):
        print('User ID not found')

    print(list[index].name.center(20))
    print(list[index].id.center(20))

    amount = float(input('Ammount to transfer : '))

    if(list[accountid].balance - amount )> 0:
        list[accountid].balance -= amount;
        list[index].balance += amount;
    else:
        system('clear')
        print('INVALID : Balance insufficient')
        sleep(2)
        system('clear')



