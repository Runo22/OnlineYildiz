#ONLINE YILDIZ ders sistemine girip aktif dersi açan otomasyon programı
#TUNA ONUR ALAN - 18.11.2020
#V2

from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import msvcrt #q ile direk çıkamk için
import sys
import os


if(len(sys.argv)==3):
	USERNAME = sys.argv[1]
	PASSWORD = sys.argv[2]
	PATH = sys.argv[0][:-16].replace("\\","/")
else:
	USERNAME = input("Kullanıcı Adı:")
	PASSWORD = input("Sifre:")
	PATH = os.path.dirname(os.path.realpath(__file__)).replace("\\","/")


driver = webdriver.Chrome(PATH + "/chromedriver.exe", service_log_path='NUL')

driver.get("https://online.yildiz.edu.tr/Account/Login?ReturnUrl=%2\f")
time.sleep(.8)
driver.find_element_by_xpath('//*[@id="Data_AccountType"]/option[3]').click()

username = driver.find_element_by_name("Data.Mail")
password = driver.find_element_by_name("Data.Password")
button = driver.find_element_by_xpath('//*[@id="Information"]/div[4]/div[2]/button')

username.send_keys(USERNAME)
password.send_keys(PASSWORD)

button.click()

wait = WebDriverWait(driver,15)
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="flow-tab"]/div/div[1]/div[3]'))).click()
waitshort = WebDriverWait(driver,3)
try:
    waitshort.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Derse Katıl"))).click()
    print('OK')
except:
	print("Aktif Ders Bulunamadı")


while True:
	print ("Çıkmak için q ya bas:")
	char = msvcrt.getch()
	if (char == b"q"):
		driver.quit()
		break

