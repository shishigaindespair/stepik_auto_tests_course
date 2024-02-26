from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    summa = str(int(browser.find_element(By.ID, 'num1').text) + int(browser.find_element(By.ID, 'num2').text))
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(summa)
    browser.find_element(By.TAG_NAME, 'button').click()
    print(browser.switch_to.alert.text)

finally:
    time.sleep(5)
    browser.quit()