from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import *

class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_name(self, name):
        self.driver.find_element(*name_field).send_keys(name)

    def enter_surname(self, surname):
        self.driver.find_element(*surname_field).send_keys(surname)

    def enter_address(self, address):
        self.driver.find_element(*address_field).send_keys(address)

    def select_metro_station(self, station_name):
        metro_station_input = self.driver.find_element(*metro_stations)
        self.driver.execute_script("arguments[0].value = arguments[1];", metro_station_input, station_name)

    def enter_phone(self, phone):
        self.driver.find_element(*phone_field).send_keys(phone)

    def click_next_button(self):
        self.driver.find_element(*next_button).click()

    def set_date_of_delivery(self, date):
        self.driver.find_element(*date_of_delivery).date_field.send_keys(date)

    def set_length_of_rent_two_days(self):
        rent_field = self.driver.find_element(*length_of_rent)
        rent_field.click()

        two_days_option = WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(two_days_rent))
        two_days_option.click()

    def set_length_of_rent_five_days(self):
        rent_field = self.driver.find_element(*length_of_rent)
        rent_field.click()

        five_days_option = WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(five_days_rent))
        five_days_option.click()

    def click_check_box_black(self):
        self.driver.find_element(*check_box_black).click()

    def click_check_box_grey(self):
        self.driver.find_element(*check_box_grey).click()

    def set_comment(self, comment):
        self.driver.find_element(*comment_field).send_keys(*comment)

    def click_order_button_order_page(self):
        self.driver.find_element(*order_button_order_page).click()

    def click_yes_button(self):
        self.driver.find_element(*yes_button).click()

    def click_status_button(self):
        self.driver.find_element(*status_button).click()