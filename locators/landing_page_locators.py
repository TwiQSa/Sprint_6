from selenium.webdriver.common.by import By

faq_title = (By.XPATH, ".//*[contains(@class, 'Home_SubHeader__zwi_E') and text()='Вопросы о важном']") #Большая надпись "Вопросы о важном" в разделе «Вопросы о важном»

home_faq_price = (By.XPATH, ".//div[contains(text(), 'Сколько это стоит? И как оплатить?')]") #Вопросы о важном, "Сколько это стоит? И как оплатить?"
home_faq_multiple_scooters = (By.XPATH, ".//div[contains(text(), 'Хочу сразу несколько самокатов! Так можно?')]") #Вопросы о важном, "Хочу сразу несколько самокатов! Так можно?"
home_faq_rent_time = (By.XPATH, ".//div[contains(text(), 'Как рассчитывается время аренды?')]") #Вопросы о важном, "Как рассчитывается время аренды?"
home_faq_rent_today = (By.XPATH, ".//div[contains(text(), 'Можно ли заказать самокат прямо на сегодня?')]") #Вопросы о важном, "Можно ли заказать самокат прямо на сегодня?"
home_faq_rent_prolongation = (By.XPATH, ".//div[contains(text(), 'Можно ли продлить заказ или вернуть самокат раньше?')]") #Вопросы о важном, "Можно ли продлить заказ или вернуть самокат раньше?"
home_faq_charger = (By.XPATH, ".//div[contains(text(), 'Вы привозите зарядку вместе с самокатом?')]") #Вопросы о важном, "Вы привозите зарядку вместе с самокатом?"
home_faq_order_denial = (By.XPATH, ".//div[contains(text(), 'Можно ли отменить заказ?')]") #Вопросы о важном, "Можно ли отменить заказ?"
home_faq_mkad = (By.XPATH, ".//div[contains(text(), 'Я жизу за МКАДом, привезёте?')]") #Вопросы о важном, "Я жизу за МКАДом, привезёте?"

home_faq_price_text = (By.XPATH, ".//p[contains(text(), 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.')]") #Ответ на вопрос - "Сколько это стоит? И как оплатить?"
home_faq_multiple_scooters_text = (By.XPATH, ".//p[contains(text(), 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.')]") #Ответ на вопрос - "Хочу сразу несколько самокатов! Так можно?"
home_faq_rent_time_text = (By.XPATH, ".//p[contains(text(), 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')]") #Ответ на вопрос - "Как рассчитывается время аренды?"
home_faq_rent_today_text = (By.XPATH, ".//p[contains(text(), 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.')]") #Ответ на вопрос - "Можно ли заказать самокат прямо на сегодня?"
home_faq_rent_prolongation_text = (By.XPATH, ".//p[contains(text(), 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.')]") #Ответ на вопрос - "Можно ли продлить заказ или вернуть самокат раньше?"
home_faq_charger_text = (By.XPATH, ".//p[contains(text(), 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.')]") #Ответ на вопрос - "Вы привозите зарядку вместе с самокатом?"
home_faq_order_denial_text = (By.XPATH, ".//p[contains(text(), 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.')]") #Ответ на вопрос - "Можно ли отменить заказ?"
home_faq_mkad_text = (By.XPATH, ".//p[contains(text(), 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')]") #Ответ на вопрос - "Я жизу за МКАДом, привезёте?"