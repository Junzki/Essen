# -*- coding:utf-8 -*-
import os
from unittest import TestCase
from essen.conf import settings, ENVIRONMENT_VARIABLE


class TestSettings(TestCase):
    SETTINGS_MODULE = 'tests.test_core.settings'

    def prepare(self):
        os.environ.setdefault(ENVIRONMENT_VARIABLE, self.SETTINGS_MODULE)

    def test_load_settings(self):
        self.prepare()

        self.assertEqual(settings.BROKER_TRANSPORT, 'sqs')
