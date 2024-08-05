from selenium.webdriver.common.by import By

ORDER_BUTTON_TOP = (By.XPATH, ".//button[@class='Button_Button__ra12g' and text()='Заказать']") #Кнопка «Заказать» вверху страницы
ORDER_BUTTON_BOTTOM = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_UltraBig__UU3Lp' and text()='Заказать']") #Кнопка «Заказать» внизу страницы

LOGO_SCOOTER = (By.XPATH, ".//img[@src='/assets/scooter.svg' and @alt='Scooter']") #Логотип Самокат
LOGO_YANDEX = (By.XPATH,".//img[@src='/assets/ya.svg' and @alt='Yandex']") #Логотип Яндекс

PICTURE_SCOOTER = (By.XPATH, ".//div[@class='Home_Scooter__3YdJy']//img[@src='/assets/scooter.png' and @alt='Scooter blueprint']") #Картинка самоката на верху страницы

COOKIE_ACCEPT_BUTTON = (By.XPATH, ".//button[contains(text(), 'да все привыкли')]") #Кнопка "да все привыкли", чтобы принять куки
