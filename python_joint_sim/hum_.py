from vpython import *

# ---------------------------
# Motor Class
# ---------------------------
class DCMotor:
    def __init__(self, name, max_angle=180):
        self.name = name
        self.current_angle = 0
        self.max_angle = max_angle
        self.failsafe = False

    def move_to(self, target_angle, speed_deg_per_sec):
        if self.failsafe:
            return
        target_angle = max(min(target_angle, self.max_angle), -self.max_angle)
        step = 1 if target_angle > self.current_angle else -1
        while self.current_angle != target_angle:
            self.current_angle += step
            rate(speed_deg_per_sec*20)
            yield self.current_angle

    def activate_failsafe(self):
        self.failsafe = True
        print(f"[{self.name}] Failsafe activated!")

# ---------------------------
# Humanoid Robot Class
# ---------------------------
class HumanoidRobot:
    def __init__(self):
        # Body parts
        self.torso = box(pos=vector(0,1,0), length=0.4, height=0.6, width=0.2, color=color.blue)
        self.left_arm = box(pos=vector(-0.35,1.2,0), length=0.1, height=0.5, width=0.1, color=color.red)
        self.right_arm = box(pos=vector(0.35,1.2,0), length=0.1, height=0.5, width=0.1, color=color.red)
        self.left_leg = box(pos=vector(-0.15,0.2,0), length=0.1, height=0.6, width=0.1, color=color.green)
        self.right_leg = box(pos=vector(0.15,0.2,0), length=0.1, height=0.6, width=0.1, color=color.green)
        self.head = sphere(pos=vector(0,1.7,0), radius=0.15, color=color.orange)

        # Motors
        self.motors = {
            "left_arm": DCMotor("Left Arm"),
            "right_arm": DCMotor("Right Arm"),
            "left_leg": DCMotor("Left Leg"),
            "right_leg": DCMotor("Right Leg"),
            "head": DCMotor("Head", max_angle=180)
        }

    def rotate_part(self, part, delta_deg, axis=vector(1,0,0)):
        part.rotate(angle=radians(delta_deg), axis=axis, origin=part.pos)

    def walk(self, steps, speed):
        # Head movement: full range -180 to +180
        head_direction = 1  # 1 = rotate right, -1 = rotate left
        head_angle = 0

        for _ in range(steps):
            # Step 1: Left leg forward, right leg backward, arms opposite
            for angle in self.motors["left_leg"].move_to(30, speed):
                self.rotate_part(self.left_leg, 1)
                self.rotate_part(self.right_leg, -1)
                self.rotate_part(self.left_arm, -0.5)
                self.rotate_part(self.right_arm, 0.5)
                # Rotate head smoothly
                head_angle += head_direction
                if head_angle >= 180 or head_angle <= -180:
                    head_direction *= -1
                self.head.rotate(angle=radians(head_direction), axis=vector(0,1,0), origin=self.head.pos)

            # Step 2: Switch legs
            for angle in self.motors["left_leg"].move_to(-30, speed):
                self.rotate_part(self.left_leg, -1)
                self.rotate_part(self.right_leg, 1)
                self.rotate_part(self.left_arm, 0.5)
                self.rotate_part(self.right_arm, -0.5)
                # Rotate head smoothly
                head_angle += head_direction
                if head_angle >= 180 or head_angle <= -180:
                    head_direction *= -1
                self.head.rotate(angle=radians(head_direction), axis=vector(0,1,0), origin=self.head.pos)

    def emergency_stop(self):
        print("Emergency stop! Activating failsafe.")
        for motor in self.motors.values():
            motor.activate_failsafe()

# ---------------------------
# Run Simulation
# ---------------------------
scene.background = color.white
scene.title = "Humanoid Walking Simulation with Head ±180°"

robot = HumanoidRobot()

# Animate walking 4 steps with head full rotation
robot.walk(4, speed=10)

# Trigger emergency stop
robot.emergency_stop()
