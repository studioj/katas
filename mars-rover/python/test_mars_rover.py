from unittest import TestCase

from .mars_rover import title


class TestMarsRover(TestCase):
    def test_the_title(self):
        """this test can be removed"""
        self.assertIn("mars", title)
