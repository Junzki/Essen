# -*- coding:utf-8 -*-
""" Task for sample.
"""
from essen.app import celery


@celery.task
def hello():
    print('Aloha!')
