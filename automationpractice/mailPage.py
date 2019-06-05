from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class MailPage:

    def __init__(self, driver):
        self.driver = driver


    def logToOutlok(self):
        self.driver.find_element_by_xpath('//a[contains (text(), "Zaloguj się")]').click()
    def login(self):
        self.driver.find_element_by_xpath('//input[contains (@name, "loginfmt")]').send_keys('kapczynski.test@outlook.com')
    def dalej(self):
        self.driver.find_element_by_xpath('//input[contains (@type, "submit")]').click()
    def password(self):
        self.driver.find_element_by_xpath('//input[contains (@name, "passwd")]').send_keys("P3vsj!!38s!!")












