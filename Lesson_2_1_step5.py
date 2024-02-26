from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    browser.find_element(By.ID, 'answer').send_keys(calc(browser.find_element(By.ID,'input_value').text))
    browser.find_element(By.ID,'robotCheckbox').click()
    browser.find_element(By.ID,'robotsRule').click()
    browser.find_element(By.TAG_NAME,'button').click()
    print(browser.switch_to.alert.text)

finally:
    time.sleep(5)
    browser.quit()

