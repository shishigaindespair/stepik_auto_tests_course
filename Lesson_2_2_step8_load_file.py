from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

browser = webdriver.Chrome()

# Задание:
# 1. Открыть страницу

browser.get("http://suninjuly.github.io/file_input.html")

# 2. Заполнить текстовые поля

browser.find_element(By.NAME, "firstname").send_keys("Firstname")
browser.find_element(By.NAME, "lastname").send_keys("Lastname")
browser.find_element(By.NAME, "email").send_keys("E-mail")

# 3. Загрузить txt файл

current_dir = os.path.abspath(os.path.dirname(__file__))
browser.find_element(By.NAME, "file").send_keys(os.path.join(current_dir, 'file.txt'))

# 4. Нажать кнопку "Submit"

browser.find_element(By.TAG_NAME, "button").click()

print(browser.switch_to.alert.text)

time.sleep(5)
browser.quit()
