from selenium import webdriver
import time
path = "C:\driverler\chromedriver.exe"
url = "http://orteil.dashnet.org/cookieclicker/"

class sinif:

    def __init__(self,ad):
        self.ad = ad
        self.driver = webdriver.Chrome(path)
    def func(self):
        driver = self.driver
        driver.get(url)
        time.sleep(2)
        cookie= driver.find_element_by_xpath("//div[@id='bigCookie']")
        while True:
            cookie.click()


bot = sinif("bot")
bot.func()


























