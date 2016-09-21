import sys
import argparse
import re
import operator

DIMX = DIMY = 5 #SIZE OF THE TABLE
DIRECTIONS = ["NORTH", "SOUTH", "WEST", "EAST"] #VALID DIRECTIONS
COMMANDS = ["PLACE", "MOVE", "LEFT", "RIGHT", "REPORT"] #VALID COMMANDS

class Robot:
    """
    Manager of Robot commands within the table
    """

    """Dict with the actions to take given the current direction.
    Left: The direction to take when left command is risen
    West: The direction to take when right command is risen
    Move: A callable to either _moveX or _moveY method accordingly to current direction
    """
    CONFIG = {
        "NORTH": {"left": "WEST", "right": "EAST", "move": operator.methodcaller('_moveY', 1)},
        "SOUTH": {"left": "EAST", "right": "WEST", "move": operator.methodcaller('_moveY', -1)},
        "EAST": {"left": "NORTH", "right": "SOUTH", "move": operator.methodcaller('_moveX', 1)},
        "WEST": {"left": "SOUTH", "right": "NORTH", "move": operator.methodcaller('_moveX', -1)},
    }

    def __init__(self, dimx, dimy):
        """Class constructor
        dimx -- Size of the world in X direction
        dimy -- Size of the world in Y direction
        """
        self.dimx = dimx
        self.dimy = dimy
        self.posx = self.posy = self.direction = None

    def _check_valid(self, command):
        """Check whether a command is allowed to run"""

        if (self.posx is None or self.posy is None) and command["name"] != "PLACE": #Robot has not been placed before
            return False
        if command["name"] not in COMMANDS: #Invalid command
            return False
        return True

    def _place(self, command):
        """Handles the PLACE x,y,direction command"""

        x = command["x"]
        y = command["y"]
        direction = command["direction"]

        assert 0 <= x < self.dimx, "Invalid X"
        assert 0 <= y < self.dimy, "Invalid Y"
        assert direction in DIRECTIONS, "Invalid direction"

        self.posx = x
        self.posy = y
        self.direction = direction

    def _moveX(self, step):
        """Moves the robot a number of steps in X direction"""
        if 0 <= self.posx + step < self.dimx:
            self.posx = self.posx + step

    def _moveY(self, step):
        """Moves the robot a number of steps in Y direction"""
        if 0 <= self.posy + step < self.dimy:
            self.posy = self.posy + step

    def _move(self, command):
        """Handles the MOVE command"""
        Robot.CONFIG[self.direction]["move"](self)

    def _left(self, command):
        """Handles the LEFT command"""
        self.direction = Robot.CONFIG[self.direction]["left"]

    def _right(self, command):
        """Handles the RIGHT command"""
        self.direction = Robot.CONFIG[self.direction]["right"]

    def _report(self, command):
        """Handles the REPORT command"""
        return "%d,%d,%s" % (self.posx, self.posy, self.direction)

    def command(self, command):
        """Entry point method for all commands

        command -- A dict object with command name and parameters, i.e. {'name': 'PLACE', 'x': 0, 'y': 0}
        """
        if self._check_valid(command): #Ignore command if not valid
            return operator.methodcaller("_"+command["name"].lower(), command)(self)
#End class

def parse_command(command):
    """Check that a line is a valid command and returns a Command dict"""
    groups = re.match(r"^(MOVE|LEFT|RIGHT|REPORT)$", command)
    if groups is not None:
        return {"name": groups.group(1)}

    groups = re.match(r"^PLACE (\d),(\d),(NORTH|SOUTH|EAST|WEST)$", command)
    if groups is not None:
        return {"name": "PLACE",
                "x": int(groups.group(1)),
                "y": int(groups.group(2)),
                "direction": groups.group(3)}

    raise Exception("Invalid Command")


def main(stdin, dimx, dimy):
    robot = Robot(dimx, dimy)

    for command in stdin:
        try:
            command = parse_command(command)
            #print(command)
            output = robot.command(command)
            if isinstance(output, str): print(output)
        except Exception as e:
            print("Exception: %s" % e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input', nargs='?', type=argparse.FileType('r'), default=sys.stdin)

    args = parser.parse_args()

    main(args.input, DIMX, DIMY)

