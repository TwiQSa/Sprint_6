from selenium.webdriver.common.by import By

TITLE_FOR_WHOM = (By.CLASS_NAME, "Order_Header__BZXOb") #Надпись "Для кого самокат" на странице заказа
NAME_FIELD = (By.XPATH, ".//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN' and @placeholder='* Имя']") #Поле Имя
SURNAME_FIELD = (By.XPATH, ".//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN' and @placeholder='* Фамилия']") #Поле Фамилия
ADDRESS_FIELD = (By.XPATH, ".//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN' and @placeholder='* Адрес: куда привезти заказ']") #Поле Адрес
METRO_STATIONS = (By.XPATH, ".//input[@class='select-search__input' and @placeholder='* Станция метро']") #Выбор станции метро из списка
PHONE_FIELD = (By.XPATH, ".//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN' and @placeholder='* Телефон: на него позвонит курьер']") #Поле номер телефона
NEXT_BUTTON = (By.XPATH, ".//button[@class= 'Button_Button__ra12g Button_Middle__1CSJM']") #Кнопка далее на странице заказа "Для кого самокат"

TITLE_ABOUT_RENT = (By.XPATH, ".//div[@class='Order_Header__BZXOb' and text()='Про аренду']") #Надпись "Про аренду" на странице заказа
DATE_OF_DELIVERY = (By.XPATH, ".//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN' and @placeholder='* Когда привезти самокат']") #Поле Когда привезти самокат
LENGTH_OF_RENT = (By.XPATH, ".//div[@class='Dropdown-control']") #Поле Срок Аренды
FIVE_DAYS_RENT = (By.XPATH, ".//div[@class='Dropdown-option' and text()='пятеро суток']") #Пятеро суток выбор в Сроке Аренды
TWO_DAYS_RENT = (By.XPATH, ".//div[@class='Dropdown-option' and text()='двое суток']") #Двое суток выбор в Сроке Аренды
CHECK_BOX_BLACK = (By.XPATH, ".//input[@id='black' and @class='Checkbox_Input__14A2w']") #Чек бокс черный жемчуг
CHECK_BOX_GREY = (By.XPATH, ".//input[@id='grey' and @class='Checkbox_Input__14A2w']") #Чек бокс серая безысходность
COMMENT_FIELD = (By.XPATH, ".//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN' and @placeholder='Комментарий для курьера']") #Поле комментарий
ORDER_BUTTON_ORDER_PAGE = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']") #Кнопка "Заказать" на странице заказа

CREATE_ORDER_WINDOW = (By.XPATH, ".//div[@class='Order_ModalHeader__3FDaJ' and text()='Хотите оформить заказ?']") #Текст "Хотите оформить заказ?", помогает проверить, что окно появилось
YES_BUTTON = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']") #Кнопка "Да" в окне "Хотите оформить заказ?"
STATUS_BUTTON = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Посмотреть статус']") #Кнопка "Посмотреть статус"
CANCEL_ORDER_BUTTON = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i' and text()='Отменить заказ']") #Кнопка "Отменить заказ" на странице с трекингом