import unittest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class AutomationPracticeTest(unittest.TestCase):
    def randomWord(self, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://automationpractice.com/index.php")
        WebDriverWait(self.driver, 10) \
            .until(EC.presence_of_element_located((By.CLASS_NAME, "login")))

    def testRegistration(self):
        randstr = self.randomWord(5)
        mail = randstr + 'mail@mail.com'

        def fillwithdata(type, element, data):
            if type == "id":
                self.driver.find_element_by_id(element).send_keys(data)
            elif type == "class":
                self.driver.find_element_by_class_name(element).send_keys(data)

        def click(type, element):
            if type == "id":
                self.driver.find_element_by_id(element).click()
            elif type == "class":
                self.driver.find_element_by_class_name(element).click()

        def wait(time, element):
            WebDriverWait(self.driver, time) \
                .until(EC.presence_of_element_located((By.ID, element)))

        def getvalue(type, element, attribute):
            global value
            if type == "id":
                value = self.driver.find_element_by_id(element).get_attribute(attribute)
            elif type == "class":
                value = self.driver.find_element_by_class_name(element).get_attribute(attribute)
            return value

        def assertion(val_a, val_b):
            self.assertEqual(val_a, val_b, "values %s and %s are not equal" % (val_a, val_b))

        click('class', 'login')
        wait(10, 'email_create')
        fillwithdata('id', 'email_create', mail)
        click('id', 'SubmitCreate')
        wait(10, 'id_gender1')
        click('id', 'id_gender1')
        fillwithdata('id', 'customer_firstname', 'Name')
        fillwithdata('id', 'customer_lastname', 'Surname')
        usedmail = getvalue('id', 'email', 'value')
        assertion(usedmail, mail)
        # usedmail = self.driver.find_element_by_id('email').get_attribute('value')
        # self.assertEqual(mail, usedmail, "mails %s and %s are not equal" % (mail, usedmail))
        # self.driver.find_element_by_id('passwd').send_keys('pass123')
        # day = Select(self.driver.find_element_by_id('days'))
        # day.select_by_value('11')
        # Select(self.driver.find_element_by_id('months')).select_by_visible_text('April ')
        # Select(self.driver.find_element_by_id('years')).select_by_value('2001')
        # self.driver.find_element_by_id('company').send_keys('my company')
        # self.driver.find_element_by_id('address1').send_keys('street')
        # self.driver.find_element_by_id('address2').send_keys('other street')
        # self.driver.find_element_by_id('city').send_keys('city')
        # self.driver.find_element_by_id('id_state').send_keys('Alabama')
        # self.driver.find_element_by_id('postcode').send_keys('12345')
        # self.driver.find_element_by_id('phone').send_keys('322189112')
        # self.driver.find_element_by_id('alias').clear()
        # self.driver.find_element_by_id('alias').send_keys('address')
        # self.driver.find_element_by_id('submitAccount').click()
        # page = self.driver.find_element_by_class_name('page-heading').get_attribute("innerText")
        # expectedpage = "MY ACCOUNT"
        # self.assertEqual(page, expectedpage, "page title obtained %s and expected %s are not equal" % (page, expectedpage))


if __name__ == '__main__':
    unittest.main(verbosity=2)
