from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Instagram:
    def __init__(self, email, password):
        self.driver = webdriver.Chrome()
        self.email = email
        self.password = password

    def giris(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        mail_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
        mail_input.send_keys(self.email)

        password_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
        password_input.send_keys(self.password)

        password_input.send_keys(Keys.ENTER)
        time.sleep(10)

# Kullanım örneği
if __name__ == "__main__":
    bot = Instagram("youremail@gmail.com", "yourpassword")
    bot.giris()
