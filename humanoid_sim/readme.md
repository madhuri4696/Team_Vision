# Humanoid Motor Control – Gazebo Simulation Demo

## 1. Overview

This project demonstrates a humanoid motor-control concept using the Gazebo simulator.

- Target: 32-DOF humanoid with DC motor control, ±180° joint range, 5 kg payload capability, 
  humanoid walking speed ~1 m/s and arm endpoint speed ~0.3 m/s.
- This submission focuses on:
  - A humanoid model loaded in Gazebo
  - A subset of joints that can be moved via GUI and/or position controllers
  - An architecture that scales to all 32 DOF

## 2. Files

- `test_hum.sdf`  
  Main Gazebo world file used in the demo.  
  Loads the humanoid model and associated elements (ground, light, etc).

- `screenshots/sim_full_humanoid.png`  
  Full view of the humanoid in Gazebo.

- `screenshots/sim_joint_moved.png`  
  Example of a joint movement (e.g., arm raised / leg bent).

## 3. How to Run

From Ubuntu (WSL):

```bash
cd /mnt/c/Users/madhu/OneDrive/Desktop/vision_25/Gazebo/humanoid_sim_submission
gz sim -v 4 test_hum.sdf

### 4. JOINT Control

/model/humanoid_dof_demo/joint/j_shoulder/0/cmd_pos

/model/humanoid_dof_demo/joint/j_elbow/0/cmd_pos

gz topic -t "/model/humanoid_dof_demo/joint/j_shoulder/0/cmd_pos" \ -m gz.msgs.Double -p "data: 0.8"

