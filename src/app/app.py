from src.base.base import *
from src.utils.utils import *
from src.app.app import *
from selenium.webdriver.common.by import By


class RobotClass(Bot):
    def __init__(self):
        super().__init__()
        
        self.DRIVER.get(self.URL)
        
        count = 0
        
        while True:
            if len(self.CPFS) > count and len(self.DATES) > count:
                
                cpf = self.CPFS[count]
                date = self.DATES[count]
                
                if cpf == "" or date == "":
                    break
                
                if not ValidateCpf(cpf=cpf) or not ValidateDate(date=date):
                    print("Invalid date or cpf accepted format cpf:12345678900 date:12072005")
                    break
                
                Sleeping(2)
                cpf = self.receive_value_ainserts_in_field(locator=By.XPATH, path='//*[@id="txtCPF"]', value=cpf)
                Sleeping(2)
                date = self.receive_value_ainserts_in_field(locator=By.XPATH, path='//*[@id="txtDataNascimento"]', value=date)
                Sleeping(2)
                
                captcha_box = self.searching_for_element(locator=By.CSS_SELECTOR, path='div[id="idRepCatchaFrame"]')
                Sleeping(2)
                
                hcaptcha = self.looking_for_element_from_within(element=captcha_box, locator=By.CSS_SELECTOR, path='div[id="hcaptcha"]')
                Sleeping(2)
                
                iframe = self.looking_for_element_from_within(element=hcaptcha, locator=By.CSS_SELECTOR, path='iframe')
                Sleeping(2)
                
                self.change_context(context=iframe)
                Sleeping(2)
                
                checkbox = self.searching_for_element(locator=By.CSS_SELECTOR, path='div[id="checkbox"]')
                
                self.receives_element_and_clicks(element=checkbox, sleep=2)
                Sleeping(2)
                
                self.change_context(activate=False)
                Sleeping(2)
                
                submit = self.searching_for_element(locator=By.CSS_SELECTOR, path='input[id="id_submit"]')
                Sleeping(2)
                
                self.receives_element_and_clicks(element=submit, sleep=2)
                
                Sleeping(2)
                
                
                if self.DRIVER.current_url != self.DOC:
                    continue
                
                find_name_file = self.searching_for_elements(locator=By.CSS_SELECTOR, path='div[class="clConteudoEsquerda"]')
                Sleeping(2)
                
                find_elements_span = self.looking_for_all_elements_from_within(element=find_name_file[0],locator=By.CSS_SELECTOR, path='span')
                
                Sleeping(2)
                
                self.print_file(element=find_elements_span[1])
                count += 1
                continue
            break
        self.DRIVER.quit()