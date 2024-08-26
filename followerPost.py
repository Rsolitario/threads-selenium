from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from time import sleep
import sys, random
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

from type_threads import *
from target_market import *
from settings import *
from master import *
buffer = []

class Bot(Sequence):

    def __init__(self, username:str, password:str):
        self.username = username
        self.password = password
        options = Options()
        options.add_argument("headless")
        if Settings.debug:
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.url = "https://www.threads.net"
        self.url_search = "https://www.threads.net/search?q=%23{}&serp_type=default"
        self.hashtag = Hashtag()
        self.sequence = 0
    
    def scrollTagName(self, num: int):
        for _ in range(num):
            self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
            sleep(Settings.max_sleep_run)
    
    def log(self, text:str):
        if not os.path.exists('logs'):
            os.mkdir('logs')
        with open(f'logs/@logs-{datetime.now()}.txt'.replace(' ', '-').replace(':','-'), 'w') as f:
            f.write(text)
        return self
    
    def buscar(self):
        self.esperar_ser_clickeable(self.driver, 10, By.XPATH, Threads.buscar.b_buscar)     # estoy dentro
        self.driver.get(self.url_search.format(self.hashtag.next(self.sequence)))

        #self.driver.find_element(By.XPATH, Threads.buscar.b_buscar).click()
        #self.esperar_ser_clickeable(self.driver, 10, By.XPATH, Threads.buscar.i_buscar)
        #busqueda = self.driver.find_element(By.XPATH, Threads.buscar.i_buscar).send_keys(Target.hashtag.next()) 
        #sleep(5)
        #busqueda.send_keys(Keys.RETURN)
        #self.esperar_ser_clickeable(self.driver, 10, By.XPATH, Threads.buscar.b_start) # error!
        #self.driver.find_element(By.XPATH, Threads.buscar.i_buscar).click() # error!
        return self
    
    def esperar(self):
        if Settings.debug:
            print(buffer)
        self.log(str(buffer)) # exception!!!
        buffer.clear()
        print('[+] Sleeping')
        sleep(Settings.sleep_time)
    
    def listar_iterar(self):
        try:
            if Settings.debug:
                print('len buffer: ', len(buffer), "sequence: ", self.sequence)
            if len(buffer) >= Settings.maximum_number_of_likes:
                self.esperar()
            
            # Scroll
            self.scrollTagName(Settings.scroll)
            self.esperar_ser_clickeable(self.driver, 10, By.XPATH, Threads.fila_publicaciones.l_post3)
            rows_threads = self.driver.find_elements(By.XPATH, Threads.fila_publicaciones.l_post3)
            size = len(rows_threads)
            print("[+] next thread to click()")
            
            # cambiar por una secuencia predecible
            thread = rows_threads[self.int_sequence()]       
            thread.click()
                        #thread.find_element(By.XPATH, Threads.fila_publicaciones.b_post_start).click()
            if Settings.debug:
                print(thread.id)
            self.esperar_ser_clickeable(self.driver, 10, By.XPATH, Threads.publicacion.b_ver_actividad)
            self.driver.find_element(By.XPATH, Threads.publicacion.b_ver_actividad).click()                 # ver actividad

            self.esperar_ser_clickeable(self.driver, 10, By.XPATH, Threads.publicacion.l_likes)
            like_data = self.driver.find_elements(By.XPATH, Threads.publicacion.l_likes)
                        #for i in like_data:
                        #    print(i.text)
            
            self.esperar_ser_clickeable(self.driver, 10, By.XPATH, Threads.publicacion._l_likes_data)
            likes = self.driver.find_elements(By.XPATH, Threads.publicacion._l_likes_data)
            count:int = 0            
            for like in likes:
                try:
                    count += 1
                    if (count % Threads.publicacion.max_likes_2h) == 0:
                        self.esperar()

                    like.find_element(By.XPATH, Threads.publicacion._l_likes).click()
                    buffer.append(like.text)
                    
                    if Settings.debug:
                        print(count, len(likes))
                    if count - 1 == len(likes): # hora de regresar
                        self.esperar_ser_clickeable(self.driver, 10, By.XPATH, Threads.publicacion.b_time_reset)
                        self.driver.find_element(By.XPATH, Threads.publicacion.b_time_reset)
                        self.driver.back()
                        break
                                
                    if count <= Threads.publicacion.number_selector:
                        continue

                    sleep(random.randint(1, Settings.max_sleep_run))
                except:
                    self.driver.find_element(By.XPATH, Threads.publicacion.b_time_reset)
                    break

            sleep(random.randint(2, Settings.max_sleep_run))
            self.driver.get(self.url_search.format(self.hashtag.next(self.sequence)))
            self.listar_iterar()
        except:
            sleep(random.randint(2, Settings.max_sleep_run))
            self.driver.get(self.url_search.format(self.hashtag.next(self.sequence)))
            self.listar_iterar()

bot = Bot(os.environ.get('USERNAME_THREADS'), os.environ.get('PASSWORD_THREADS'))
bot.login().buscar().listar_iterar()