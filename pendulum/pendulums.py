import numpy as np

class pendulum:
    def __init__(self, mass, angle, angular_velocity, length):
        self.mass = mass
        self.angle = angle
        self.angular_velocity = angular_velocity
        self.length = length

    def __str__(self):
        return (
            f"Mass: {self.mass} kg\n"
            f"Angle: {self.angle} rad\n"
            f"Angular Velocity: {self.angular_velocity} rad/s\n"
            f"Rod Length: {self.length} m"
        )

pendulum1 = pendulum(mass = 1, angle = np.pi * (2/3), angular_velocity = 0, length = 1)
pendulum2 = pendulum(mass = 1 , angle = - np.pi / 18, angular_velocity = 0, length = 1)