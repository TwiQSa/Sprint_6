import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.order_page import *
from locators.order_page_locators import *
from locators.base_page_locators import *
import time

class TestScooterOrder:

    def test_order_scooter_top_button(self, driver):

        driver.find_element(*ORDER_BUTTON_TOP).click()

        driver.find_element(*NAME_FIELD).send_keys("Семён")
        driver.find_element(*SURNAME_FIELD).send_keys("Семёнов")
        driver.find_element(*ADDRESS_FIELD).send_keys("Пушкина 22")

        driver.find_element(*METRO_STATIONS).click()
        metro_station = (By.XPATH, ".//*[contains(text(), 'Сокольники')]")
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(metro_station)).click()

        driver.find_element(*PHONE_FIELD).send_keys("+79521234567")
        driver.find_element(*NEXT_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TITLE_ABOUT_RENT))
        driver.find_element(*DATE_OF_DELIVERY).send_keys("12.08.2024")
        driver.find_element(*TITLE_ABOUT_RENT).click()
        driver.find_element(*LENGTH_OF_RENT).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(FIVE_DAYS_RENT)).click()
        driver.find_element(*CHECK_BOX_BLACK).click()
        driver.find_element(*COMMENT_FIELD).send_keys("Позвоните заранее")
        driver.find_element(*ORDER_BUTTON_ORDER_PAGE).click()

        create_order_window_element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(CREATE_ORDER_WINDOW))
        assert create_order_window_element.is_displayed()
        driver.find_element(*YES_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(STATUS_BUTTON)).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LOGO_SCOOTER))
        driver.find_element(*LOGO_SCOOTER).click()
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be("https://qa-scooter.praktikum-services.ru/"))
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LOGO_YANDEX))
        driver.find_element(*LOGO_YANDEX).click()
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 10).until(expected_conditions.url_contains("https://dzen.ru/?yredirect=true"))

        assert driver.current_url == "https://dzen.ru/?yredirect=true"

    def test_order_scooter_bottom_button(self, driver):

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")

        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(ORDER_BUTTON_BOTTOM))
        driver.find_element(*ORDER_BUTTON_BOTTOM).click()

        driver.find_element(*NAME_FIELD).send_keys("Вадим")
        driver.find_element(*SURNAME_FIELD).send_keys("Ярославов")
        driver.find_element(*ADDRESS_FIELD).send_keys("Карбышева 29")

        driver.find_element(*METRO_STATIONS).click()
        metro_station = (By.XPATH, ".//*[contains(text(), 'Лубянка')]")
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(metro_station)).click()

        driver.find_element(*PHONE_FIELD).send_keys("+79841256589")
        driver.find_element(*NEXT_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TITLE_ABOUT_RENT))
        driver.find_element(*DATE_OF_DELIVERY).send_keys("07.08.2024")
        driver.find_element(*TITLE_ABOUT_RENT).click()
        driver.find_element(*LENGTH_OF_RENT).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TWO_DAYS_RENT)).click()
        driver.find_element(*CHECK_BOX_GREY).click()
        driver.find_element(*COMMENT_FIELD).send_keys("Напишите вместо звонка")
        driver.find_element(*ORDER_BUTTON_ORDER_PAGE).click()

        create_order_window_element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(CREATE_ORDER_WINDOW))
        assert create_order_window_element.is_displayed()
        driver.find_element(*YES_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(STATUS_BUTTON)).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LOGO_SCOOTER))
        driver.find_element(*LOGO_SCOOTER).click()
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be("https://qa-scooter.praktikum-services.ru/"))
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LOGO_YANDEX))
        driver.find_element(*LOGO_YANDEX).click()
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 10).until(expected_conditions.url_contains("https://dzen.ru/?yredirect=true"))

        assert driver.current_url == "https://dzen.ru/?yredirect=true"

