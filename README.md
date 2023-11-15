
Bluetooth-Controlled Robot with Live Video Feed Tracking
Overview
This repository contains the code and documentation for a robot that can be controlled via Bluetooth communication based on messages received from a live video feed tracking the position of a green object. The robot is built using the SPIKE Prime robotics kit, and it utilizes computer vision techniques to track the movement of a green object in real-time.

Prerequisites
Before running the code, make sure you have the following:

LEGO SPIKE Prime robotics kit
A computer with a compatible Bluetooth module
A webcam or a camera connected to the computer
Python 3.x installed on your computer
Required Python libraries (install using pip install -r requirements.txt)
Setup
Build the SPIKE Prime Robot:
Assemble the robot using the SPIKE Prime set according to the provided instructions.

Connect the Bluetooth Module:
Ensure that your computer has a Bluetooth module and is paired with the SPIKE Prime robot.# SPIKE-Prime-BLE
Usage
Start the Live Video Feed:
The code initializes the webcam or camera connected to your computer. Ensure that the camera has a clear view of the area where the green object will be placed.

Place the Green Object:
Position a green object in the view of the camera. The robot will track and follow this object.

Control the Robot:
Use a Bluetooth-enabled device (e.g., a smartphone) to send control messages to the robot. The messages can include commands such as "forward," "backward," "left," and "right."

Enjoy the Robot's Movement:
The SPIKE Prime robot will move based on the commands received via Bluetooth, following the tracked green object in real-time.

Customization
Feel free to customize the code to fit your specific requirements. You can adjust parameters related to computer vision, Bluetooth communication, and robot movement in the main.py file.

Issues and Contributions
If you encounter any issues or have suggestions for improvement, please open an issue on the GitHub repository. Contributions are welcome!
