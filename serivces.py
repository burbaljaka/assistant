from selenium import webdriver
from selenium.webdriver.common.by import By

def compliment():
    url = 'http://castlots.org/generator-komplimentov-devushke/'

    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element('id', 'random-button').click()
    val = driver.find_element(By.CLASS_NAME, "compliment")
    return val.text