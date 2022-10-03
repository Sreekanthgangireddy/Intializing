import pytest
from selenium import webdriver
from pageObject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test001_Login:
    baseURL = ReadConfig.applicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen().get_logger()

    def test_login(self,setup):
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.lp.search(self.baseURL, self.logger)

        act_title = self.driver.title
        self.logger.info(act_title)
        if act_title == 'Apple iPhone 11 (128GB) - Purple : Amazon.in: Electronics':
            self.logger.info("***********************test_login is passed******************")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.logger.error("********************test_login is failed***********************")
            assert False