from locators.landing_page_locators import *
from selenium.webdriver.remote.webdriver import WebDriver

class LandingPage:
    def __init__(self, driver):
        self.driver = driver

    def click_home_faq_price(self):
        self.driver.find_element(HOME_FAQ_PRICE).click()

    def click_home_faq_multiple_scooters(self):
        self.driver.find_element(HOME_FAQ_MULTIPLE_SCOOTERS).click()

    def click_home_faq_rent_time(self):
        self.driver.find_element(HOME_FAQ_RENT_TIME).click()

    def click_home_faq_rent_today(self):
        self.driver.find_element(HOME_FAQ_RENT_TODAY).click()

    def click_home_faq_rent_prolongation(self):
        self.driver.find_element(HOME_FAQ_RENT_PROLONGATION).click()

    def click_home_faq_charger(self):
        self.driver.find_element(HOME_FAQ_CHARGER).click()

    def click_home_faq_order_denial(self):
        self.driver.find_element(HOME_FAQ_ORDER_DENIAL).click()

    def click_home_faq_mkad(self):
        self.driver.find_element(HOME_FAQ_MKAD).click()