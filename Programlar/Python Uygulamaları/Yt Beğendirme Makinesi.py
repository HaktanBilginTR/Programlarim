from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
path = "C:\driverler\chromedriver.exe"
url ="https://accounts.google.com/signin/v2/sl/pwd?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Fnext%3D%252F%253Fhl%253Dtr%2526gl%253DTR%26hl%3Dtr%26app%3Ddesktop%26action_handle_signin%3Dtrue&hl=tr&passive=true&service=youtube&uilel=3&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
print("Beğendirme Makinesine Hoş Geldiniz")
email = input("Google Emailinizi Girin :")
sifre = input("Google Şifrenizi Girin :")
begenilecekurl=input("Urlyi girin :")
class hup:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(path)
    def login(self):
        driver = self.driver
        driver.get(url)
        mail = driver.find_element_by_xpath("//input")
        mail.send_keys(self.username)
        mail.send_keys(Keys.RETURN)
        time.sleep(2.5)
        pesvird = driver.find_element_by_xpath("//input[@name='password']")
        pesvird.send_keys(self.password)
        pesvird.send_keys(Keys.RETURN)

    def begen(self):
        driver = self.driver
        time.sleep(2)
        driver.get(begenilecekurl)
        time.sleep(2)
        butonbegen = driver.find_element_by_xpath("//ytd-toggle-button-renderer[@class='style-scope ytd-menu-renderer force-icon-button style-text']")
        butonbegen.click()
viyu = hup(email,sifre)
viyu.login()
viyu.begen()