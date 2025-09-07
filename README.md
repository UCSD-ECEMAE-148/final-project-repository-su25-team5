<div id="top"></div>

<h1 align="center">Image Filter Pipeline & Obstacle Avoidance</h1>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://jacobsschool.ucsd.edu/">
  <img src="https://github.com/UCSD-ECEMAE-148/winter-2024-final-project-team-4/blob/main/images/UCSDLogo_JSOE_BlueGold.png" alt="Logo" width="400" height="100">
  </a>
<h3>ECE/MAE148 Final Project</h3>
<p>
Team 5 Summer 2025
</p>


<img src="images/Team 5 RoboCar.jpg" alt="Logo" width="400" height="400">  

*Special thanks to Angel for the documentation.*
</div>




<!-- TABLE OF CONTENTS -->
<details>
  <summary><h1>Table of Contents<h1></summary>
  <ol>
    <li><a href="#overview">Overview</a></li>
      <ul>
        <li><a href="#youtube-videos">YouTube Videos</a></li>
        <li><a href="#key-features">Key Features</a></li>
      </ul>
    </li>
    <li><a href="#team-members">Team Members</a></li>
    <li><a href="#project-goals">Project Goals</a>
      <ul>
        <li><a href="#core-objectives">Core Objectives</a></li>
        <li><a href="#nice-to-have-features">Nice-to-Have Features</a></li>
      </ul>
    </li>
        <li><a href="#ros2-node-descriptions">ROS2 Node Descriptions</a>
      </ul>
    </li>
    <li><a href="#technologies-used">Technologies Used</a></li>
    <li><a href="#how-to-run">How to Run</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#steps">Steps</a></li>
      </ul>
    </li>
    <li><a href="#future-improvements">Future Improvements</a></li>
    <li><a href="#final-project-documentation">Final Project Documentation</a></li>
    <li><a href="#robot-design">Robot Design</a>
      <ul>
        <li><a href="#cad-parts">Car Parts</a>
          <ul>
            <li><a href="#custom-designed-parts">Custom Designed Parts</a></li>
            <li><a href="#open-source-parts">Open Source Parts</a></li>
          </ul>
        </li>
        <li><a href="#electronic-hardware">Electronic Hardware</a></li>
        <li><a href="#software">Software</a>
          <ul>
            <li><a href="#embedded-systems">Embedded Systems</a></li>
            <li><a href="#ros2">ROS2</a></li>
          </ul>
        </li>
      </ul>
    </li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
    <li><a href="#contacts">Contacts</a></li>
  </ol>
</details>

## Overview

This project focuses on developing an imaging process filter designated to improve the reliability of Donkey Car training across different environments. An image filter pipeline will be made to the OAK-D camera feed to normalize lighting conditions so that training and inference remain robust at any time of day.
In addition, LiDAR sensing will be integrated for obstacle detection, further improving the perception capabilities of the Donkey Car. Emergency avoidance will be provided to handle suddenly appearing objects, ensuring the safety of people, the driver, and the car itself.
ROS2 will be used as the link between donkey car and LiDAR sensing, where LiDAR scans are published to topics, and the control node fuses this data to generate safe and accurate driving commands.

<img src="https://github.com/UCSD-ECEMAE-148/winter-2024-final-project-team-4/blob/main/images/UCSDLogo_JSOE_BlueGold.png">

### **YouTube Videos:**

Click to watch "Filtering in Action"

