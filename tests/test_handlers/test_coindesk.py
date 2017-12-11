# -*- coding:utf-8 -*-
import datetime
from coin_spider.handlers import coindesk

def test_coindesk_fetch():
    """
    Test coindesk handler.
    """
    src = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    update, rates = coindesk.handler(src)

    assert isinstance(update, datetime.datetime)

    for item in rates:
        assert 'currency' in item
        assert 'price' in item
        assert isinstance(item['price'], (int, float)) or item['price'] is None
