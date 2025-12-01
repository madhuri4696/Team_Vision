from controller import Robot
import math

# -------------------------------
# Create robot and timestep
# -------------------------------
robot = Robot()
timestep = int(robot.getBasicTimeStep())

# -------------------------------
# 1. Get motors
# -------------------------------
# Arms
left_arm_motor = robot.getDevice('LShoulderPitch')
right_arm_motor = robot.getDevice('RShoulderPitch')

# Head
head_motor = robot.getDevice('HeadYaw')

# Legs
left_knee_motor = robot.getDevice('LKneePitch')
right_knee_motor = robot.getDevice('RKneePitch')

# -------------------------------
# 2. Set velocity limits
# -------------------------------
left_arm_motor.setVelocity(0.5)
right_arm_motor.setVelocity(0.5)
head_motor.setVelocity(0.3)
left_knee_motor.setVelocity(0.4)
right_knee_motor.setVelocity(0.4)

# -------------------------------
# 3. Enable sensors (optional)
# -------------------------------
for motor_name in ['LShoulderPitch', 'RShoulderPitch', 'HeadYaw', 'LKneePitch', 'RKneePitch']:
    sensor = robot.getDevice(motor_name + 'S')
    sensor.enable(timestep)

# -------------------------------
# 4. Main motion loop
# -------------------------------
# We'll use sin() to create smooth repetitive motions
t = 0.0
while robot.step(timestep) != -1:
    t += timestep / 1000.0  # convert ms to seconds

    # Arm waving: swing +/- 0.7 rad
    left_arm_motor.setPosition(0.7 * math.sin(2 * math.pi * 0.5 * t))
    right_arm_motor.setPosition(-0.7 * math.sin(2 * math.pi * 0.5 * t))

    # Head rotation: +/- 0.5 rad slowly
    head_motor.setPosition(0.5 * math.sin(2 * math.pi * 0.2 * t))

    # Knee bending: simple stepping motion +/- 0.4 rad
    left_knee_motor.setPosition(0.4 * math.sin(2 * math.pi * 0.5 * t))
    right_knee_motor.setPosition(-0.4 * math.sin(2 * math.pi * 0.5 * t))

    # Optional: print joint positions
    # left_pos = robot.getDevice('LShoulderPitchS').getValue()
    # print(f"Left Arm: {left_pos:.2f}")
