from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_different_languages(browser):
    browser.get(link)
    assert browser.find_elements(By.CLASS_NAME, 'btn-add-to-basket'), 'Button not found'
    
   
    