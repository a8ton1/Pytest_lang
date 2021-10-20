import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket(browser):
    browser.get(link)
    browser.implicitly_wait(10)
    try:
        basket_button = browser.find_element_by_css_selector('.btn-add-to-basket')
        assert basket_button is not None
        basket_button.click()
    except AssertionError:
        print("Кнопка не найдена")
