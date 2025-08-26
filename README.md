<div id="top"></div>

<h1 align="center">Image Filter Pipeline</h1>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://jacobsschool.ucsd.edu/">
    *ADD PHOTO OF CAR HERE*
  </a>
<h3>ECE/MAE148 Final Project</h3>
<p>
Team 5 Summer 2025
</p>

<img src="images/ROBOCAR.jpg" alt="Logo" width="400" height="400">
</div>




<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#overview">Overview</a>
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
In addition, we will integrate LiDAR sensing for obstacle detection and mapping, further improving the perception capabilities of the Donkey Car. LiDAR data will complement the filtered camera input by providing reliable depth and spatial awareness.
We will use ROS2 as the link to filters and LiDAR sensing, where filtered camera images and LiDAR scans are published to topics, and the control node fuses this data to generate safe and accurate driving commands.


*Add links to videos needed in order to make a good overview*


### **Key Features**
- **1**
- **2**
- **3**
- **4**
- **5**

---

## Team Members

| Name              | Major                      | Class       |
|-------------------|----------------------------|-------------|
| Zhenyu Jiang      | Computer Engineering       | Class of 2026 |
| Omar Hernandez    | Electrical Engineering     | Class of 2026 |
| Angel Rubio       | Mechanical Engineering     | Class of 2026 |

---

## **Project Goals**

### **Core Objectives**
1. **Filtering:**
   - Implement a filter that

2. **Goal 2**

### **Nice-to-Have Features**
  
---

## **System Architecture**

### **Node Descriptions**

1. 

2. 

---

## **Technologies Used**

---

## **How to Run**

__Detailed instructions can be found in ball_vision_info.md__

### **Prerequisites**
- Install ROS2 (Foxy recommended).
- Set up the DepthAI SDK.
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

- Integrate a path prediction algorithm for smarter ball interception.
- Enhance the PID controller for faster and smoother responses.
- Explore deep learning-based ball detection for improved accuracy in varying lighting conditions.


### Final Project Documentation

* [Final Project Presentation](https://docs.google.com/presentation/d/19Qnh-O2huFwSPowrSBKmezatQEWL6zlXS5n7mhxw9v8/edit?usp=sharing)

<!-- Early Quarter -->
## Robot Design

### CAD Parts

#### Custom Designed Parts
| Part | CAD Model | Designer |
|------|--------------|------------|
| Camera Mount | <img src="images/Camera Mount.png" width="300" height="477" /> | Zhenyu
| LiDAR Mount | <img src="images/LiDAR Case.png" width="300" height="202" /> | Angel
| GPS Mount | <img src="images/LiDAR Case.png" width="300" height="202" /> | Angel
| VESC Mount | <img src="images/LiDAR Case.png" width="300" height="202" /> | Angel


#### Open Source Parts
| Part | CAD Model | Source |
|------|--------|-----------|
| Jetson Nano Case | <img src="images/Jetson Case.png" width="300" height="214" /> | [Thingiverse](https://www.thingiverse.com/thing:5237669) |
| Oak-D Lite Case | <img src="images/Camera Case.png" width="300" height="250" /> | [Thingiverse](https://www.thingiverse.com/thing:3518410) |


### Electronic Hardware
Circuit Diagram of the electronic hardware setup for the car.

<img src="https://github.com/kiers-neely/ucsd-mae-148-team-4/assets/161119406/6f7501ee-382a-4590-9c0a-f8ce738efec3" width="800" height="400" />
*Special thanks to Omar for soldering and fixing the broken components*

### Software
#### Embedded Systems
Our team utilized a wirless SSH to a Jetson Nano that contained a docker container with all the necessary packages and dependecies used to run our program in a ROS2 workspace. SSH was done via both Mac terminal and Windows PC with Virtual Machine.

#### ROS2
The Docker Images, which were provided to us and pulled from the Docker Hub, contained the UCSD Robocar Module along with the ROS/ROS2 submodules that we utilized during project prototyping and lane following.
The UCSD Robocar Module, running on Linux OS (Ubuntu 20.04), was initially developed by Dominic Nightingale, a graduate student at the University of California, San Diego

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
*Much thanks and appreciation to Professor Jack Silberman and our two awesome TA's Alexander and Jose for a great summer 2025! Credits to Team 1 Fall 2024 for the README.md template in which they also gave credit to [@kiers-neely](https://github.com/kiers-neely)*

<!-- CONTACTS -->
## Contacts

* Zhenyu Jiang   | zhj014@ucsd.edu
* Omar Hernandez | o2hernandez@ucsd.edu
* Angel Rubio    | acrubio@ucsd.edu
