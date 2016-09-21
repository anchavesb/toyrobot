# Toy Robot

Toy Robot simulator

### Prerequisities

Python 3.5

### How to run

Given a commands.txt file with commands, the simulator can be invoqued using one of the following ways:

```bash
$ python3.5 command.py < commands.txt
```

```bash
$ cat commands.txt |python3.5 command.py
```

```bash
$ python3.5 command.py commands.txt
```

Alternatively, commands can be typed in an interactive session:

```bash
$ python3.5 command.py
```

## Running the tests

There are two test classes, one for testing the robot and one for testing the command interface. To run the test classes one must issue the following:

```bash
$ python3.5 -m unittest test_robot.py

$ python3.5 -m unittest test_command.py
```