"""
Functional tests for checking a basic visitor can visit the site.
"""
from django.test import override_settings

from functional_tests.base import BaseFunctionalTest
from profile.models import Essay


@override_settings(DEBUG=True)
class TestFunctionalVisitor(BaseFunctionalTest):

    def test_visitor_sees_profile(self):
        # -- Setup some essays in the database.
        essay1 = Essay.objects.create(title='An Awesome Essay')

        # Kara goes to visit the homepage.
        self.browser.get(self.live_server_url)

        # She sees she's reached the right page.
        self.assertEqual(self.browser.title, "Greg Olmschenk")

        # Next, she sees the section displaying education.
        headers = self.browser.find_elements_by_tag_name('h2')
        self.assertIn('Education', [header.text for header in headers])

        # There are also links to published essays.
        headers = self.browser.find_elements_by_tag_name('h2')
        self.assertIn('Essays', [header.text for header in headers])

        # She clicks on one.
        essay_div = self.browser.find_element_by_id('essay_div')
        essay_div.find_elements_by_tag_name('button')[0].click()

        # The essay comes up ready to read.
        self.assertEqual(self.browser.title, "Name of the essay")

        # It's too long to read at the moment, so Kara closes out of the page.
        self.browser.close()
