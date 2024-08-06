from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from locators.base_page_locators import *
class BasePageButtons:

    def __init__(self, driver):
        self.driver = driver
    def click_order_button_top(self):
        self.driver.find_element(ORDER_BUTTON_TOP).click()

    def click_order_button_bottom(self):
        self.driver.find_element(ORDER_BUTTON_BOTTOM).click()

    def click_logo_scooter(self):
        self.driver.find_element(LOGO_SCOOTER).click()

    def click_logo_yandex(self):
        self.driver.find_element(LOGO_YANDEX).click()