from locators.landing_page_locators import *
from selenium.webdriver.remote.webdriver import WebDriver

class LandingPage:
    def __init__(self, driver):
        self.driver = driver

    def click_home_faq_price(self):
        self.driver.find_element(home_faq_price).click()

    def click_home_faq_multiple_scooters(self):
        self.driver.find_element(home_faq_multiple_scooters).click()

    def click_home_faq_rent_time(self):
        self.driver.find_element(home_faq_rent_time).click()

    def click_home_faq_rent_today(self):
        self.driver.find_element(home_faq_rent_today).click()

    def click_home_faq_rent_prolongation(self):
        self.driver.find_element(home_faq_rent_prolongation).click()

    def click_home_faq_charger(self):
        self.driver.find_element(home_faq_charger).click()

    def click_home_faq_order_denial(self):
        self.driver.find_element(home_faq_order_denial).click()

    def click_home_faq_mkad(self):
        self.driver.find_element(home_faq_mkad).click()