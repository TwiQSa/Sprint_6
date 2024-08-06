from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import *

class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_name(self, name):
        self.driver.find_element(*NAME_FIELD).send_keys(name)

    def enter_surname(self, surname):
        self.driver.find_element(*SURNAME_FIELD).send_keys(surname)

    def enter_address(self, address):
        self.driver.find_element(*ADDRESS_FIELD).send_keys(address)

    def select_metro_station(self, station_name):
        metro_station_input = self.driver.find_element(*METRO_STATIONS)
        self.driver.execute_script("arguments[0].value = arguments[1];", metro_station_input, station_name)

    def enter_phone(self, phone):
        self.driver.find_element(*PHONE_FIELD).send_keys(phone)

    def click_next_button(self):
        self.driver.find_element(*NEXT_BUTTON).click()

    def set_date_of_delivery(self, date):
        self.driver.find_element(*DATE_OF_DELIVERY).date_field.send_keys(date)

    def set_length_of_rent_two_days(self):
        rent_field = self.driver.find_element(*LENGTH_OF_RENT)
        rent_field.click()

        two_days_option = WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(TWO_DAYS_RENT))
        two_days_option.click()

    def set_length_of_rent_five_days(self):
        rent_field = self.driver.find_element(*LENGTH_OF_RENT)
        rent_field.click()

        five_days_option = WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(FIVE_DAYS_RENT))
        five_days_option.click()

    def click_check_box_black(self):
        self.driver.find_element(*CHECK_BOX_BLACK).click()

    def click_check_box_grey(self):
        self.driver.find_element(*CHECK_BOX_GREY).click()

    def set_comment(self, comment):
        self.driver.find_element(*COMMENT_FIELD).send_keys(*comment)

    def click_order_button_order_page(self):
        self.driver.find_element(*ORDER_BUTTON_ORDER_PAGE).click()

    def click_yes_button(self):
        self.driver.find_element(*YES_BUTTON).click()

    def click_status_button(self):
        self.driver.find_element(*STATUS_BUTTON).click()