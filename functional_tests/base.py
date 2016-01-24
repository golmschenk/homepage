"""
Functional template base class.
"""
from django.test import override_settings
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


@override_settings(DEBUG=True)
class BaseFunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
