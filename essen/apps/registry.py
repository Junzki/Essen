# -*- coding:utf-8 -*-
""" App registry.
"""
import importlib


class App(object):

    _installed_apps = None

    def __init__(self):
        self._installed_apps = list()
