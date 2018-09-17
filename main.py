from time import sleep
from driver import get_driver
from client_list import get_client_list
from block_client import block_client_by_mac, unblock_all

def main():
    driver = get_driver(headless=False)
    # block_client_by_mac(driver, 'ac:5f:3e:81:94:78')
    unblock_all(driver)
    sleep(10)

if __name__ == '__main__':
    main()
