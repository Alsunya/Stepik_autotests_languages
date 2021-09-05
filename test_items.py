import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#link = "https://selenium1py.pythonanywhere.com"
def test_is_there_a_button(browser):
    try:
        browser.get(link)
        browser.find_element_by_css_selector(".btn-add-to-basket")
        assert True
    finally:
        time.sleep(8)
