from selenium.webdriver.common.by import By

order_button_top = (By.XPATH, ".//button[@class='Button_Button__ra12g' and text()='Заказать']") #Кнопка «Заказать» вверху страницы
order_button_bottom = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_UltraBig__UU3Lp' and text()='Заказать']") #Кнопка «Заказать» внизу страницы

logo_scooter = (By.XPATH, ".//img[@src='/assets/scooter.svg' and @alt='Scooter']") #Логотип Самокат
logo_yandex = (By.XPATH,".//img[@src='/assets/ya.svg' and @alt='Yandex']") #Логотип Яндекс

picture_scooter = (By.XPATH, ".//div[@class='Home_Scooter__3YdJy']//img[@src='/assets/scooter.png' and @alt='Scooter blueprint']") #Картинка самоката на верху страницы

cookie_accept_button = (By.XPATH, ".//button[contains(text(), 'да все привыкли')]") #Кнопка "да все привыкли", чтобы принять куки