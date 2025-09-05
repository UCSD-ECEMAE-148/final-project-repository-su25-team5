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
</div>




<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#overview">Overview</a></li>
      <ul>
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
    <li><a href="#system-architecture">System Architecture</a>
      <ul>
        <li><a href="#node-descriptions">Node Descriptions</a></li>
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
        <li><a href="#cad-parts">CAD Parts</a>
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
            <li><a href="#donkeycar-ai">DonkeyCar AI</a></li>
          </ul>
        </li>
      </ul>
    </li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## Overview

This project focuses on developing an imaging process filter designated to improve the reliability of Donkey Car training across different environments. An image filter pipeline will be made to the OAK-D camera feed to normalize lighting conditions so that training and inference remain robust at any time of day.
In addition, LiDAR sensing will be integrated for obstacle detection and mapping, further improving the perception capabilities of Donkey Car. LiDAR data will complement the filtered camera input by providing reliable depth and spatial awareness.
ROS2 will be used as the link between filters and LiDAR sensing, where filtered camera images and LiDAR scans are published to topics, and the control node fuses this data to generate safe and accurate driving commands.

### **YouTube Videos:**

Click to watch "Filtering in Action":

[![Filter in Action](http://img.youtube.com/vi/sU_MpfjnF3E/0.jpg)](https://youtu.be/sU_MpfjnF3E "Filtering in Action")

Click to watch "5 PM Day Model Usage":

[![5 PM Day Model Usage](http://img.youtube.com/vi/hHPtVVqu_K4/0.jpg)](https://youtu.be/hHPtVVqu_K4 "5 PM Day Model Usage")

Click to watch "Night Model Usage":

[![Night Model Usage](http://img.youtube.com/vi/2x252IADBzo/0.jpg)](https://youtu.be/2x252IADBzo "Night Model Usage")


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
   - Implement a multitude of filters that can enhance an image throughout anytime of day which allows an ease of deep learning image processing for autonomous use. 

2. **Obstacle Avoidance:**
   - Using ROS2 as a framework for connecting the image filtering and LiDAR, the car will be able to ```stop``` or ```turn``` away from obstacles.

### **Nice-to-Have Features**
- **Faster Obstacle Avoidance:**
   - Have the robot car react faster to obstacles and in turn be able to react to moving obstacles.
- **Improved GPU Cluster:**
   - An improved GPU cluster allows for higher resolution photos when training the model, and a higher resolution allows for clearer photos used for image deep learning. 
---

### **Node Descriptions**

1. 

2. 

---

## **Technologies Used**
- **ROS2:** Framework for data between nodes i.e. the image filter and camera pipeline, as well as the LiDAR for detecting obstacles.
- **Donkey Car:** Donkey Simulator is implemented into the ROS2 framework in order for deep-learning of the filtered imaging, allowing for autonomous driving.
- **VESC:** Controls the car's steering and throttle which is necessary for obstacle avoidance.
  
---

## **How to Run**

__Detailed instructions can be found in ...__

### **Prerequisites**
- Install NoMachine for connection to Nvidia Jetson Nano Developer Kit
- Install ROS2 (Foxy recommended) on the Jetson
- Set up the DepthAI SDK
  - In Docker container ```projects``` directory
  ```bash
  git clone https://github.com/luxonis/depthai-python
  ```
- Ensure the VESC is configured and calibrated.

### **Steps**
1. In Docker container, run ```source_ros2```
1. Enter the ```src``` directory and clone the repository:
   ```bash
   cd src
   git clone https://github.com/UCSD-ECEMAE-148/fall-2024-final-project-team-1/tree/main
   cd ..
   ```
2. Build the ROS2 workspace:
   ```bash
   colcon build --packages-select ball_vision_package
   ```
3. Launch the system:
   ```bash
   ros2 launch ball_vision_package ball_tracking.launch.py
   ```
   
## **Future Improvements**

- More records to improve autonomous driving in different lightings
- 


### Final Project Documentation

* [Final Project Presentation](https://docs.google.com/presentation/d/19Qnh-O2huFwSPowrSBKmezatQEWL6zlXS5n7mhxw9v8/edit?usp=sharing)

<!-- Early Quarter -->
## Robot Design

### CAD Parts

#### Custom Designed Parts
| Part | CAD Model | Designer |
|------|--------------|------------|
| Camera Mount | <img src="images/Camera Mount.png" width="300" height="477" /> | Zhenyu
| LiDAR Mount | <img src="images/LiDAR Mount.png" width="300" height="477" /> | Angel
| GPS Mount 
(Not used in final project but used earlier in the quarter) | <img src="images/GPS Stand.png" width="300" height="530" /> | Angel
| VESC Mount | <img src="images/VESC Holder.png" width="235" height="202" /> | Angel


#### Open Source Parts
| Part | CAD Model | Source |
|------|--------|-----------|
| Jetson Nano Case | <img src="images/Jetson Nano Cover.png" width="300" height="214" /> | [Thingiverse](https://www.thingiverse.com/thing:3518410) |
| Oak-D Lite Case | <img src="images/Camera Case.png" width="300" height="250" /> | [Thingiverse](https://www.thingiverse.com/thing:3518410) |


### Electronic Hardware
Circuit Diagram of the electronics for the car.

<img src="images/ECE 148 Schematics.jpg" width="800" height="400" />

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
*Much thanks and appreciation to Professor Jack Silberman and our two awesome TA's Alexander and Jose for a great summer 2025! Credits to Team 1 Fall 2024 for the README.md template in which they also gave credit to [@kiers-neely](https://github.com/kiers-neely)*

<!-- CONTACTS -->
## Contacts

* Omar Hernandez | o2hernandez@ucsd.edu
* Zhenyu Jiang   | zhj014@ucsd.edu
* Angel Rubio    | acrubio@ucsd.edu
