
import pytest
from selenium import chrome
import seleniumwrapper as seleniumwrapper
from selenium import webdriver
driver = webdriver.chrome
wrapper = seleniumwrapper

from selenium.webdriver.support.wait import WebDriverWait

def open_web_page():
    driver = init_web_driver()
    driver.get("https://docs.openproject.org//")


#open_web_page()

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.python.org")

input('done')



