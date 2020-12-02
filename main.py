from selenium import webdriver
import time

PATH = "F:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://opac.mbp.katowice.pl")

def close_initial_popup():
    initial_popup_button = driver.find_element_by_id("yui-gen2")
    initial_popup_button.click()

def title_search(title):
    title_searchbar = driver.find_element_by_id("IdTxtSz1")
    search_button = driver.find_element_by_id("search-zlozone")
    title_searchbar.send_keys(title)
    search_button.click()
    get_results()

def get_results():
    rows = driver.find_elements_by_xpath("//table[@id='search_result']/tbody/tr")

    for el in rows:
        print(el.text)

book_title = "Solaris"
close_initial_popup()
title_search(book_title)
driver.close()