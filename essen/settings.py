# -*- coding:utf-8 -*-
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SOURCES = {
    'CoinDesk': {
        'path': 'https://api.coindesk.com/v1/bpi/currentprice.json',
        'currency': ['USD', 'GBP', 'EUR']
    }
}
