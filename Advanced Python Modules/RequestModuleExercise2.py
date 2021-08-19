import requests
import json

class Github:
    def __init__(self):
        self.api_url = "https://api.github.com"
        self.token =  "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" 

    
    def getUser(self,username):
        response = requests.get(self.api_url+'/users/'+username)
        return response.json()
    
    def getRepos(self,username):
        response = requests.get(self.api_url+"/users/"+username+"/repos")
        return response.json()

    def createRepo(self,name):
        response = requests.post(self.api_url+"/user/repos?access_token="+self.token,json={
            "name" : name,
            "description": "This is a repo created with python requests module",
            "homepage" : "https://yarasareis.com",
            "private" : False,
            "has_issues" : True,
            "has_projects" : True,
            "has_wiki" : True
        })
        return response.json()

github = Github()

while True:
    choice = input("1 -Find User\n2 -Get Repo\n3 -Create Repo\n4 -Exit\nYour Choice : ")
    if(choice == "4"):
        break
    else:
        if(choice == "1"):
            username = input("Username : ")
            result = github.getUser(username)
            print(f"name = {result['name']} public repos :{result['public_repos']} follower :{result['followers']}")
        elif(choice == "2"):
            username = input("Username : ")
            result = github.getRepos(username)
            for repo in result:
                print(repo["name"])
        elif(choice == "3"):
            name = input("Repository name : ")
            result = github.createRepo(name)
            print(result)
        else:
            print("Invalid choice.")
