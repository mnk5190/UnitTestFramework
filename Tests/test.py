import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
import HTMLTestRunner
import HtmlTestRunner
from HtmlTestRunner import HTMLTestRunner
from Pages.AddtoCart import AddtoCart1
from Pages.LoginPage import LoginPage

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/khan/Downloads/chromedriver_win32/chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        driver.get("https://www.ebay.ca")

        login = LoginPage(driver)
        login.signin_button()
        login.enter_username("pfbmnf@gmail.com")
        login.enter_password("5190@MNABILK")
        login.enter_Login()

        AddtoCart = AddtoCart1(driver)
        AddtoCart.search_item("Mobile")
        AddtoCart.addtoCart()
        AddtoCart.logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output="C:/Users/khan/Desktop/run"),verbosity = 2)
