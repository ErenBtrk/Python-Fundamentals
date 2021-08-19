#Bank Application

account1 = {
    "name" : "Ali Veli",
    "accountNo" : "12342424",
    "balance" : 3000,
    "overdraft" :2000
}

account2 = {
    "name" : "Isa Musa",
    "accountNo" : "12345678",
    "balance" : 2000,
    "overdraft" :1000
}

def withdraw(account,amount):
    print(f'Hello {account["name"]}')

    if(account["balance"] >= amount):
        account["balance"] -= amount
        print("You can withdraw.")
        checkBalance(account1)
    else:
        total = account["balance"]+account["overdraft"]

        if(total >= amount):
            overdraftBool = input("Do you want to overdraft (y/n)")
            if(overdraftBool == "y"):
                overdraftAmount = amount - account["balance"] 
                account["balance"] = 0
                account["overdraft"] -= overdraftAmount
                print("You can take your money.")
                checkBalance(account1)
            else:
                print(f'You have {account["balance"]} in {account["accountNo"]} account no.')
        else:
            print(f"Sorry.Your balance is not enough")
            checkBalance(account1)

def checkBalance(account):
    print(f'You have {account["balance"]} USD in your {account["accountNo"]} account no.\nYou have {account["overdraft"]} USD in your overdraft account. ')


withdraw(account1,3000)
print("***********************")
withdraw(account1,2000)
