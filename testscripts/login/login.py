import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

logging = None
status = None

def Login(driver, EMAIL, PASSWORD):
    driver = driver
    try:
        user_info = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="header_user_info"]')))
        signin = user_info.find_element_by_xpath('//a[@class="login"]')
        print "Click on "+signin.text
        signin.click()
        try:
            email = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID,"email")))
            password = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID,"passwd")))
            button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID,"SubmitLogin")))
            print "Fill email field : "+EMAIL
            email.send_keys(EMAIL)
            print "Fill password field : "+PASSWORD
            password.send_keys(PASSWORD)
            print "Click on "+button.text
            button.click()
            try:
                alert = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="alert alert-danger"]')))
                logging = alert.text
                time.sleep(3)
                status = "FAIL"
            except Exception as e:
                try:
                    user_info = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="header_user_info"]')))
                    time.sleep(3)
                    assert "My account - My Store" in driver.title
                    logging = "Verify browser title "+driver.title
                    logging = user_info.find_element_by_xpath('//a[@class="account"]').text
                    status = "PASS"
                except Exception as e:
                    raise
        except Exception as e:
            raise
    except Exception as e:
        raise
    return driver, logging, status
