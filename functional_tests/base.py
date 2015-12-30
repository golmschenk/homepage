"""
Functional template base class.
"""
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class BaseFunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
