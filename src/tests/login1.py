import unittest
from selenium import webdriver
import HtmlTestRunner
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from src.PajeObjects.MyAccountPage import MyAccountPage
from src.PajeObjects.HomePage import HomePage
from src.TestData import TestData

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\\Users\\Xaoc\\PycharmProjects\EstetoPom\\drivers\\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        self.driver.get("https://esteto.net/my-account/")
        login = MyAccountPage(driver)
        login.enter_username("")
        login.enter_password("")
        login.click_login()
        time.sleep(2)
        login.click_logout_from_profile()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Completed")



if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\Xaoc\\PycharmProjects\\EstetoPom\\Reports"))
