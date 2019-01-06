from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
path = "C:\driverler\chromedriver.exe"
url = "https://www.instagram.com"
tempmail = "https://temp-mail.org/tr/option/change/"
followlanacak = "ulaþ sinan yýldýrým"
necat = "h2arda"
sayi = 0
sifre_base="arda"
class bot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(path)

    def instagram_kurma(self):
        driver = self.driver
        time.sleep(2)
        driver.get(url)
        time.sleep(2)
        mail_giris = driver.find_element_by_xpath("//input[@name='emailOrPhone']")
        mail_giris.send_keys(necat+str(sayi)+"@koyukodal.com")
        adsoyad = driver.find_element_by_xpath("//input[@name='fullName']")
        adsoyad.send_keys(necat+str(sayi))
        time.sleep(2)
        yenile = driver.find_element_by_xpath("//span[@class='coreSpriteInputRefresh Szr5J']")
        yenile.click()
        time.sleep(1)



        sifre_giris = driver.find_element_by_xpath("//input[@name='password']")
        sifre_giris.send_keys(sifre_base+str(sayi)+str(sayi))
        time.sleep(3)
        sifre_giris.send_keys(Keys.RETURN)
        time.sleep(5)


    def follow(self):
        driver = self.driver
        time.sleep(2)

        simdi_degil = driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']")
        time.sleep(1)
        simdi_degil.click()
        arama_tik = driver.find_element_by_xpath("//div[@class='eyXLr wUAXj ']")
        arama_tik.click()
        arama_text = driver.find_element_by_xpath("//input[@class='XTCLo x3qfX ']")
        arama_text.send_keys(followlanacak)
        time.sleep(2)
        ben = driver.find_element_by_xpath("//a[@href='/ulasyildiriim/']")
        ben.click()
        time.sleep(2)
        follow_but = driver.find_element_by_xpath("//button[@class='BY3EC  _0mzm- sqdOP  L3NKy       ']")
        follow_but.click()
        time.sleep(20)
        driver.quit()





mal = bot("mal23","123456")
while True:

    mal.instagram_kurma()
    mal.follow()






















