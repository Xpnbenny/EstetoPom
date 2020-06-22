from src.Locators.Locators import Locators


class MyAccountPage:

    def __init__(self, driver):
        self.driver = driver
        self.log_field_username = Locators.log_field_username
        self.log_field_password = Locators.log_field_password
        self.reg_field_email = Locators.reg_field_email
        self.reg_field_password = Locators.reg_field_password
        self.login_button = Locators.login_button
        self.register_button = Locators.register_button
        self.logout_from_profile = Locators.logout_from_profile
        self.logout_link = Locators.logout_link
        self.back_previous_page = Locators.back_previous_page
        self.begin_link = Locators.begin_link




    def enter_username(self, username):
        self.driver.find_element_by_xpath(self.log_field_username).clear()
        self.driver.find_element_by_xpath(self.log_field_username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.log_field_password).clear()
        self.driver.find_element_by_xpath(self.log_field_password).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button).click()

    def click_logout_from_profile(self):
        self.driver.find_element_by_xpath(self.logout_from_profile).click()




