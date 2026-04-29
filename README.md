# CleaningRobotPy
_CleaningRobotPy_ is an autonomous cleaning robot that moves in a room, detects obstacles, and cleans dust from the floor using a built-in cleaning system. It is equipped with sensors and motors that allow it to navigate and operate efficiently.

## Features

- Autonomous movement with two DC motors (wheels & rotation)
- Infrared sensor for obstacle detection
- Intelligent Battery Sensor (IBS) to monitor battery levels
- Recharge LED indicator when battery is low
- Cleaning system with two rotating brushes
- Controlled by a Route Management System (RMS) that tracks room layout and obstacles
- GPIO communication for seamless integration with hardware

## How It Works

1. When powered on, the robot activates its cleaning system and starts moving.

2. It follows movement commands from the Route Management System (RMS).

3. If it encounters an obstacle, the infrared sensor detects it and adjusts movement accordingly.

4. The battery sensor (IBS) continuously monitors battery charge.

5. If the charge is too low, the recharge LED turns on, signaling that it needs to be recharged.

6. The room is represented as a rectangular grid where the RMS keeps track of obstacles and the robot's position.

## Components & Sensors

- DC Motor (wheels) – Moves the robot forward

- DC Motor (rotation) – Rotates the robot left or right

- Route Management System (RMS) – Sends movement commands

- Infrared Sensor – Detects obstacles

- Intelligent Battery Sensor (IBS) – Checks remaining charge

- Recharge LED – Signals low battery

- Cleaning System – Two rotating brushes

## Installation & Usage

1. Clone the repository:
```
git clone https://github.com/yourusername/cleaningrobotpy.git
cd cleaningrobotpy
```
2. Install dependencies (if needed):
```
pip install -r requirements.txt
```
3. Run the simulation:
```
python cleaning_robot.py
```


## License

This project is licensed under the MIT License.

