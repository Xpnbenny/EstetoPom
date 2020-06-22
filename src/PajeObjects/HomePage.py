from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from src.Locators.Locators import Locators


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.log_reg_button = Locators.log_reg_button
        self.log_reg_field_username = Locators.log_reg_field_username
        self.log_reg_field_password = Locators.log_reg_field_password
        self.log_reg_login_button = Locators.log_reg_login_button


    def is_visible(self, log_reg_button):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(log_reg_button))
        return bool(log_reg_button)

    def hover_to(self, log_reg_button):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(log_reg_button))
        ActionChains(self.driver).move_to_element(log_reg_button).perform()

    def hover_log_reg_button(self):
        self.driver.find_element_by_xpath(self.log_reg_button).move_to_element()

    def enter_username(self, username):
        self.driver.find_element_by_xpath(self.log_reg_field_username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.log_reg_field_password).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.log_reg_login_button).click()

