from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()

# Задание:
# 1. Открыть страницу

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# 2. Дождаться, когда цена дома уменьшится до $100

button = WebDriverWait(browser, 20).until(
    EC.text_to_be_present_in_element((By.ID, "price"), text_= "$100")
)

# 3. Нажать кнопку "Book"

browser.find_element(By.ID, "book").click()

# 4. Решить задачу и отправить решение

browser.find_element(By.ID, 'answer').send_keys(calc(browser.find_element(By.ID, "input_value").text))
browser.find_element(By.ID, "solve").click()

print(browser.switch_to.alert.text)

time.sleep(5)
browser.quit()
