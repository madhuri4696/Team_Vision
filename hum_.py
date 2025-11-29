from vpython import box, cylinder, vector, rate, scene
import math

# -------------------------------
# 1. Create humanoid parts
# -------------------------------
# Torso
torso = box(pos=vector(0,0,1), size=vector(0.3,0.2,0.5), color=vector(0.7,0.7,0.7))

# Head
head = box(pos=vector(0,0,1.55), size=vector(0.2,0.2,0.2), color=vector(1,0.8,0.6))

# Arms (upper + lower)
left_arm_upper = cylinder(pos=vector(-0.2,0,1.4), axis=vector(0,-0.3,0), radius=0.05, color=vector(0.8,0.5,0.5))
right_arm_upper = cylinder(pos=vector(0.2,0,1.4), axis=vector(0,0.3,0), radius=0.05, color=vector(0.8,0.5,0.5))

# Legs (upper + lower simplified as single segment)
left_leg = cylinder(pos=vector(-0.1,0,0.75), axis=vector(0,0,-0.5), radius=0.06, color=vector(0.3,0.3,0.8))
right_leg = cylinder(pos=vector(0.1,0,0.75), axis=vector(0,0,-0.5), radius=0.06, color=vector(0.3,0.3,0.8))

# -------------------------------
# 2. Stage 5: Modular movement functions
# -------------------------------
def move_joint(current_angle, target_angle, max_delta):
    """
    Moves a joint towards target angle, limited by max_delta per timestep
    """
    delta = target_angle - current_angle
    if abs(delta) > max_delta:
        delta = math.copysign(max_delta, delta)
    return current_angle + delta

# -------------------------------
# 3. Simulation loop
# -------------------------------
t = 0
dt = 0.02  # seconds per frame
left_arm_angle = 0
right_arm_angle = 0
head_angle = 0
left_leg_angle = 0
right_leg_angle = 0

while True:
    rate(50)  # 50 FPS
    t += dt

    # Target positions (sinusoidal)
    left_arm_target = 0.7 * math.sin(2*math.pi*0.5*t)
    right_arm_target = -0.7 * math.sin(2*math.pi*0.5*t)
    head_target = 0.5 * math.sin(2*math.pi*0.2*t)
    left_leg_target = 0.4 * math.sin(2*math.pi*0.5*t)
    right_leg_target = -0.4 * math.sin(2*math.pi*0.5*t)

    # Stage 5: move joints safely
    left_arm_angle = move_joint(left_arm_angle, left_arm_target, 0.03)
    right_arm_angle = move_joint(right_arm_angle, right_arm_target, 0.03)
    head_angle = move_joint(head_angle, head_target, 0.02)
    left_leg_angle = move_joint(left_leg_angle, left_leg_target, 0.03)
    right_leg_angle = move_joint(right_leg_angle, right_leg_target, 0.03)

    # -------------------------------
    # Update visualization
    # -------------------------------
    left_arm_upper.axis = vector(0, -0.3*math.cos(left_arm_angle), 0.3*math.sin(left_arm_angle))
    right_arm_upper.axis = vector(0, 0.3*math.cos(right_arm_angle), 0.3*math.sin(right_arm_angle))

    head.pos = vector(0, 0, 1.55 + 0.05*math.sin(head_angle))

    left_leg.axis = vector(0, 0, -0.5*math.cos(left_leg_angle))
    right_leg.axis = vector(0, 0, -0.5*math.cos(right_leg_angle))
