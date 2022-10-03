import time
from selenium.webdriver.common.by import By
from selenium .webdriver.common.keys import Keys

class LoginPage:
    textbox_email_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[contains(text(),'Log in')]"
    link_logout_linktext = "Logout"

    def __init__(self, driver):

        self.driver = driver

    def search(self, baseUrl, logger):
        iphone = dict()
        self.driver.get(baseUrl)
        time.sleep(2)

        self.driver.find_element(By.XPATH, '//input[@id="twotabsearchtextbox"]').send_keys("iphone")
        self.driver.find_element(By.XPATH, '//input[@id="nav-search-submit-button"]').click()
        time.sleep(5)
        phone_Type = self.driver.find_element(By.XPATH, '//span[@class="a-size-medium a-color-base a-text-normal"]').text
        if phone_Type == "Apple iPhone 11 (128GB) - Purple":
            self.driver.find_element(By.XPATH, '//span[@class="a-size-medium a-color-base a-text-normal"]').click()

        p = self.driver.current_window_handle

        parent = self.driver.window_handles[1]
        self.driver.switch_to.window(parent)
        logger.info(self.driver.title)
        time.sleep(5)
        model = self.driver.find_element(By.XPATH,
                                    '//tr[@class="a-spacing-small po-model_name"]/td[@class="a-span3"]/span').text
        model_type = self.driver.find_element(By.XPATH,
                                         '//tr[@class="a-spacing-small po-model_name"]/td[@class="a-span9"]/span').text
        memory = self.driver.find_element(By.XPATH, '//tr[@class="a-spacing-small po-memory_storage_capacity"]/td/span').text
        memory_storage = self.driver.find_element(By.XPATH,
                                             '//tr[@class="a-spacing-small po-memory_storage_capacity"]/td[@class="a-span9"]/span').text



        iphone[model]=model_type
        iphone[memory]=memory_storage
        data = dict()
        data["iphone"]=iphone
        logger.info(data)


        return data





