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
    (home_faq_price, home_faq_price_text),
    (home_faq_multiple_scooters, home_faq_multiple_scooters_text),
    (home_faq_rent_time, home_faq_rent_time_text),
    (home_faq_rent_today, home_faq_rent_today_text),
    (home_faq_rent_prolongation, home_faq_rent_prolongation_text),
    (home_faq_charger, home_faq_charger_text),
    (home_faq_order_denial, home_faq_order_denial_text),
    (home_faq_mkad, home_faq_mkad_text)
]


class TestLandingPage:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://qa-scooter.praktikum-services.ru/")
        cls.page = LandingPage(cls.driver)

        WebDriverWait(cls.driver, 5).until(expected_conditions.element_to_be_clickable(cookie_accept_button)).click()

        faq_title_visible = WebDriverWait(cls.driver, 10).until(expected_conditions.visibility_of_element_located(faq_title))
        cls.driver.execute_script("arguments[0].scrollIntoView();", faq_title_visible)
        time.sleep(5)

    @pytest.mark.parametrize("locator, expected_text_xpath", faq_data)
    def test_faq(self, locator, expected_text_xpath):
        self.page.driver.find_element(*locator).click()
        assert WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((expected_text_xpath)))

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()