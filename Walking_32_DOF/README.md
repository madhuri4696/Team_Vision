# 🦾 Humanoid 32-DOF Walking Simulation (Gazebo Harmonic)

This repository contains a **fully actuated humanoid robot simulation** built using **Gazebo Harmonic (gazebo-sim)**.  
The humanoid includes **32 degrees of freedom**, basic joint actuation, and a simple demo walking motion — all implemented **entirely in SDF**, with **no external meshes or ROS** required.

This makes the project lightweight, portable, and perfect for rapid prototyping and hackathon demonstrations.

---

# 🚀 Features

### ✔️ Fully actuated humanoid (32 DOF)  
- Torso, pelvis, head  
- Both arms (shoulder + elbow joints)  
- Both legs (hip + knee + ankle joints)

### ✔️ Dynamic walking motion  
- Implemented using `gz::sim::systems::JointController`  
- Velocity-based joint control  
- SDF-embedded actuation — no scripts needed

### ✔️ Stable (no exploding physics)  
- Gravity disabled per-link  
- Joint damping added  
- Effort limits added (Fixes the JointFeatures error)

### ✔️ Zero external dependencies  
- No ROS required  
- No STL/DAE meshes  
- Only uses basic shapes (boxes)  
- Works on any Gazebo Harmonic installation

---

# 📁 Project Structure

```
Team_Vision/
│
├── humanoid_32dof_walk.sdf      ← main simulation file
├── icub_world.sdf              ← optional world
│
└── icub-models/         ← The iCub model is used for static 32 DOF in test_hum.sdf file 
```

---

# ▶️ How to Run the Simulation

### **1. Install Gazebo Harmonic**  
Follow: https://gazebosim.org/docs/harmonic/install_ubuntu/

### **2. Clone the repository**

```bash
git clone https://github.com/madhuri4696/Team_Vision.git
cd Team_Vision/Walking_32_DOF
```

### **3. Run the humanoid simulation**

```bash
gz sim humanoid_32dof_walk.sdf
```

---

# 🧠 How It Works

- Links = Box primitives  
- Joints = Revolute joints with limits/damping/effort  
- Plugins = Joint velocity controllers  

Gravity disabled individually → avoids instability  
Effort limits & damping → prevent joint explosions  
Velocity oscillation → simple walking animation

---

# 🎥 Demo Behavior

- Natural arm swing  
- Alternating leg motion  
- Torso & neck motion  
- Oscillating walk pose  

---

# 🛠️ Extending This Project

You can add:

- Forward walking gait (sinusoidal control)  
- Waving  
- Head tracking  
- Collision physics  
- Balance controllers  
- ROS2 integration  

---

# 📚 Requirements

- Ubuntu 24.04 / WSL2  
- Gazebo Harmonic  
- GPU recommended  

---

# 🤝 Author

Prepared for **Hackathon 2025 – Team Vision**  
Team:


Tech assistance: ChatGPT

---
