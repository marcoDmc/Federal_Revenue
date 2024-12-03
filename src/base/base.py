from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from ..utils.utils import *
import json, time, pyautogui, logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("bot.log"), logging.StreamHandler()],
)

class Bot:
    def __init__(self):
        with open("bin/config.json", "r") as file:
            self.config = json.load(file)

        self.URL = self.config["BOT"]["URL"]
        self.CPFS = self.config["BOT"]["CPFS"]
        self.DATES = self.config["BOT"]["DATES"]
        self.DOC = self.config["BOT"]["DOC_URL"]

        self.OPTIONS = Options()
        self.OPTIONS.add_argument('--no-sandbox')

        self.SERVICE = Service(ChromeDriverManager().install())
        self.DRIVER = webdriver.Chrome(service=self.SERVICE, options=self.OPTIONS)
        self.DRIVER.maximize_window()

    def receive_value_and_insert_in_field(self, locator, path, value):
        wait = WebDriverWait(self.DRIVER, 2)
        wait.until(EC.presence_of_element_located((locator, path))).send_keys(value)

    def searching_for_element(self, locator, path):
        wait = WebDriverWait(self.DRIVER, 2)
        return wait.until(EC.visibility_of_element_located((locator, path)))

    def searching_for_elements(self, locator, path):
        try:
            wait = WebDriverWait(self.DRIVER, 2)
            return wait.until(EC.visibility_of_all_elements_located((locator, path)))
        except TimeoutException:
            logging.error(f"Timeout when searching for elements: {path}")
            return []

    def looking_for_element_from_within(self, element, locator, path):
        return element.find_element(locator, path)

    def looking_for_all_elements_from_within(self, element, locator, path):
        return element.find_elements(locator, path)

    def change_context(self, context=None, activate=True):
        if activate:
            self.DRIVER.switch_to.frame(context)
        else:
            self.DRIVER.switch_to.default_content()

    def receives_element_and_clicks(self, element, sleep):
        time.sleep(sleep)
        element.click()

    def print_file(self, element):
        pyautogui.FAILSAFE = False
        CreateFolder(name='Downloads')
        Sleeping(10)

        pyautogui.hotkey('ctrl', 'p')
        Sleeping(2)
        pyautogui.press('enter')
        Sleeping(5)

        pyautogui.hotkey('ctrl', 'l')
        pyautogui.write('C:/Downloads', interval=0.10)
        pyautogui.press('enter')
        Sleeping(2)
        PressKeyTimes(7)

        filename = str(element.text).split(":")[1].lower()
        number = GenerateNumber()

        pyautogui.typewrite(f'{filename}-{number}', interval=0.10)
        pyautogui.press('enter')
        Sleeping(5)

        self.DRIVER.back()