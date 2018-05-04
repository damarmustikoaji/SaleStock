import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

logging = None
status = None

def CreateAccount(driver, EMAIL):
    driver = driver
    try:
        user_info = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="header_user_info"]')))
        signin = user_info.find_element_by_xpath('//a[@class="login"]')
        print "Click on "+signin.text
        signin.click()
        try:
            email = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID,"email_create")))
            button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID,"SubmitCreate")))
            print "Fill email field "+EMAIL
            email.send_keys(EMAIL)
            print "Click on "+button.text
            button.click()
            time.sleep(3)
            try:
                alert = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,'//div[@class="alert alert-danger"]')))
                logging = alert.find_element_by_xpath('//ol/li').text
            except Exception as e:
                raise
        except Exception as e:
            raise
    except Exception as e:
        raise
    return driver, logging, status
