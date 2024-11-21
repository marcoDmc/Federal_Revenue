from src.base.base import *
from src.utils.utils import *
from src.app.app import *
from selenium.webdriver.common.by import By


class RobotClass(Bot):
    def __init__(self):
        # Inicializando a classe pai (Bot)
        super().__init__()
        
        # Agora que DRIVER está inicializado, podemos usá-lo
        self.DRIVER.get(self.URL)
        
        cpf = self.receive_value_ainserts_in_field(locator=By.CSS_SELECTOR, path='input[id="txtCPF"]', value=self.CPFS[0])
        
        date = self.receive_value_ainserts_in_field(locator=By.CSS_SELECTOR, path='input[id="txtDataNascimento"]', value=self.DATES[0])
        
        captcha_box = self.searching_for_element(locator=By.CSS_SELECTOR, path='div[id="idRepCatchaFrame"]')
        
        hcaptcha = self.looking_for_element_from_within(element=captcha_box, locator=By.CSS_SELECTOR, path='div[id="hcaptcha"]')
        
        iframe = self.looking_for_element_from_within(element=hcaptcha, locator=By.CSS_SELECTOR, path='iframe')
        
        self.change_context(context=iframe)
        
        checkbox = self.searching_for_element(locator=By.CSS_SELECTOR, path='div[id="checkbox"]')
        
        self.receives_element_and_clicks(element=checkbox, sleep=10)
        
        self.change_context(activate=False)
        
        submit = self.searching_for_element(locator=By.CSS_SELECTOR, path='input[id="id_submit"]')
        self.receives_element_and_clicks(element=submit, sleep=10)
        
        input("press any key for closed")
        self.DRIVER.quit()