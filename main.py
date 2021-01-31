from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "F:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://opac.mbp.katowice.pl/catalog")

def title_search(title):
    title_searchbar = driver.find_element_by_id("SimpleSearchForm_q")
    search_button = driver.find_element_by_xpath('//button[text()="Szukaj"]')
    title_searchbar.send_keys(title)
    choose_search_option()
    search_button.click()
    time.sleep(5)
    get_results()

def choose_search_option():
    option_dropdown_list = driver.find_element_by_id("indexChooserLabel")
    option_dropdown_list.click()
    search_option = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@data-id=2]')))
    search_option.click()
    time.sleep(5)

def get_results():
    # ToDo: add wait
    rows = driver.find_elements_by_xpath("//article[@data-type='cataloged']")
    number_of_results = len(rows)

    for i in range(0, number_of_results-1):
        link_to_result = rows[i].find_element_by_partial_link_text(book_title)
        link_to_result.click()
        time.sleep(1)
        library_number = driver.find_element_by_partial_link_text('Filia')
        print(library_number.text)
        driver.back()
        time.sleep(1)
        rows = driver.find_elements_by_xpath("//article[@data-type='cataloged']")


book_title = "Solaris"
title_search(book_title)
driver.close()
