from settings import Settings

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from type_threads import *
from time import sleep
import random

class Sequence:
    sequence = 0

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
        self.esperar_ser_clickeable(self.driver, 10, By.XPATH, Threads.sesion.b_entrar)
        self.driver.find_element(By.XPATH, Threads.sesion.b_entrar).click()
        self.esperar_ser_clickeable(self.driver, 10, By.XPATH, Threads.sesion.i_password)
        self.driver.find_element(By.XPATH, Threads.sesion.i_user).send_keys(self.username)
        self.driver.find_element(By.XPATH, Threads.sesion.i_password).send_keys(self.password)
        sleep(random.randint(1,5))
        self.driver.find_element(By.XPATH, Threads.sesion.b_start_sesion).click()
        
        return self