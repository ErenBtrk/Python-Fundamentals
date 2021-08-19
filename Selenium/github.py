from githubUserInfo import username,password
from selenium import webdriver
import time

class Github:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []
    
    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        username = self.browser.find_element_by_xpath('//*[@id="login_field"]')
        password = self.browser.find_element_by_xpath('//*[@id="password"]')

        username.send_keys(self.username)
        password.send_keys(self.password)

        time.sleep(1)

        self.browser.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]').click()

        time.sleep(1)

        self.browser.find_element_by_xpath('/html/body/div[1]/header/div[7]/details/summary').click()

        time.sleep(1)

        self.browser.find_element_by_xpath('/html/body/div[1]/header/div[7]/details/details-menu/a[1]').click()

        time.sleep(1)

        self.browser.find_element_by_xpath('//*[@id="js-pjax-container"]/div[2]/div/div[1]/div/div[4]/div[2]/div[3]/div/a[1]').click()

        time.sleep(1)

    def getFollowers(self):
        items = self.browser.find_elements_by_css_selector('.d-table.table-fixed')

        for i in items:
            self.followers.append(tuple((i.find_element_by_css_selector('.f4.Link--primary').text,i.find_element_by_css_selector('.Link--secondary').text)))
            

    def printFollowers(self):
        for item in self.followers:
            print(item)

github = Github(username,password)
github.signIn()
github.getFollowers()
github.printFollowers()