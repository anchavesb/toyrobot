import unittest
from command import Robot

class TestRobot(unittest.TestCase):
    """Unit Tests for the Robot"""

    #Constants and commands
    INITIAL_PLACEMENT = {"name": "PLACE", "x":0, "y":0, "direction": "NORTH"}
    LEFT_COMMAND = {"name": "LEFT"}
    RIGHT_COMMAND = {"name": "RIGHT"}
    MOVE_COMMAND = {"name": "MOVE"}

    def setUp(self):
        """Test case set up"""
        self.robot = Robot(5,5)

    def _assert_robot_attributes(self, x, y, direction):
        """Assert that the internal state of the robot is equal to the method parameters"""
        self.assertEqual(self.robot.posx, x)
        self.assertEqual(self.robot.posy, y)
        self.assertEqual(self.robot.direction, direction)

    def test_valid_placement(self):
        self.robot.command(TestRobot.INITIAL_PLACEMENT)
        self._assert_robot_attributes(0,0,"NORTH")

    def test_invalid_placement(self):
        with self.assertRaises(AssertionError) as context:
            self.robot.command({"name": "PLACE",
                            "x": -1,
                            "y": -1,
                            "direction": "NORTH"})

        self._assert_robot_attributes(None, None, None)

        with self.assertRaises(AssertionError) as context:
            self.robot.command({"name": "PLACE",
                                "x": 5,
                                "y": 5,
                                "direction": "NORTH"})

        self._assert_robot_attributes(None, None, None)

        with self.assertRaises(AssertionError) as context:
            self.robot.command({"name": "PLACE",
                                "x": 0,
                                "y": 0,
                                "direction": "NORTHY"})

        self._assert_robot_attributes(None, None, None)

    def test_commands_discarded(self):
        self.robot.command(TestRobot.LEFT_COMMAND)
        self._assert_robot_attributes(None, None, None)

    def test_left(self):
        self.robot.command(TestRobot.INITIAL_PLACEMENT)
        self.robot.command(TestRobot.LEFT_COMMAND)
        self._assert_robot_attributes(0, 0, "WEST")
        self.robot.command(TestRobot.LEFT_COMMAND)
        self._assert_robot_attributes(0, 0, "SOUTH")
        self.robot.command(TestRobot.LEFT_COMMAND)
        self._assert_robot_attributes(0, 0, "EAST")
        self.robot.command(TestRobot.LEFT_COMMAND)
        self._assert_robot_attributes(0, 0, "NORTH")

    def test_right(self):
        self.robot.command(TestRobot.INITIAL_PLACEMENT)
        self.robot.command(TestRobot.RIGHT_COMMAND)
        self._assert_robot_attributes(0, 0, "EAST")
        self.robot.command(TestRobot.RIGHT_COMMAND)
        self._assert_robot_attributes(0, 0, "SOUTH")
        self.robot.command(TestRobot.RIGHT_COMMAND)
        self._assert_robot_attributes(0, 0, "WEST")
        self.robot.command(TestRobot.RIGHT_COMMAND)
        self._assert_robot_attributes(0, 0, "NORTH")

    def test_valid_move(self):
        self.robot.command(TestRobot.INITIAL_PLACEMENT)
        self.robot.command(TestRobot.MOVE_COMMAND)
        self._assert_robot_attributes(0, 1, "NORTH")
        self.robot.command({"name": "PLACE", "x":1, "y":1, "direction":"SOUTH"})
        self.robot.command(TestRobot.MOVE_COMMAND)
        self._assert_robot_attributes(1, 0, "SOUTH")
        self.robot.command({"name": "PLACE", "x": 2, "y": 2, "direction": "WEST"})
        self.robot.command(TestRobot.MOVE_COMMAND)
        self._assert_robot_attributes(1, 2, "WEST")
        self.robot.command({"name": "PLACE", "x": 3, "y": 3, "direction": "EAST"})
        self.robot.command(TestRobot.MOVE_COMMAND)
        self._assert_robot_attributes(4, 3, "EAST")

    def test_robot_not_falling(self):
        self.robot.command({"name": "PLACE", "x":0, "y":0, "direction":"SOUTH"})
        self.robot.command(TestRobot.MOVE_COMMAND)
        self.robot.command(TestRobot.MOVE_COMMAND)
        self._assert_robot_attributes(0, 0, "SOUTH")
        self.robot.command(TestRobot.RIGHT_COMMAND)
        self.robot.command(TestRobot.MOVE_COMMAND)
        self._assert_robot_attributes(0, 0, "WEST")
        self.robot.command({"name": "PLACE", "x": 4, "y": 4, "direction": "NORTH"})
        self.robot.command(TestRobot.MOVE_COMMAND)
        self._assert_robot_attributes(4, 4, "NORTH")
        self.robot.command(TestRobot.RIGHT_COMMAND)
        self.robot.command(TestRobot.MOVE_COMMAND)
        self._assert_robot_attributes(4, 4, "EAST")


