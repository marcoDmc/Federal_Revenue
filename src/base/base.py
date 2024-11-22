from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..utils.utils import *
import json, time, pyautogui
from selenium.common.exceptions import TimeoutException



class Bot:
    def __init__(self):
        with open("bin/config.json", "r") as file:
            self.config = json.load(file)

        self.URL = self.config["BOT"]["URL"]
        self.CPFS = self.config["BOT"]["CPFS"]
        self.DATES = self.config["BOT"]["DATES"]
        self.DOC = self.config["BOT"]["DOC_URL"]
        self.OPTIONS = ChromeOptions()
        self.DRIVER = webdriver.Chrome(options=self.OPTIONS)
        self.DRIVER.maximize_window()
        
    def receive_value_ainserts_in_field(self, locator, path, value):
        wait = WebDriverWait(self.DRIVER, 2)
        wait.until(EC.presence_of_element_located((locator, path))).send_keys(value)
            
    def searching_for_element(self, locator, path):
        wait = WebDriverWait(self.DRIVER, 2)
        captchaFrame = wait.until(EC.visibility_of_element_located((locator, path)))
        return captchaFrame

    def searching_for_elements(self, locator, path):
        try:
            wait = WebDriverWait(self.DRIVER, 2)
            elements = wait.until(EC.visibility_of_all_elements_located((locator, path)))
            return elements
        except TimeoutException as e:
            print(f"Timeout when searching for elements: {path}")
            return []
        
    def looking_for_element_from_within(self, element, locator, path):
        return element.find_element(locator, path)

    def looking_for_all_elements_from_within(self, element, locator, path):
        return element.find_elements(locator, path)
    
    def change_context(self,context=None,activate=True):
        if activate:
            return self.DRIVER.switch_to.frame(context)
        else:
            return self.DRIVER.switch_to.default_content()
    
    def receives_element_and_clicks(self, element, sleep):
        time.sleep(sleep)
        element.click()
        
    def print_file(self,element):
        #criando pasta para armazenar os arquivos
        CreateFolder(name='Downloads')
        Sleeping(10)
        
        #comando para imprimir documento
        pyautogui.hotkey('ctrl', 'p')
        Sleeping(2)  
        pyautogui.press('enter')
        Sleeping(5)
        
        #inserindo caminho da pasta
        pyautogui.hotkey('ctrl','l')
        pyautogui.write('C:/Downloads', interval=0.10)
        pyautogui.press('enter')
        Sleeping(2)
        PressKeyTimes(7)
        
        
        filename = str(element.text).split(":")[1].lower()
        
        #gerando numeros aleatorios para evitar problemas de nome
        #de arquivos iguais
        number = GenerateNumber()
        
        #inserindo nome de arquivo
        pyautogui.typewrite(f'{filename}-{number}', interval=0.10)
        pyautogui.press('enter')
        Sleeping(5)
        
        self.DRIVER.back()
        
