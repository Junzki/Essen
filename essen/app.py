# -*- coding:utf-8 -*-
from celery import Celery
from celery.app.defaults import DEFAULTS


def init_celery(external_config=None):
    app = Celery('essen')
    app.config_from_object('essen.conf:settings')

    # Reload Celery's default settings.
    # Ref. http://docs.celeryproject.org/en/latest/reference/celery.html#celery.Celery.config_from_object
    for k, v in app.conf.items():
        default = DEFAULTS.get(k)
        if v and v != default:
            continue

        app.conf[k] = default

    return app


celery = init_celery()
