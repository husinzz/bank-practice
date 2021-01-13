from bin.customer import customer as cs

# class teller:
#     def __init__(self, name, uid, rank,pin):
#         self.name = name;
#         self.uid = uid;
#         self.pin = pin;
#         self.rank = rank;


def createAccount(list):
    list.append(cs(
        input("Account Name"),
        input("Account PIN"),
        'CS' + str(len(list)),
        0
    ));