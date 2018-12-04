# -*- coding:utf-8 -*-
from unittest import TestCase
from essen.conf import settings


class TestSettings(TestCase):

    def test_load_settings(self):
        self.assertEqual(settings.BROKER_TRANSPORT, 'sqs')
