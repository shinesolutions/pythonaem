import os
from pythonaem import PythonAem

def init_client():
    conf = {
        'username': os.getenv('aem_username', 'admin'),
        'password': os.getenv('aem_password', 'admin'),
        'protocol': os.getenv('aem_protocol', 'http'),
        'host': os.getenv('aem_host', 'localhost'),
        'port': os.getenv('aem_port', 45652),
    }
    return PythonAem(conf)
