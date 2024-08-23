from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
import sys, random
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

from type_threads import *
from target_market import *

class Bot:

    def __init__(self, username:str, password:str):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.url = "https://www.threads.net"
        self.url_search = "https://www.threads.net/search?q=%23{}&serp_type=default"

    def esperar_ser_clickeable(self, driver, time, selector, xpath_target):
        try:
            return WebDriverWait(driver,
                                 time).until(EC.element_to_be_clickable((selector, xpath_target)))
        except Exception as e:
            print(f"esperar_ser_clickeable - {xpath_target}")
        return -1
    
    def log(self, text:str):
        if not os.path.exists('logs'):
            os.mkdir('logs')
        with open(f'@logs {datetime.now()}', 'w') as f:
            f.write(text)
        return self

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
    
    def buscar(self):
        self.esperar_ser_clickeable(self.driver, 10, By.XPATH, Threads.buscar.b_buscar)     # estoy dentro
        self.driver.get(self.url_search.format(Target.hashtag.next()))

        #self.driver.find_element(By.XPATH, Threads.buscar.b_buscar).click()
        #self.esperar_ser_clickeable(self.driver, 10, By.XPATH, Threads.buscar.i_buscar)
        #busqueda = self.driver.find_element(By.XPATH, Threads.buscar.i_buscar).send_keys(Target.hashtag.next()) 
        #sleep(5)
        #busqueda.send_keys(Keys.RETURN)
        #self.esperar_ser_clickeable(self.driver, 10, By.XPATH, Threads.buscar.b_start) # error!
        #self.driver.find_element(By.XPATH, Threads.buscar.i_buscar).click() # error!
        return self
    
    def listar_iterar(self):
        self.esperar_ser_clickeable(self.driver, 10, By.XPATH, Threads.fila_publicaciones.l_post)
        rows_threads = self.driver.find_elements(By.XPATH, Threads.fila_publicaciones.l_post)
        size = len(rows_threads)
        sleep(5)
        print("[+] siguiente hilo por clickear()")
        thread = rows_threads[random.randint(1, size)]
        thread.click()
                    #thread.find_element(By.XPATH, Threads.fila_publicaciones.b_post_start).click()
        print(thread.id)
        sleep(5)
        self.esperar_ser_clickeable(self.driver, 10, By.XPATH, Threads.publicacion.b_ver_actividad)
        self.driver.find_element(By.XPATH, Threads.publicacion.b_ver_actividad).click()                 # ver actividad

        self.esperar_ser_clickeable(self.driver, 10, By.XPATH, Threads.publicacion.l_likes)
        like_data = self.driver.find_elements(By.XPATH, Threads.publicacion.l_likes)
                    #for i in like_data:
                    #    print(i.text)
        sleep(5)
        self.esperar_ser_clickeable(self.driver, 10, By.XPATH, Threads.publicacion._l_likes_data)
        likes = self.driver.find_elements(By.XPATH, Threads.publicacion._l_likes_data)
        count:int = 0
        buffer = []
        for like in likes:
            try:
                count += 1
                if (count % Threads.publicacion.max_likes_2h) == 0:
                    self.log(str(buffer))
                    buffer.clear()
                    print('[+] Sleeping')
                    sleep(60 * 60 * 2)

                    like.find_element(By.XPATH, Threads.publicacion._l_likes).click()
                    buffer.append(like.text)

                    print(count, len(likes))
                    if count - 1 == len(likes): # hora de regresar
                        self.esperar_ser_clickeable(self.driver, 10, By.XPATH, Threads.publicacion.b_time_reset)
                        self.driver.find_element(By.XPATH, Threads.publicacion.b_time_reset)
                        self.driver.back()
                        break
                            
                    if count <= Threads.publicacion.number_selector:
                        continue
            except:
                self.driver.find_element(By.XPATH, Threads.publicacion.b_time_reset)
                break
        
        self.driver.get(self.url_search.format(Target.hashtag.next()))
        self.listar_iterar()

bot = Bot(os.environ.get('USERNAME_THREADS'), os.environ.get('PASSWORD_THREADS'))
bot.login().buscar().listar_iterar()