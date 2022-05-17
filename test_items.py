import time
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_backet_displey(browser):
    browser.get(link)
    time.sleep(3)
    button = browser.find_element(By.CSS_SELECTOR, "form > button.btn-lg.btn-add-to-basket")
    assert button.is_displayed(), "Кнопка добавления товара в корзину отсутсвует"
