# -*- coding:utf-8 -*-
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

INCLUDE_PACKAGES = (
    'tasks',
)

SOURCES = {
    'CoinDesk': {
        'path': 'https://api.coindesk.com/v1/bpi/currentprice.json',
        'currency': ['USD', 'GBP', 'EUR']
    }
}


# Celery Settings
BROKER_TRANSPORT = 'redis'
CELERY_REDIS_HOST = 'localhost'
CELERY_REDIS_PORT = 6379
CELERY_REDIS_DB = 0
CELERY_REDIS_PASSWORD = ''
CELERYD_PREFETCH_MULTIPLIER = 4
