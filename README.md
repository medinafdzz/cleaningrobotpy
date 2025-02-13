# cleaningrobotpy
_cleaningrobotpy_ is cleaning robot, which moves in a room and cleans the dust on the floor along the way. To clean the dust, the robot is equipped with a cleaning system placed below it, consisting of two rotating brushes. When the robot is turned on, it turns on the cleaning system.

The robot moves thanks to two DC motors, one controlling its wheels and one controlling its rotation. The robot's movements are contolled by a Route Management System (RMS), which sends commands to the robot. While moving in the room, the robot can encounter obstacles; these can be detected thanks to an infrared distance sensor placed in the front of it.

The robot checks the charge left in its internal battery. To do so, it is equipped with an Intelligent Battery Sensor (IBS). Furthermore, a recharging LED is mounted on the top of the robot to signal that it needs to be recharged.

The room, where the robot moves, is represented as a rectangular grid with _x_ and _y_ coordinates. The origin cell of the grid – i.e., _(0,0)_ – is located at the bottom-left corner. A cell of the grid may contain or not an obstacle. The RMS keeps track of the room layout, including the last known positions of the obstacles in the room.

To recap, the following sensors, actuators, and systems are present:
* A DC motor to control the wheels in order to move the robot forward.
* A DC motor to control the rotation of the body of the robot, in order to make it rotate left or right.
* An RMS, sending commands to the robot.
* An infrared distance sensor used to detect obstacles.
* An IBS to determine the battery charge left.
* A recharge LED.
* A cleaning system, consisting of two rotating brushes.

The communication between the main board and the other components happens via GPIO pins (BOARD mode).