# File: humanoid_controller.py
from controller import Robot

# Create robot instance
robot = Robot()

# Get simulation timestep
timestep = int(robot.getBasicTimeStep())

# -------------------------------
# 1. Get motors (names depend on robot)
# -------------------------------
# Arms
left_arm_motor = robot.getDevice('LShoulderPitch')
right_arm_motor = robot.getDevice('RShoulderPitch')

# Head
head_motor = robot.getDevice('HeadYaw')

# Leg
left_knee_motor = robot.getDevice('LKneePitch')

# -------------------------------
# 2. Set velocity limits (rad/s)
# -------------------------------
left_arm_motor.setVelocity(0.3)      # slower arm movement
right_arm_motor.setVelocity(0.3)
head_motor.setVelocity(0.2)          # slow head turn
left_knee_motor.setVelocity(0.5)     # leg movement

# -------------------------------
# 3. Set target positions (radians)
# -------------------------------
# Arm positions
left_arm_motor.setPosition(1.0)      # raise left arm
right_arm_motor.setPosition(-1.0)    # raise right arm oppositely

# Head position
head_motor.setPosition(0.5)          # turn head to right

# Leg position
left_knee_motor.setPosition(0.7)     # bend left knee

# -------------------------------
# 4. Enable joint sensors (optional, for monitoring)
# -------------------------------
left_arm_sensor = robot.getDevice('LShoulderPitchS')
right_arm_sensor = robot.getDevice('RShoulderPitchS')
head_sensor = robot.getDevice('HeadYawS')
left_knee_sensor = robot.getDevice('LKneePitchS')

left_arm_sensor.enable(timestep)
right_arm_sensor.enable(timestep)
head_sensor.enable(timestep)
left_knee_sensor.enable(timestep)

# -------------------------------
# 5. Main control loop
# -------------------------------
while robot.step(timestep) != -1:
    # Optional: read current positions for debugging
    left_pos = left_arm_sensor.getValue()
    right_pos = right_arm_sensor.getValue()
    head_pos = head_sensor.getValue()
    knee_pos = left_knee_sensor.getValue()

    # Print positions every loop (optional)
    print(f"Left Arm: {left_pos:.2f}, Right Arm: {right_pos:.2f}, Head: {head_pos:.2f}, Knee: {knee_pos:.2f}")

    # Safety check: stop movement if angles exceed limits
    if abs(left_pos) > 2.0 or abs(right_pos) > 2.0 or abs(head_pos) > 1.5 or abs(knee_pos) > 1.5:
        left_arm_motor.setVelocity(0.0)
        right_arm_motor.setVelocity(0.0)
        head_motor.setVelocity(0.0)
        left_knee_motor.setVelocity(0.0)
        print("Joint limit exceeded! Motors stopped.")
        break
