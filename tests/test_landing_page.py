import pytest
from selenium import webdriver
from pages.landing_page import *
from locators.landing_page_locators import *
from locators.base_page_locators import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

faq_data = [
    (HOME_FAQ_PRICE, HOME_FAQ_PRICE_TEXT),
    (HOME_FAQ_MULTIPLE_SCOOTERS, HOME_FAQ_MULTIPLE_SCOOTERS_TEXT),
    (HOME_FAQ_RENT_TIME, HOME_FAQ_RENT_TIME_TEXT),
    (HOME_FAQ_RENT_TODAY, HOME_FAQ_RENT_TODAY_TEXT),
    (HOME_FAQ_RENT_PROLONGATION, HOME_FAQ_RENT_PROLONGATION_TEXT),
    (HOME_FAQ_CHARGER, HOME_FAQ_CHARGER_TEXT),
    (HOME_FAQ_ORDER_DENIAL, HOME_FAQ_ORDER_DENIAL_TEXT),
    (HOME_FAQ_MKAD, HOME_FAQ_MKAD_TEXT)
]


class TestLandingPage:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://qa-scooter.praktikum-services.ru/")
        cls.page = LandingPage(cls.driver)

        WebDriverWait(cls.driver, 5).until(expected_conditions.element_to_be_clickable(COOKIE_ACCEPT_BUTTON)).click()

        faq_title_visible = WebDriverWait(cls.driver, 10).until(expected_conditions.visibility_of_element_located(FAQ_TITLE))
        cls.driver.execute_script("arguments[0].scrollIntoView();", faq_title_visible)
        WebDriverWait(cls.driver, 10).until(expected_conditions.visibility_of_element_located(HOME_FAQ_PRICE))
        WebDriverWait(cls.driver, 10).until(expected_conditions.visibility_of_element_located(HOME_FAQ_MULTIPLE_SCOOTERS))
        WebDriverWait(cls.driver, 10).until(expected_conditions.visibility_of_element_located(HOME_FAQ_RENT_TIME))
        WebDriverWait(cls.driver, 10).until(expected_conditions.visibility_of_element_located(HOME_FAQ_MKAD))
        WebDriverWait(cls.driver, 10).until(expected_conditions.visibility_of_element_located(HOME_FAQ_CHARGER))

    @pytest.mark.parametrize("locator, expected_text_xpath", faq_data)
    def test_faq(self, locator, expected_text_xpath):
        self.page.driver.find_element(*locator).click()
        assert WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((expected_text_xpath)))

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()