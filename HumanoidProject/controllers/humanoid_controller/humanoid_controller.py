from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

# ----------- GET MOTORS (correct names from PROTO) -----------------
motor_names = [
    "LShoulder",
    "RShoulder",
    "LElbow",
    "RElbow",
    "LHip",
    "LKnee",
    "RHip",
    "RKnee"
]

motors = {}

for name in motor_names:
    device = robot.getDevice(name)
    if device is None:
        print(f"ERROR: Motor '{name}' not found in Humanoid32!")
    else:
        print(f"Loaded motor: {name}")
        motors[name] = device
        device.setVelocity(1.0)

# ----------- SET TARGET POSITIONS ------------------

# Example arm motion
motors["LShoulder"].setPosition(0.5)
motors["RShoulder"].setPosition(-0.5)

# Example leg motion
motors["LKnee"].setPosition(0.3)
motors["RKnee"].setPosition(-0.3)

# ----------- MAIN LOOP -----------------------------
while robot.step(timestep) != -1:
    pass
