from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()

# Задание:
# 1. Открыть страницу

browser.get("http://suninjuly.github.io/redirect_accept.html")

# 2. Нажать на кнопку

browser.find_element(By.TAG_NAME, "button").click()

# 3. Переключиться на новую вкладку

browser.switch_to.window(browser.window_handles[1])

# 4. Пройти капчу для робота

browser.find_element(By.ID, 'answer').send_keys(calc(browser.find_element(By.ID, "input_value").text))
browser.find_element(By.TAG_NAME, "button").click()

print(browser.switch_to.alert.text)

time.sleep(5)
browser.quit()

