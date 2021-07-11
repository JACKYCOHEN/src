import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    _driver = webdriver.Chrome()
    yield _driver
    _driver.quit()