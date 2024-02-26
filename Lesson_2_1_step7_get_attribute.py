from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    treasure = browser.find_element(By.ID, 'treasure').get_attribute("valuex")
    browser.find_element(By.ID, 'answer').send_keys(calc(treasure))
    browser.find_element(By.ID,'robotCheckbox').click()
    browser.find_element(By.ID,'robotsRule').click()
    browser.find_element(By.TAG_NAME,'button').click()
    print(browser.switch_to.alert.text)

finally:
    time.sleep(5)
    browser.quit()