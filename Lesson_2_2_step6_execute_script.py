from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/execute_script.html")
    browser.find_element(By.ID, "answer").send_keys(calc(browser.find_element(By.ID, "input_value").text))
    browser.find_element(By.ID, "robotCheckbox").click()

    robots = browser.find_element(By.ID,"robotsRule")
    browser.execute_script("return arguments [0].scrollIntoView(true);", robots)
    robots.click()

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments [0].scrollIntoView(true);", button)
    button.click()

    print(browser.switch_to.alert.text)

finally:
    time.sleep(5)
    browser.quit()
    