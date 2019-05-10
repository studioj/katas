from unittest import TestCase

from .mars_rover import title, Rover


class TestMarsRover(TestCase):
    def test_the_title(self):
        """this test can be removed"""
        self.assertIn("mars", title)

    def test_mars_rover_provides_a_location(self):
        rover = Rover('N', 0, 0)
        self.assertEqual(rover.location, (0, 0))
