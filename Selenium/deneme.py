from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
import time


driver = webdriver.Chrome()

url = "https://google.com"
driver.get(url)

searchInput = driver.find_element_by_css_selector("body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input")
clickOn = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[3]/div[2]")
print(clickOn)
searchInput.send_keys("Hello World")

action = ActionChains(driver)
action.move_to_element(clickOn).click().perform()

searchInput.send_keys(Keys.ENTER)

clickOn2 = driver.find_element_by_css_selector('#rso > div:nth-child(1) > div > div > div.yuRUbf > a')

action2 = ActionChains(driver)
action2.move_to_element(clickOn2).click().perform()



