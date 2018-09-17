from time import sleep
from exception import RouterOperationException
from settings import ROUTER_HOST, get_router_password, get_router_username
from utils import form_input

def authorize_driver(driver):
    driver.get(ROUTER_HOST)
    sleep(1)
    driver.switch_to_frame(driver.find_element_by_id('loginPage'))
    if is_driver_authorized(driver):
        return
    form_input(driver, {
        'User': get_router_username(),
        'Passwd': get_router_password()
    }, submit='submit')
    driver.switch_to_default_content()
    driver.switch_to_frame(driver.find_element_by_name('loginPage'))
    if is_driver_authorized(driver):
        print('Driver authorized!')
    else:
        raise RouterOperationException('Driver authorization failed')

def is_driver_authorized(driver):
    try:
        driver.find_element_by_id('Wireless Status')
        return True
    except:
        return False

def with_authorized_driver(function):
    def wrapper(driver, *args, **kwargs):
        authorize_driver(driver)
        return_value = function(driver, *args, **kwargs)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_name('loginPage'))
        return return_value
    return wrapper
