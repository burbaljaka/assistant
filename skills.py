import copy
import json
import os, webbrowser, sys, requests, subprocess
import time

import loguru
import pyttsx3
from selenium import webdriver
from selenium.webdriver.common.by import By

engine = pyttsx3.init()
voices = engine.getProperty('voices')


engine.setProperty('rate', 220)
engine.setProperty('voice', voices[45].id)

def speaker(text_to_say):
    loguru.logger.debug(text_to_say)
    # engine.say(text_to_say)
    # engine.runAndWait()
    os.system(f'say {text_to_say}')

def browser():
    webbrowser.open('https://github.com', new=2)

def weather():
    api_key = 'b3baf369bd9d439de549daf27034b545'
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = 'Ryazan'
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    if response.status_code != 404:
        speaker(f"на улице {round(response.json()['main']['temp'] - 273)} градусов")

def off_bot():
    sys.exit()

def joke():
    anek = requests.get("http://rzhunemogu.ru/RandJSON.aspx?CType=1")
    res = anek.text.replace('\r', '.').replace('\n', ".").replace('- ', '') if anek.ok else None
    if res:
        try:
            speaker(json.loads(res).get("content"))
        except json.decoder.JSONDecodeError:
            print(res)
    else:
        speaker("Что-то не получается")

def passive():
    pass

def friendly():
    pass


def compliment():
    url = 'http://castlots.org/generator-komplimentov-devushke/'

    driver = webdriver.Chrome()
    driver.set_page_load_timeout(15)
    driver.get(url)
    time.sleep(5)
    driver.find_element('id', 'random-button').click()
    # driver.find_element('id', 'random-button').click()
    val = driver.find_element(By.CLASS_NAME, "compliment")
    while not val:
        print("will try again")
    res = copy.deepcopy(val.text)
    driver.quit()
    speaker(res)


