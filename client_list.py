from auth import with_authorized_driver

@with_authorized_driver
def get_client_list(authorized_driver):
    authorized_driver.find_element_by_xpath('//*[@id="Status"]').click()
    authorized_driver.find_element_by_id('Wireless Status').click()
    authorized_driver.find_element_by_xpath("//*[contains(text(), 'WIFI Clients List')]").click()
    authorized_driver.switch_to_frame(authorized_driver.find_element_by_id('frameContent'))
    mac_list = authorized_driver.find_elements_by_xpath('//*[@id="wifi_mac"]')
    ip_list = authorized_driver.find_elements_by_xpath('//*[@id="wifi_ip"]')
    return [(mac.get_attribute('innerHTML'), ip.get_attribute('innerHTML')) for mac, ip in zip(mac_list, ip_list)]
