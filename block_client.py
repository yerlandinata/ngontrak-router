from auth import with_authorized_driver

@with_authorized_driver
def block_client_by_mac(authorized_driver, target_mac):
    authorized_driver.find_element_by_xpath('//*[@id="Security"]').click()
    authorized_driver.find_element_by_xpath('//*[@id="navsub"]/ul/li[1]/ul/li[7]').click()
    authorized_driver.switch_to_frame(authorized_driver.find_element_by_id('frameContent'))
    authorized_driver.find_element_by_xpath('//*[@id="mf_add"]').click()
    authorized_driver.find_element_by_xpath('//*[@id="macaddr_mac"]').send_keys(target_mac)
    authorized_driver.find_element_by_xpath('//*[@id="mac_rule_enable"]').click()
    authorized_driver.find_element_by_xpath('//*[@id="mac_rule_enable"]/option[1]').click()
    authorized_driver.find_element_by_xpath('//*[@id="macaddr_apply"]').click()

@with_authorized_driver
def get_blocked_clients(authorized_driver):
    authorized_driver.find_element_by_xpath('//*[@id="Security"]').click()
    authorized_driver.find_element_by_xpath('//*[@id="navsub"]/ul/li[1]/ul/li[7]').click()
    authorized_driver.switch_to_frame(authorized_driver.find_element_by_id('frameContent'))
    macs = []
    i = 0
    while True:
        try:
            macs.append(authorized_driver.find_element_by_id('mac_adress_{}'.format(i)).get_attribute('innerHTML'))
        except:
            break
        i += 1
    return tuple(macs)

@with_authorized_driver
def unblock_all(authorized_driver):
    authorized_driver.find_element_by_xpath('//*[@id="Security"]').click()
    authorized_driver.find_element_by_xpath('//*[@id="navsub"]/ul/li[1]/ul/li[7]').click()
    authorized_driver.switch_to_frame(authorized_driver.find_element_by_id('frameContent'))
    authorized_driver.find_element_by_xpath('//*[@id="mf_deleteAll"]').click()
    alert = authorized_driver.switch_to_alert()
    alert.accept()
