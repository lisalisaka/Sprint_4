from selenium.webdriver.common.by import By

class OrderPageLocators():
    NAME_INPUT = (By.XPATH, ".//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    UNDEGROUND_INPUT = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    UNDEGROUND_STATION_1 = (By.XPATH, ".//div[text()='Бульвар Рокоссовского']/parent::button")
    UNDEGROUND_STATION_2 = (By.XPATH, ".//div[text()='Лубянка']/parent::button")
    PHONE_INPUT = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")
    DATE_FIELD = (By.CLASS_NAME, 'Order_MixedDatePicker__3qiay')
    DATE_INPUT = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    DATE_IN_CALENDAR = (By.CLASS_NAME, "react-datepicker__day react-datepicker__day--010")
    RENT_PERIOD_INPUT = (By.CLASS_NAME, "Dropdown-control")
    RENT_PERION_DROPDOWN_2_DAYS = (By.XPATH, ".//div[@class='Dropdown-option'][2]")
    RENT_PERION_DROPDOWN_5_DAYS = (By.XPATH, ".//div[@class='Dropdown-option'][5]")
    COLOR_CHOICE_BLACK = (By.XPATH, ".//label[@for='black']")
    COLOR_CHOICE_GREY = (By.XPATH, ".//label[@for='grey']")
    COMMENT_FOR_COURIER = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    MAKE_ORDER_BUTTON = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    EMPTY_PLACE = (By.CLASS_NAME, "App_App__15LM-")
    CONFIRMATION_ORDER_MODAL_WINDOW = (By.CLASS_NAME, "Order_Modal__YZ-d3")
    SAY_YES_ORDER_BUTTON = (By.XPATH, ".//button[text()='Да']")
    ORDER_IS_MAID_MODAL_WINDOW = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
    VIEW_STATUS_BUTTON_IN_MODAL_WINDOW = (By.XPATH, ".//button[text()='Посмотреть статус']")