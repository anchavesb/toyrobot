import unittest
import command
from io import StringIO
from unittest.mock import patch

class TestCommand(unittest.TestCase):
    """Tests for the Command program"""

    @patch('sys.stdout', new_callable=StringIO)
    def test_expected_output(self, mock_stdout):
        command.main(["PLACE 0,0,NORTH","MOVE","REPORT"],5,5)
        self.assertEqual(mock_stdout.getvalue(), "0,1,NORTH\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_expected_output2(self, mock_stdout):
        command.main(["PLACE 0,0,NORTH","LEFT","REPORT"],5,5)
        self.assertEqual(mock_stdout.getvalue(), "0,0,WEST\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_expected_output2(self, mock_stdout):
        command.main(["PLACE 1,2,EAST","MOVE","MOVE","LEFT","MOVE","REPORT"],5,5)
        self.assertEqual(mock_stdout.getvalue(), "3,3,NORTH\n")

