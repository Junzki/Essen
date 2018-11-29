# -*- coding:utf-8 -*-
import requests
import iso8601

from essen.exceptions import RequestException


def handler(src, **kwargs):
    """
    Fetch coin price from coindisk.

    Args:
        - src: Fetch source

    Returns:
        - updateed: Upstream update time, in UTC.
        - List of coin price in several currencies.
    """
    res = requests.get(src)
    if res.status_code != 200:
        raise RequestException(res.status_code, res.text)

    try:
        content = res.json()
    except ValueError:
        raise ValueError("Badly formated JSON, content: %s." % res.text)

    updated = iso8601.parse_date(content['time']['updatedISO'])

    price = []
    for cur, detail in content['bpi'].items():
        _rate = detail['rate'].replace(',', '')
        try:
            _rate = float(_rate)
        except (TypeError, ValueError):
            _rate = None

        price.append({
            'currency': cur,
            'price': _rate
        })

    return updated, price
