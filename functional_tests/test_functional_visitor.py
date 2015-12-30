"""
Functional tests for checking a basic visitor can visit the site.
"""
from functional_tests.base import BaseFunctionalTest


class TestFunctionalVisitor(BaseFunctionalTest):

    def test_visitor_sees_scale_scores(self):
        # Kara goes to visit the homepage.
        self.browser.get(self.live_server_url)

        # She sees she's reached the right page.
        self.assertEqual(self.browser.title, "Greg Olmschenk")

        # Next, she sees the section displaying education.
        headers = self.browser.find_elements_by_tag_name('h2')
        self.assertIn('Education', [header.text for header in headers])

        # There are also links to published essays.
        self.fail()

        # She clicks on one.

        # The essay comes up ready to read.

        # It's too long to read at the moment, so Kara closes out of the page.
