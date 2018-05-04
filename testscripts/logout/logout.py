import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

logging = None
status = "FAIL"

def Logout(driver):
    driver = driver
    status = "FAIL"
    try:
        user_info = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="header_user_info"]')))
        signout = user_info.find_element_by_xpath('//a[@class="logout"]')
        print signout.text+" ditemukan"
        logging = signout.text
        print "Click on "+signout.text
        signout.click()
        try:
            user_info = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="header_user_info"]')))
            signin = user_info.find_element_by_xpath('//a[@class="login"]')
            print "Verify menu "+signin.text
            logging = "Browser title "+driver.title
            status = "PASS"
        except Exception as e:
            raise
    except Exception as e:
        logging = "current url : "+driver.current_url
    return driver, logging, status
