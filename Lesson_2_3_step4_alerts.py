from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()

# Задание:
# 1. Открыть страницу

browser.get("http://suninjuly.github.io/alert_accept.html")

# 2. Нажать кнопку

browser.find_element(By.TAG_NAME, "button").click()

# 3. Принять Confirm

browser.switch_to.alert.accept()

# 4. На новой странице решить капчу

browser.find_element(By.ID, 'answer').send_keys(calc(browser.find_element(By.ID, "input_value").text))
browser.find_element(By.TAG_NAME, "button").click()

print(browser.switch_to.alert.text)
