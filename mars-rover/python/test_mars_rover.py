from unittest import TestCase

from .mars_rover import title, Rover


class TestMarsRover(TestCase):
    def test_the_title(self):
        """this test can be removed"""
        self.assertIn("mars", title)

    def test_mars_rover_moves_north_when_facing_north_and_asked_to_go_forward(self):
        rover = Rover(0, 0)