[![Filter in Action](http://img.youtube.com/vi/sU_MpfjnF3E/0.jpg)](https://youtu.be/sU_MpfjnF3E "Filtering in Action")

Click to watch "5 PM Day Model Usage"

[![5 PM Day Model Usage](http://img.youtube.com/vi/hHPtVVqu_K4/0.jpg)](https://youtu.be/hHPtVVqu_K4 "5 PM Day Model Usage")

Click to watch "Night Model Usage"

[![Night Model Usage](http://img.youtube.com/vi/2x252IADBzo/0.jpg)](https://youtu.be/2x252IADBzo "Night Model Usage")

Click to watch "Obstacle Avoidance"

[![Obstacle Avoidance](http://img.youtube.com/vi/Y8Ywqo7uJKo/0.jpg)](https://youtu.be/Y8Ywqo7uJKo "Obstacle Avoidance")

Note that the setup of parts (such as camera position, compute power, and Donkey Car configuration) can vary from car to car, and tuning may be required to achieve the same effect.

### **Key Features**
- **Image Filtering:** Imaging is captured, enhanced, lifted, blurred, gray scaled, then a canny edge filter is applied.
- **Obstacle Avoidance:** LiDAR, or light detection and ranging, is used to measure distances between the car and objects in order to avoid collisions.
- **ROS2 Framework:** Custom ROS2 nodes are used for the functionalities listed above.
- **Donkey Car Framework:** Uses the OpenAI gym wrapper around the Self Driving Sandbox donkey simulator in order for deep learning image processing, allowing the use for autonomous use.
---

## Team Members

| Name              | Major                      | Class       |
|-------------------|----------------------------|-------------|
| Omar Hernandez    | Electrical Engineering     | Class of 2026 |
| Zhenyu Jiang      | Computer Engineering       | Class of 2026 |
| Angel Rubio       | Mechanical Engineering     | Class of 2026 |

---

## **Project Goals**

### **Core Objectives**
1. **Image Filtering:**
   - Implement a custom donkey car part that includes multitude of filters that can enhance an image throughout anytime of day which allows an ease of deep learning image processing for autonomous use. 

2. **Obstacle Avoidance:**
   - Using ROS2 as a framework for connecting the LiDAR and donkey car, the car will be able to stop or turn away from obstacles.

### **Nice-to-Have Features**
- **Faster/Cleaner Obstacle Avoidance:**
   - Have the robot car react faster and more efficiently to obstacles and in turn be able to react to moving obstacles.
- **Better Developer Kit:**
   - An improved kit with a more efficient G ram limit would allow for higher resolution photos when training the model, and a higher resolution allows for clearer photos used for image deep learning.
- **Fully intergation between obstacle avoidance from ros2 to donkey car**
  - Currently, we created a custom Donkey Car part to subscribe to the ROS2 topic, but it failed to override the Donkey Car while running. This may be due to overwriting from the joystick or an inability to correctly receive messages from the ROS node.
---

### **Donkey Car Custom part Descriptions**

 1. **The '''canny_filter'''** part
    - Applies a series of image processing steps to the input images: capture, enhancement, lifting, blurring, grayscale conversion, and Canny edge detection.

    - The number of filters applied can be turned on or off based on the average brightness of the input images.

 2. **'''The donkey_bridge part'''** (successfully subscribes to ROS2 topics but cannot feed data to the Donkey Car)
    - Subscribes to the /cmd_vel2 topic in ROS2.
    - Parses throttle and steering commands from messages and updates shared control values (angle and throttle) used by Donkey Car.
    
### **ROS2 Node Descriptions**

1. **The '''donkey_bridge_node'''** (initial test to link ROS2 and Donkey Car, but this approach does not work as intended)
    - Subscribes to the /cmd_vel2 topic in ROS2.
  
    - Parses throttle and steering commands from messages and updates shared control values (angle and throttle) used by Donkey Car.
  
    - Provides a workaround for the rclpy.init() conflict by allowing ROS2 commands to directly control the car without running inside manage.py.

2. **The '''safety_override_node'''**
    - Fuses inputs from LiDAR (/lidar_status) and camera (/camera_status) to make safety-critical driving decisions.
  
    - Implements rules such as stopping for obstacles, avoiding objects detected on the left or right, and slowing down when necessary.
    
    - Publishes safe driving commands as Twist messages on /cmd_vel, ensuring obstacle avoidance and safety overrides take priority over normal control commands.
  
    - Publishes safe driving commands as String messages on /cmd_vel2, ensuring obstacle avoidance and safety overrides take priority over normal control commands. It is intended to serve the Donkey Car, but this functionality is still under development.

3. **The ''''smart_avoid_node'''** 
   - Subscribes to LiDAR scan data (/scan) and divides the laser readings into front, left, and right sectors.

   - Determines if there is an obstacle ahead and decides the safest direction to move (LEFT, RIGHT, or FORWARD) based on the amount of free space in each sector.

   - Publishes the decision as a String message on /lidar_status for downstream nodes like safety_override_node.

   - Based on code from 148-spring-2025-final-project-team-15, with minor modifications.
---

## **Technologies Used**
- **ROS2:** Framework for data between nodes i.e. the image filter and camera pipeline, as well as the LiDAR for detecting obstacles.
- **Donkey Car:** Donkey Simulator is implemented into the ROS2 framework in order for deep-learning of the filtered imaging, allowing for autonomous driving.
- **VESC:** Controls the car's steering and throttle which is necessary for obstacle avoidance.
- **OAK-D Camera:** The eyes of our robocar, uses images recorded through the camera using Donkey Car, a model is trained for autonomous runs.
- **LiDAR:** Another pair of eyes of our robocar, the LiDAR allows for obstacle avoidance by measuring distance and the angle where an object is detected
  
---

## **How to Run**

### **Prerequisites**
- Install NoMachine for connection to Nvidia Jetson Nano Developer Kit
- Install ROS2 (Foxy recommended) on the Jetson
- Install ROS2 ucsd_robocar_hub2 packages
- Install donkey car inside the ros2 workspace
- Ensure the VESC is configured and calibrated.

### **Steps**
1. In Docker container, run ```source_ros2```
2. Enter the ```src``` directory and clone the repository:
   ```bash
   cd src
   git clone https://github.com/UCSD-ECEMAE-148/final-project-repository-su25-team5.git
   cd ..
   ```
3. install donkey car in ROS2 workspace:
   ```bash
   source_ros2
   git clone https://github.com/autorope/donkeycar 
   cd donkeycar
   git fetch --all --tags -f
   git checkout 4.5.1
   pip install -e .[nano]
   source_ros2
   ```
4. Launch the donkey car:
   ```bash
   cd UCSD-ECEMAE-148/final-project-repository-su25-team5/donkey_canny/
   python3 manage.py drive
   ``` 
5. Build the ROS2 workspace:
   ```bash
   source_ros2
   colcon build --packages-select ros_con2
   ```
6. Launch the ros system:
   ```bash
   ros2 launch ros_con2 safety_override_system.launch.py
   ```
   

### Final Project Documentation

* [Final Project Presentation](https://docs.google.com/presentation/d/19Qnh-O2huFwSPowrSBKmezatQEWL6zlXS5n7mhxw9v8/edit?usp=sharing)

<!-- Early Quarter -->
## Robot Design

### Car Parts

#### Custom Designed Parts
| Part | CAD Model/Laser Cut | Designer |
|------|--------------|------------|
| Camera Mount | <img src="images/Camera Mount.png" width="300" height="477" /> | Zhenyu
| LiDAR Mount | <img src="images/LiDAR Mount.png" width="300" height="477" /> | Angel
| GPS Mount (Used earlier in the quarter) | <img src="images/GPS Stand.png" width="300" height="530" /> | Angel
| VESC Mount | <img src="images/VESC Holder.png" width="235" height="202" /> | Angel
| OAK-D Lite Case | <img src="images/OAK-D Lite Case.png" width="300" height="250" /> | Omar 
| RoboCar Support Board | <img src="images/Support Board.png" width="300" height="250" /> | Omar



#### Open Source Parts
| Part | CAD Model | Source |
|------|--------|-----------|
| Jetson Nano Case | <img src="images/Jetson Nano Cover.png" width="300" height="214" /> | [Thingiverse](https://www.thingiverse.com/thing:3518410) |

### Electronic Hardware
Circuit Diagram of the electronics for the car.

<img src="images/ECE 148 Schematics.jpg" width="800" height="600" />

*Special thanks to Omar for soldering & fixing the broken components as well as organizing them.*

### Software
#### Embedded Systems
A wireless SSH connection was established with the Jetson Nano that contained a docker container with all the necessary packages and dependecies used to run programs in a ROS2 workspace. Connection of our host computers and the Jetson were used through NoMachine for Windows and Liinux terminals.

#### ROS2
The Docker Images, which were provided to us and pulled from the Docker Hub, contained the UCSD Robocar Module along with the ROS/ROS2 submodules that we utilized.
The UCSD Robocar Module runs on Linux OS (Ubuntu 20.04) and was initially developed by Dominic Nightingale, a graduate student at the University of California, San Diego.

*Special thanks to Zhenyu for addressing software concerns and commiting to working on the ROS2 framework.*

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
*Much thanks and appreciation to Professor Jack Silberman and our two awesome TA's Alexander and Jose for a great summer 2025! Credits to Team 1 Fall 2024 for the README.md template,n which they also gave credit to [@kiers-neely](https://github.com/kiers-neely) and Team 15 spring 2024 for the lidar_detection ros node*

<!-- CONTACTS -->
## Contacts
| Name | Email |
| ----------- | ----------- |
| Omar Hernandez | o2hernandez@ucsd.edu
| Zhenyu Jiang   | zhj014@ucsd.edu
| Angel Rubio    | acrubio@ucsd.edu
