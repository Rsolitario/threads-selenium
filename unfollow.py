from type_threads import *
from selenium import webdriver
from master import *
import random
from time import sleep
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os

load_dotenv()


class Unfollow(Sequence):

    def __init__(self, username:str, password:str) -> None:
        self.username = username
        self.password = password
        options = Options()
        options.add_argument("headless")
        if Settings.debug:
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.url = 'https://www.threads.net/'

    def reset(self):
        self.esperar_ser_clickeable(self.driver, 10, By.XPATH, Threads.buscar.b_buscar)
        self.driver.get(self.url)
        
        return self

    def perfil(self):
        self.esperar_ser_clickeable(self.driver, 20, By.XPATH, Threads.navegacion_boton_perfil.perfil)
        self.driver.find_element(By.XPATH, Threads.navegacion_boton_perfil.perfil).click()
        
        return self

    def link_follow(self):
        self.esperar_ser_clickeable(self.driver, 20, By.XPATH, 
                                    Threads.perfil_unfollow.perfil_follow)
        self.driver.find_element(By.XPATH, Threads.perfil_unfollow.perfil_follow).click()

        self.esperar_ser_clickeable(self.driver, 10, By.XPATH, 
                                    Threads.perfil_unfollow.b_follow)
        self.driver.find_element(By.XPATH, Threads.perfil_unfollow.b_follow).click()
        sleep(10)
        self.esperar_ser_clickeable(self.driver, 10, By.XPATH, 
                                    Threads.perfil_unfollow._l_b_follows1)
        _l_b_follow = self.driver.find_elements(By.XPATH, Threads.perfil_unfollow._l_b_follows1)
        
        cont = 1
        for item in _l_b_follow:
            item.click()


        #self.esperar_ser_clickeable(self.driver, 10, By.XPATH, Threads.perfil_unfollow.perfil_unfollow)
        #self.driver.find_element(By.XPATH, Threads.perfil_unfollow.perfil_unfollow)

        
        #self.perfil().link_follow(n - 1)
       
            
            sleep(random.randint(10, Settings.max_sleep_run))
        
            cont = cont % Settings.maximum_number_of_likes
            if cont == 0:
                print("[+] Sleeping")
                sleep(Settings.sleep_time)
            cont += 1
        
        return self
    
    def unfollower(self):
        self.login().reset().perfil().link_follow()
        self.driver.close()

if '__main__' == __name__:
    e = Unfollow(os.environ.get('USERNAME_THREADS'), os.environ.get('PASSWORD_THREADS'))
    e.unfollower()