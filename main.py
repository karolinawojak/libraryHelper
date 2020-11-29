from selenium import webdriver
import time

PATH = "F:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://opac.mbp.katowice.pl")

initial_popup_button = driver.find_element_by_id("yui-gen2")
initial_popup_button.click()

driver.close()