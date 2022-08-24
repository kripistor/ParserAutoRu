from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary
from selenium.common.exceptions import StaleElementReferenceException
import time
import re

browser = webdriver.Chrome()
browser.get("https://auto.ru/")
Lada_button = browser.find_element(By.CSS_SELECTOR,'[href="https://auto.ru/moskva/cars/vaz/all/"]').click()
time.sleep(5)# Небольшой тайминг загрузки страници
Check_box = browser.find_element(By.CSS_SELECTOR,'[name="on_credit"]').click()
ShowContent_Button = browser.find_element(By.CLASS_NAME,"ButtonWithLoader__content").click()

Cars_name = browser.find_elements(By.XPATH,"//a[@class='Link ListingItemTitle__link']")

Cars_price = browser.find_elements(By.XPATH,"//div[@class='ListingItemPrice__content']")
PriceOfAllCars = []
for price,name  in zip(Cars_price,Cars_name):
    try:
        count = re.sub(r"\D", "", price.text)
        print(f"\n Name:{name.text}\n Price:{price.text}")
        PriceOfAllCars.append(int(count))
    except StaleElementReferenceException: #Не мог пофиксить ошибку, понимаю как она появляется, но способов решения не нашел
        continue
print(f"\n Min price of car:{min(PriceOfAllCars)}₽")
