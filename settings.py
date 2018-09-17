import os

ROUTER_HOST = 'http://36.70.151.44'

def get_router_username():
    return os.environ['USERNAME']

def get_router_password():
    return os.environ['PASSWORD']
