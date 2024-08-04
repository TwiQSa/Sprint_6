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

    @pytest.mark.parametrize("name, surname, address, metro, phone, comment, date_to_deliver", [
        ("Семён", "Семёнов", "Пушкина 22", "Сокольники", "+79521234567", "Позвоните заранее", "12.08.2024")
    ])
    def test_order_scooter_top_button(self, driver, name, surname, address, metro, phone, comment, date_to_deliver):

        driver.find_element(*order_button_top).click()

        driver.find_element(*name_field).send_keys(name)
        driver.find_element(*surname_field).send_keys(surname)
        driver.find_element(*address_field).send_keys(address)

        driver.find_element(*metro_stations).click()
        metro_station = (By.XPATH, f".//*[contains(text(), '{metro}')]")
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(metro_station)).click()

        driver.find_element(*phone_field).send_keys(phone)
        driver.find_element(*next_button).click()

        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(title_about_rent))
        driver.find_element(*date_of_delivery).send_keys(f"{date_to_deliver}")
        driver.find_element(*title_about_rent).click()
        driver.find_element(*length_of_rent).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(five_days_rent)).click()
        driver.find_element(*check_box_black).click()
        driver.find_element(*comment_field).send_keys(comment)
        driver.find_element(*order_button_order_page).click()

        create_order_window_element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(create_order_window))
        assert create_order_window_element.is_displayed()
        driver.find_element(*yes_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(status_button)).click()

        time.sleep(2)
        driver.find_element(*logo_scooter).click()
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be("https://qa-scooter.praktikum-services.ru/"))
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"

        time.sleep(2)
        driver.find_element(*logo_yandex).click()
        time.sleep(6)
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 10).until(expected_conditions.url_contains("https://dzen.ru/?yredirect=true"))

        assert driver.current_url == "https://dzen.ru/?yredirect=true"

    @pytest.mark.parametrize("name, surname, address, metro, phone, comment, date_to_deliver", [
        ("Вадим", "Ярославов", "Карбышева 29", "Лубянка", "+79841256589", "Напишите вместо звонка", "07.08.2024")
    ])
    def test_order_scooter_bottom_button(self, driver, name, surname, address, metro, phone, comment, date_to_deliver):

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")
        time.sleep(5)

        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(order_button_bottom))
        driver.find_element(*order_button_bottom).click()

        driver.find_element(*name_field).send_keys(name)
        driver.find_element(*surname_field).send_keys(surname)
        driver.find_element(*address_field).send_keys(address)

        driver.find_element(*metro_stations).click()
        metro_station = (By.XPATH, f".//*[contains(text(), '{metro}')]")
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(metro_station)).click()

        driver.find_element(*phone_field).send_keys(phone)
        driver.find_element(*next_button).click()

        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(title_about_rent))
        driver.find_element(*date_of_delivery).send_keys(f"{date_to_deliver}")
        driver.find_element(*title_about_rent).click()
        driver.find_element(*length_of_rent).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(two_days_rent)).click()
        driver.find_element(*check_box_grey).click()
        driver.find_element(*comment_field).send_keys(comment)
        driver.find_element(*order_button_order_page).click()

        create_order_window_element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(create_order_window))
        assert create_order_window_element.is_displayed()
        driver.find_element(*yes_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(status_button)).click()

        time.sleep(2)
        driver.find_element(*logo_scooter).click()
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be("https://qa-scooter.praktikum-services.ru/"))
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"

        time.sleep(2)
        driver.find_element(*logo_yandex).click()
        time.sleep(6)
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 10).until(expected_conditions.url_contains("https://dzen.ru/?yredirect=true"))

        assert driver.current_url == "https://dzen.ru/?yredirect=true"

