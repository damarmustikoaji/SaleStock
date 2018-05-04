import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

logging = None
status = "FAIL"

def ForgotPassword(driver, EMAIL):
    driver = driver
    try:
        user_info = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="header_user_info"]')))
        signin = user_info.find_element_by_xpath('//a[@class="login"]')
        print "Click on "+signin.text
        signin.click()
        try:
            forgot = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,'//p[@class="lost_password form-group"]/a[@title="Recover your forgotten password" and contains(text(), "Forgot")]')))
            print "Click on "+forgot.text
            forgot.click()
            try:
                email = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID,'email')))
                print "Fill email field "+EMAIL
                email.send_keys(EMAIL)
                button = driver.find_element_by_xpath('//button[@type="submit" and @class="btn btn-default button button-medium"]')
                print "Click on button "+button.text
                button.click()
                try:
                    success = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//p[@class="alert alert-success"]')))
                    logging = success.text
                    status = "PASS"
                except Exception as e:
                    try:
                        danger = driver.find_element_by_xpath('//div[@class="alert alert-danger"]')
                        logging = danger.text
                        status = "FAIL"
                    except Exception as e:
                        raise
            except Exception as e:
                raise
        except Exception as e:
            raise
    except Exception as e:
        raise
    return driver, logging, status
