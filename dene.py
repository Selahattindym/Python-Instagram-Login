from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class Instagram():
    def __init__(self,email,password):
        self.webdriver = webdriver.Chrome()
        self.email = email
        self.password = password

    def giris(self):
        self.webdriver.get("https://www.instagram.com/accounts/login/")
        mail_input = self.webdriver.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
        mail_input.send_keys(self.email)
        password_input = self.webdriver.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.ENTER)
        time.sleep(3)

Insta = Instagram("ahmet@gmail.com","123456")
Insta.giris()
time.sleep(20)
