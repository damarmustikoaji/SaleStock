import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

logging = None
status = "FAIL"

def Search(driver, KEYWORD):
    driver = driver
    status = "FAIL"
    try:
        search = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID,"search_query_top")))
        button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "submit_search")))
        print "Fill keyword on search field "+KEYWORD
        search.send_keys(KEYWORD)
        print "Click on button "+button.text
        button.click()
        try:
            heading = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//h1[@class="page-heading  product-listing"]')))
            logging = heading.text
            status = "PASS"
        except Exception as e:
            raise
    except Exception as e:
        raise
    return driver, logging, status
