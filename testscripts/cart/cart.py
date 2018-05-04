import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import random
from random import randint

logging = None
status = "FAIL"

def Cart(driver):
    driver = driver
    try:
        product_list = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,'//ul[@class="product_list grid row"]')))
        product = product_list.find_elements_by_xpath('//div[@class="product-container"]')
        count = len(product)
        print "Ditemukan data "+str(count)
        no = 0
        #pilihan = randint(0,6)
        for choose in product:
            if no < 1:
                hover = ActionChains(driver).move_to_element(choose)
                hover.perform()
                time.sleep(2)
                button = choose.find_element_by_xpath('//a[@class="product-name"]')
                if button.is_displayed():
                    button.click()
                    print "Click more view"
                    status = "PASS"
                    time.sleep(5)
                break
            no = no + 1
    except Exception as e:
        driver.save_screenshot('capture/cart_fail.png')
        time.sleep(3)
        raise
    return driver, logging, status

def Summary(driver):
    driver = driver
    try:
        order_detail = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'center_column')))
        title = order_detail.find_element_by_xpath('//h1[@class="page-heading"]')
        logging = title.text
        print logging
        button = order_detail.find_element_by_xpath('//a[@class="button btn btn-default standard-checkout button-medium"]')
        print "Click on "+button.text
        hover = ActionChains(driver).move_to_element(button)
        hover.perform()
        time.sleep(1)
        button.click()
        status = "PASS"
    except Exception as e:
        driver.save_screenshot('capture/summary_fail.png')
        time.sleep(3)
        raise
    return driver, logging, status

def SignIn(driver, EMAIL, PASSWORD):
    driver = driver
    try:
        order_detail = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'center_column')))
        title = order_detail.find_element_by_xpath('//h1[@class="page-heading"]')
        logging = title.text
        print logging
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
                user_info = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="header_user_info"]/a[@class="logout"]')))
                time.sleep(3)
                logging = "Verify browser title "+driver.title
                logging = user_info.find_element_by_xpath('//a[@class="account"]').text
                status = "PASS"
            except Exception as e:
                raise
    except Exception as e:
        driver.save_screenshot('capture/signin_fail.png')
        time.sleep(3)
        raise
    return driver, logging, status

def Address(driver):
    driver = driver
    komentar = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    try:
        order_detail = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'center_column')))
        title = order_detail.find_element_by_xpath('//h1[@class="page-heading"]')
        logging = title.text
        print logging
        message = driver.find_element_by_id('ordermsg')
        comment = message.find_element_by_xpath('//textarea[@name="message"]')
        comment.send_keys(komentar)
        button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[@name="processAddress" and @class="button btn btn-default button-medium"]')))
        hover = ActionChains(driver).move_to_element(button)
        hover.perform()
        time.sleep(1)
        print "Fill comment field : "+komentar
        print "Click on "+button.text
        button.click()
        status = "PASS"
    except Exception as e:
        driver.save_screenshot('capture/address_fail.png')
        time.sleep(3)
        raise
    return driver, logging, status

def Shipping(driver):
    driver = driver
    try:
        order_detail = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'center_column')))
        title = order_detail.find_element_by_xpath('//h1[@class="page-heading"]')
        logging = title.text
        print logging
        agreement = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'uniform-cgv')))
        print "Click on "+agreement.find_element_by_xpath('//label[@for="cgv"]').text
        agreement.find_element_by_xpath('//label').click()
        button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[@name="processCarrier" and @class="button btn btn-default standard-checkout button-medium"]')))
        time.sleep(1)
        print "Click on "+button.text
        button.click()
        status = "PASS"
    except Exception as e:
        driver.save_screenshot('capture/shipping_fail.png')
        time.sleep(3)
        raise
    return driver, logging, status

def Payment(driver):
    driver = driver
    try:
        order_detail = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'center_column')))
        title = order_detail.find_element_by_xpath('//h1[@class="page-heading"]')
        logging = title.text
        print logging
        hook_payment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'HOOK_PAYMENT')))
        pilih_pay = hook_payment.find_element_by_xpath('//a[@class="bankwire" and @title="Pay by bank wire"]')
        time.sleep(1)
        print "Click on "+pilih_pay.text
        time.sleep(2)
        pilih_pay.click()
        try:
            order_detail = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'center_column')))
            title = order_detail.find_element_by_xpath('//h1[@class="page-heading"]')
            logging = title.text
            print logging
            button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit" and @class="button btn btn-default button-medium"]')))
            time.sleep(1)
            print "Click on "+button.text
            button.click()
            try:
                order_detail = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'center_column')))
                title = order_detail.find_element_by_xpath('//h1[@class="page-heading"]')
                logging = title.text
                print logging
                logging = order_detail.find_element_by_xpath('//div[@class="box"]').text
                status = "PASS"
            except Exception as e:
                raise
        except Exception as e:
            raise
    except Exception as e:
        driver.save_screenshot('capture/payment_fail.png')
        time.sleep(3)
        raise
    return driver, logging, status

def AddToCart(driver):
    driver = driver
    try:
        driver, logging, status = Cart(driver)
        if status == "PASS":
            try:
                description = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'short_description_content')))
                print "Detail Product"
                print "Description : "+description.text
                buy = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID,'buy_block')))
                add_cart = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID,'add_to_cart')))
                button = add_cart.find_element_by_xpath('//button[@name="Submit" and @class="exclusive"]')
                hover = ActionChains(driver).move_to_element(button)
                hover.perform()
                time.sleep(1)
                print "Click on "+button.text
                button.click()
                try:
                    modal = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@id="layer_cart"]')))
                    time.sleep(2)
                    print modal.find_element_by_tag_name('h2').text
                    time.sleep(3)
                    checkout = modal.find_element_by_xpath('//a[@class="btn btn-default button button-medium"]')
                    print "Click on "+checkout.text
                    checkout.click()
                    try:
                        driver, logging, status = Summary(driver)
                        if status == "PASS":
                            try:
                                time.sleep(5)
                                status_login = driver.find_element_by_id("SubmitLogin")
                                if status_login.is_displayed():
                                    driver, logging, status = SignIn(driver, "damar@mailinator.com", "123qwe")
                                try:
                                    driver, logging, status = Address(driver)
                                    if status == "PASS":
                                        try:
                                            driver, logging, status = Shipping(driver)
                                            if status == "PASS":
                                                try:
                                                    driver, logging, status = Payment(driver)
                                                except Exception as e:
                                                    raise
                                        except Exception as e:
                                            raise
                                except Exception as e:
                                    raise
                            except Exception as e:
                                raise
                    except Exception as e:
                        raise
                except Exception as e:
                    raise
            except Exception as e:
                raise
    except Exception as e:
        raise
    return driver, logging, status
