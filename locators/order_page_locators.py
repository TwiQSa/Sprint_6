from selenium.webdriver.common.by import By

title_for_whom = (By.CLASS_NAME, "Order_Header__BZXOb") #Надпись "Для кого самокат" на странице заказа
name_field = (By.XPATH, ".//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN' and @placeholder='* Имя']") #Поле Имя
surname_field = (By.XPATH, ".//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN' and @placeholder='* Фамилия']") #Поле Фамилия
address_field = (By.XPATH, ".//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN' and @placeholder='* Адрес: куда привезти заказ']") #Поле Адрес
metro_stations = (By.XPATH, ".//input[@class='select-search__input' and @placeholder='* Станция метро']") #Выбор станции метро из списка
phone_field = (By.XPATH, ".//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN' and @placeholder='* Телефон: на него позвонит курьер']") #Поле номер телефона
next_button = (By.XPATH, ".//button[@class= 'Button_Button__ra12g Button_Middle__1CSJM']") #Кнопка далее на странице заказа "Для кого самокат"

title_about_rent = (By.XPATH, ".//div[@class='Order_Header__BZXOb' and text()='Про аренду']") #Надпись "Про аренду" на странице заказа
date_of_delivery = (By.XPATH, ".//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN' and @placeholder='* Когда привезти самокат']") #Поле Когда привезти самокат
length_of_rent = (By.XPATH, ".//div[@class='Dropdown-control']") #Поле Срок Аренды
five_days_rent = (By.XPATH, ".//div[@class='Dropdown-option' and text()='пятеро суток']") #Пятеро суток выбор в Сроке Аренды
two_days_rent = (By.XPATH, ".//div[@class='Dropdown-option' and text()='двое суток']") #Двое суток выбор в Сроке Аренды
check_box_black = (By.XPATH, ".//input[@id='black' and @class='Checkbox_Input__14A2w']") #Чек бокс черный жемчуг
check_box_grey = (By.XPATH, ".//input[@id='grey' and @class='Checkbox_Input__14A2w']") #Чек бокс серая безысходность
comment_field = (By.XPATH, ".//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN' and @placeholder='Комментарий для курьера']") #Поле комментарий
order_button_order_page = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']") #Кнопка "Заказать" на странице заказа

create_order_window = (By.XPATH, ".//div[@class='Order_ModalHeader__3FDaJ' and text()='Хотите оформить заказ?']") #Текст "Хотите оформить заказ?", помогает проверить, что окно появилось
yes_button = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']") #Кнопка "Да" в окне "Хотите оформить заказ?"
status_button = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Посмотреть статус']") #Кнопка "Посмотреть статус"
cancel_order_button = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i' and text()='Отменить заказ']") #Кнопка "Отменить заказ" на странице с трекингом