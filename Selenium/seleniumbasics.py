from selenium import webdriver
import time

driver = webdriver.Chrome()
url = "http://github.com"
driver.get(url)

time.sleep(2)
driver.maximize_window()    
driver.save_screenshot("github.com-homepage.png")

url2 = "http://github.com/ErenBtrk"
driver.get(url2)

print(driver.title)

if "ErenBtrk" in driver.title:
    driver.save_screenshot("github-erenbtrk.png")

time.sleep(2)

driver.back()
time.sleep(2)

driver.close()