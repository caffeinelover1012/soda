from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()

url = "https://www.google.com"
browser.get(url)
browser.find_element(by=By.XPATH,value="/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("Arizona State University")
browser.find_element(by=By.XPATH,value="/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(Keys.ENTER)

