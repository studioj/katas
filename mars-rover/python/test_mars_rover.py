from unittest import TestCase

from .mars_rover import title, Rover


class TestMarsRover(TestCase):
    def test_the_title(self):
        """this test can be removed"""
        self.assertIn("mars", title)

    def test_mars_rover_provides_a_location(self):
        rover = Rover('N', 0, 0)
        self.assertEqual(rover.location, (0, 0))

    def test_mars_rover_provides_a_location_based_on_his_starting_location(self):
        rover = Rover('N', 1, 0)
        self.assertEqual(rover.location, (1, 0))
        rover = Rover('N', 1, 1)
        self.assertEqual(rover.location, (1, 1))

    def test_rover_moves_north_one_step_if_asked_to_go_forward_and_facing_north(self):
        rover = Rover('N', 0, 0)
        rover.forward()
        self.assertEqual(rover.location, (0, 1))
