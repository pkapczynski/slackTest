from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from SlackHome import SlackHome
from mailPage import MailPage
from SlackApp import SlackMain
class SlackTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('/Users/piotrkapczynski/PycharmProjects/teraz to bedzie dzialac/chromedriver')
        cls.driver.get("https://slack.com/signin")
    def test_logToSlack(self):
        driver = self.driver
        time.sleep(3)
        SlackH = SlackHome(driver)
        SlackH.sendDomain()
        SlackH.submitDomain()
        time.sleep(3)
        SlackH.loginInput()
        time.sleep(3)
        SlackH.passwordInput()
        SlackH.signIn()
        time.sleep(2)
        SlackA = SlackMain(driver)

        time.sleep(3)
        SlackA.inviteUser()
        SlackA.addNewUser('kapczynskipiotr@wp.pl')

    def test_inviteUsers(self):
        driver = self.driver



    def tearDownClass(self):
        print('tearDown')



# driver.find_element_by_class_name()





