from selenium import webdriver
import time

PATH = "F:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://opac.mbp.katowice.pl/catalog")

def title_search(title):
    title_searchbar = driver.find_element_by_id("SimpleSearchForm_q")
    search_button = driver.find_element_by_xpath('//button[text()="Szukaj"]')
    title_searchbar.send_keys(title)
    search_button.click()
    time.sleep(5)
    #get_results()

def get_results():
    rows = driver.find_elements_by_xpath("//table[@id='search_result']/tbody/tr")
    rows = rows[1:len(rows)]
    number_of_results = len(rows)

    for i in range(0, number_of_results-1):
        link_to_result = rows[i].find_element_by_link_text("Wyświetl")
        link_to_result.click()
        time.sleep(1)
        driver.back()
        time.sleep(1)
        rows = driver.find_elements_by_xpath("//table[@id='search_result']/tbody/tr")[1:len(rows)]

book_title = "Solaris"
title_search(book_title)
driver.close()
