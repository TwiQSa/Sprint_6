import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.base_page_locators import *

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    driver.maximize_window()
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(COOKIE_ACCEPT_BUTTON)).click()
    yield driver
    driver.quit()