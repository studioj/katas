from unittest import TestCase

from .mars_rover import title, Rover


class TestMarsRover(TestCase):
    def test_the_title(self):
        """this test can be removed"""
        self.assertIn("mars", title)

    def test_mars_rover_provides_a_location_based_on_his_starting_location(self):
        rover = Rover('N')
        self.assertEqual(rover.location, (0, 0))

    def test_rover_moves_north_one_step_if_asked_to_go_forward_and_facing_north(self):
        rover = Rover('N')
        rover.forward()
        self.assertEqual(rover.location, (0, 1))

    def test_rover_moves_south_one_step_if_asked_to_go_forward_and_facing_south(self):
        rover = Rover('S')
        rover.forward()
        self.assertEqual(rover.location, (0, -1))

    def test_rover_moves_east_one_step_if_asked_to_go_forward_and_facing_east(self):
        rover = Rover('E')
        rover.forward()
        self.assertEqual(rover.location, (1, 0))

    def test_rover_moves_west_one_step_if_asked_to_go_forward_and_facing_west(self):
        rover = Rover('W')
        rover.forward()
        self.assertEqual(rover.location, (-1, 0))
