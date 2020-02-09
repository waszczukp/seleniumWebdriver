import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep
import string
import random

class WizzairCustomerTest(unittest.TestCase):
    def randomWord(self, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def setUp(self):
        options = Options()
        # options.add_argument("--headless")  # Runs Chrome in headless mode.
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(options=options, executable_path='/usr/local/bin/chromedriver')
        self.driver.get("http://wizzair.com")
        sleep(10)
        self.driver.save_screenshot("screenshot.png")
        WebDriverWait(self.driver, 10) \
            .until(EC.presence_of_element_located((By.CLASS_NAME, "navigation")))


    def testRegistration(self):
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(lambda driver: driver.execute_script("return jQuery.active == 0"))
        # print("jquery is done")
        randstr = self.randomWord(5)
        mail = randstr + 'mail@mail'
        password = randstr + 'pass'
        name = randstr + 'name'
        prenumber = '+48'
        number = '123123123'
        country = 'Polska'
        lastname = randstr + 'lastname'
        WebDriverWait(self.driver, 50) \
            .until(EC.presence_of_element_located((By.XPATH, '//button[@data-test="flight-search-submit"]')))
        siginbutton = self.driver.find_element_by_xpath('//button[@data-test="navigation-menu-signin"]')
        siginbutton.click()
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'modal__body')))
        self.driver.find_element_by_css_selector('.login-form__footer button').click()
        WebDriverWait(self.driver, 50) \
            .until(EC.presence_of_element_located((By.CLASS_NAME, 'register-form__content')))
        self.driver.find_element_by_xpath('//input[@data-test="registrationmodal-first-name-input"]').send_keys(name)
        self.driver.find_element_by_xpath('//input[@data-test="registrationmodal-last-name-input"]').send_keys(lastname)
        self.driver.find_element_by_class_name('modal__header').click()
        # self.driver.save_screenshot("screenshot.png")
        self.driver.find_element_by_xpath('//label[@data-test="register-gendermale"]').click()
        self.driver.find_element_by_class_name('phone-number__calling-code-selector__empty__placeholder').click()
        self.driver.find_element_by_name('phone-number-country-code').send_keys(prenumber)
        self.driver.find_element_by_xpath('//input[@data-test="check-in-step-contact-phone-number"]').send_keys(number)
        self.driver.find_element_by_xpath('//input[@data-test="booking-register-email"]').send_keys(mail)
        self.driver.find_element_by_xpath('//input[@data-test="booking-register-password"]').send_keys(password)
        self.driver.find_element_by_xpath('//input[@data-test="booking-register-country"]').send_keys(country)
        self.driver.find_element_by_xpath('//button[@data-test="booking-register-submit"]').click()
        self.driver.save_screenshot("screenshot.png")


if __name__ == '__main__':
    unittest.main(verbosity=2)
