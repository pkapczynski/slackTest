from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

getStartedButton = '//a[contains (@href, "https://slack.com/get-started")]'
createNewWorkspace = "[data-option=create]"
loginInput = 'email'
password = 'password'
submitTeamDomain = 'submit_team_domain'
signIn = 'signin_btn'
singUpEmail = 'signup_email'
confirmEmailButton = 'submit_btn'
url = 'testslack-p3b1335'

class SlackHome:
    def __init__(self, driver):
        self.driver = driver
    def getStarted(self):
        self.driver.find_element_by_xpath(getStartedButton).click()
    def createNewWorkspace(self):

        self.driver.find_element(By. CSS_SELECTOR, createNewWorkspace).click()
    def sendDomain(self):
        self.driver.find_element_by_id('domain').send_keys(url)
    def submitDomain(self):
        self.driver.find_element_by_id('submit_team_domain').click()
    def loginInput(self):
        self.driver.find_element_by_id(loginInput).send_keys('kapczynski.test@outlook.com')
    def passwordInput(self):
        self.driver.find_element_by_id(password).send_keys('t0p$cret')
    def submitDomain(self):
        self.driver.find_element_by_id(submitTeamDomain).click()

    def signIn(self):
        self.driver.find_element_by_id(signIn).click()
    def signUpEmail(self):
        self.driver.find_element_by_id(singUpEmail).send_keys('kapczynski.test@outlook.com')
    def confirmEmail(self):
        self.driver.find_element_by_id(confirmEmailButton).click()
