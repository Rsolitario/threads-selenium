from settings import Settings

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from type_threads import *
from time import sleep
import random

class Sequence:
    sequence = 0
    user_agent = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15',
                  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.0.0',
                  'Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
                  'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1']

    def int_sequence(self):
        self.sequence += 1
        self.sequence = self.sequence % Settings.range_feed       
        return self.sequence
    
    def esperar_ser_clickeable(self, driver, time, selector, xpath_target):
        try:
            return WebDriverWait(driver,
                                 time).until(EC.element_to_be_clickable((selector, xpath_target)))
        except Exception as e:
            if Settings.debug:
                print(f"esperar_ser_clickeable - {xpath_target}")
            else:
                print("time expired!")
        return -1
    
    def login(self):
        self.driver.get(self.url)
        sleep(random.randint(1,6))
        self.esperar_ser_clickeable(self.driver, 10, By.XPATH, Threads.sesion.b_entrar)
        self.driver.find_element(By.XPATH, Threads.sesion.b_entrar).click()
        self.esperar_ser_clickeable(self.driver, 10, By.XPATH, Threads.sesion.i_password)
        sleep(random.randint(1, 6))
        self.driver.find_element(By.XPATH, Threads.sesion.i_user).send_keys(self.username)
        sleep(random.randint(1, 6))
        self.driver.find_element(By.XPATH, Threads.sesion.i_password).send_keys(self.password)
        sleep(random.randint(1,5))
        self.driver.find_element(By.XPATH, Threads.sesion.b_start_sesion).click()
        
        return self