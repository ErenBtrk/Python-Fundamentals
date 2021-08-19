import json
import os

class User:
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}

        #load users from .json file
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists("users.json"):
            with open("users.json","r",encoding="utf-8") as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username = user["username"],password = user["password"],email = user["email"])
                    self.users.append(newUser)
            print(self.users)

    def register(self,user : User):
        self.users.append(user)
        self.saveToFile()
        print("User is created.")
        pass
    def login(self,username,password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print("Logged in.")
                break

    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print("Logged out.")

    def identity(self):
        if self.isLoggedIn:
            print(f"username = {self.currentUser.username}")
        else:
            print("You havent logged in.")

    def saveToFile(self):
        list = []
        for user in self.users:
            list.append(json.dumps(user.__dict__))

        with open("users.json","w") as file:
            json.dump(list,file)

repository = UserRepository()


while True:
    print("Menu".center(50,'*'))
    choice = input("1- Register\n2- Login\n3 -Identity\n4 -Log Out\n5 -Exit\nYour Choice : ")
    if choice == '5':
        break
    else:
        if choice == '1':
            username = input("Username : ")
            password = input("Password : ")
            email = input("email : ")

            user = User(username,password,email)
            repository.register(user)

            print(repository.users)
        elif choice == '2':
            if repository.isLoggedIn:
                print("Already logged in.")
            else:
                username = input("Username : ")
                password = input("Password : ")
                repository.login(username,password)

        elif choice == '3':
            repository.identity()
        elif choice == '4' :
            repository.logout() 
        else:
            print("Wrong choice.")

