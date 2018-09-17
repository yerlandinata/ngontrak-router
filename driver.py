from selenium.webdriver import Chrome, ChromeOptions

def get_driver(headless=False):
    chrome_options = ChromeOptions()  
    if headless:
        chrome_options.add_argument("--headless")
    return Chrome(chrome_options=chrome_options)
    