from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json, time


# Definindo a classe Bot
class Bot:
    def __init__(self):
        with open("bin/config.json", "r") as file:
            self.config = json.load(file)

        self.URL = self.config["BOT"]["URL"]
        self.CPFS = self.config["BOT"]["CPFS"]
        self.DATES = self.config["BOT"]["DATES"]
        self.OPTIONS = ChromeOptions()
        self.DRIVER = webdriver.Chrome(options=self.OPTIONS)
        self.DRIVER.maximize_window()
        
    def receive_value_ainserts_in_field(self, locator, path, value):
        time.sleep(10)
        self.DRIVER.find_element(locator, path).send_keys(value)
        
    def searching_for_element(self, locator, path):
        wait = WebDriverWait(self.DRIVER, 30)
        captchaFrame = wait.until(EC.visibility_of_element_located((locator, path)))
        return captchaFrame

        
    def looking_for_element_from_within(self, element, locator, path):
        return element.find_element(locator, path)

    
    def change_context(self,context=None,activate=True):
        if activate:
            return self.DRIVER.switch_to.frame(context)
        else:
            return self.DRIVER.switch_to.default_content()
    
    def receives_element_and_clicks(self, element, sleep):
        time.sleep(sleep)
        element.click()
        
    def logs(el):
        print(el)