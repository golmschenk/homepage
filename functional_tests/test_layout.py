"""
Simple checks that the layout was actually loaded.
"""

from .base import BaseFunctionalTest


class TestLayout(BaseFunctionalTest):
    def test_smoke_for_layout(self):
        """
        A smoke test for the layout. Helps confirm the layout was actually loaded.
        """
        # Kara goes to the homepage.
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # She notices that a div is styled such that it's centered and
        # it doesn't span the entire window.
        first_div = self.browser.find_elements_by_tag_name('div')[0]
        self.assertAlmostEqual(
            first_div.location['x'] + first_div.size['width'] / 2,
            512,
            delta=5
        )
        self.assertLess(first_div.size['width'], 950)
