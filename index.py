import selenium
from selenium import webdriver
import time
import os
import random
import multiprocessing
from selenium.webdriver.chrome import options
path = "./chromedriver.exe"
proxylist = [
"ult4.falix.gg:36422",
"ult5.falix.gg:36856"
]
def visitwebsite():
    f = open("useragent.txt")
    useragent = f.readline(random.randint(0,1000))
    proxy = proxylist[random.randint(0,len(proxylist)-1)]
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('user-agent=%s' % useragent)
    chrome_options.add_argument('--proxy-server=socks5://%s' % proxy)
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--disable-geolocation")
    chrome_options.add_argument("--disable-search-geolocation-disclosure")
    chrome_options.add_argument("--scan-locations")
    chrome = webdriver.Chrome(path,chrome_options=chrome_options)
    try:
        wait_timex = 0
        hata = 0
        wait_time = random.randrange(160,240)#Random 60-75 Second Waiting Time
        browse = chrome.get("https://cvary.xyz/afk-users-page/")

        while wait_time>wait_timex:
            wait_timex = wait_timex + 1
            time.sleep(1)
            
    except selenium.common.exceptions.WebDriverException:
        hata = 1
        chrome.delete_all_cookies()
        chrome.quit
    finally:
        if hata == 1:
            print("Ziyaret Hatalı Gerçekleşti yada Sayfa Kapatıldı")
        else:
            print("Ziyaret Başarılı Bir Şekilde Gerçekleşti")
            chrome.delete_all_cookies()
            chrome.quit

        
        
            




if __name__ == '__main__':
    for i in range(500):#Total Repeat
            p1 = multiprocessing.Process(target=visitwebsite)
            p2 = multiprocessing.Process(target=visitwebsite)
            p3 = multiprocessing.Process(target=visitwebsite)
            p4 = multiprocessing.Process(target=visitwebsite)
            p5 = multiprocessing.Process(target=visitwebsite)
            p6 = multiprocessing.Process(target=visitwebsite)
            p1.start()
            #p2.start()
            #p3.start()
            #p4.start()


            p1.join()
            #p2.join()
            #p3.join()
            #p4.join()