from src.base.base import *
from src.utils.utils import *
from src.app.app import *
from selenium.webdriver.common.by import By
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("bot.log"), logging.StreamHandler()],
)

class RobotClass(Bot):
    def __init__(self):
        super().__init__()

        logging.info("Inicializando o robô...")

        

        try:
            self.DRIVER.get(self.URL)
            logging.info(f"Acessando URL: {self.URL}")
        except Exception as e:
            logging.error(f"Erro ao acessar URL: {e}")
            self.DRIVER.quit()
            raise

        count = 0
        while True:
            try:
                if len(self.CPFS) > count and len(self.DATES) > count:
                    cpf = self.CPFS[count]
                    date = self.DATES[count]

                    if not cpf or not date:
                        logging.warning("CPF ou Data de nascimento vazio. Encerrando execução.")
                        break

                    if not ValidateCpf(cpf=cpf) or not ValidateDate(date=date):
                        logging.error(f"CPF ou Data inválido. CPF: {cpf}, Data: {date}")
                        break

                    logging.info(f"Processando CPF: {cpf} e Data: {date}")

                    Sleeping(2)
                    self.receive_value_and_insert_in_field(locator=By.XPATH, path='//*[@id="txtCPF"]', value=cpf)
                    logging.info("CPF inserido no campo.")

                    Sleeping(2)
                    self.receive_value_and_insert_in_field(locator=By.XPATH, path='//*[@id="txtDataNascimento"]', value=date)
                    logging.info("Data de nascimento inserida no campo.")

                    Sleeping(2)
                    captcha_box = self.searching_for_element(locator=By.CSS_SELECTOR, path='div[id="idRepCatchaFrame"]')

                    Sleeping(2)
                    hcaptcha = self.looking_for_element_from_within(element=captcha_box, locator=By.CSS_SELECTOR, path='div[id="hcaptcha"]')

                    Sleeping(2)
                    iframe = self.looking_for_element_from_within(element=hcaptcha, locator=By.CSS_SELECTOR, path='iframe')

                    Sleeping(2)
                    self.change_context(context=iframe)
                    logging.info("Contexto alterado para iframe do captcha.")

                    Sleeping(2)
                    checkbox = self.searching_for_element(locator=By.CSS_SELECTOR, path='div[id="checkbox"]')
                    self.receives_element_and_clicks(element=checkbox, sleep=2)
                    logging.info("Captcha marcado.")

                    Sleeping(2)
                    self.change_context(activate=False)

                    Sleeping(2)
                    submit = self.searching_for_element(locator=By.CSS_SELECTOR, path='input[id="id_submit"]')
                    self.receives_element_and_clicks(element=submit, sleep=2)
                    logging.info("Formulário enviado.")

                    if self.DRIVER.current_url != self.DOC:
                        logging.warning("Redirecionamento inesperado. Continuando para o próximo registro.")
                        continue

                    find_name_file = self.searching_for_elements(locator=By.CSS_SELECTOR, path='div[class="clConteudoEsquerda"]')
                    Sleeping(2)
                    find_elements_span = self.looking_for_all_elements_from_within(element=find_name_file[0], locator=By.CSS_SELECTOR, path='span')

                    Sleeping(2)
                    self.print_file(element=find_elements_span[1])
                    logging.info(f"Arquivo processado para CPF: {cpf}.")

                    count += 1
                    continue
                break
            except Exception as e:
                logging.error(f"Erro durante a execução: {str(e)}")
        self.DRIVER.quit()
        logging.info("Execução do robô encerrada.")
