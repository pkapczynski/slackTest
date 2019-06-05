from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

invite = 'p-channel_sidebar__link--invites'
emailAdress = '//div[contains (@id, "invite_1")]/div/label/div/input[contains (@type, "text")]'
class SlackMain:
    def __init__(self, driver):
        self.driver = driver
    def inviteUser(self):
        self.driver.find_element_by_class_name(invite).click()
    def addNewUser(self, email):
        self.driver.find_element_by_xpath(emailAdress).send_keys(email)
        self.driver.find_element_by_xpath('//div[contains (@id, "invite_1")]/div[contains (@class, "col span_1_of_2")]/label[contains (@class, "full_width")]')
    def sendInvitations(self):
        self.driver.find_element_by_id('admin_invites_submit_btn')

    def createChannel(self):
        self.driver.find_element_by_class_name('p-channel_sidebar__section_heading_plus').click()
