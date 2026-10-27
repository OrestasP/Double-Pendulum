import numpy as np

from parameters import GRAVITATIONAL_ACCELERATION
from pendulums import pendulum1, pendulum2

def kinetic_energy(angle1, angle2, angular_velocity1, angular_velocity2):
    return (
        0.5 * pendulum1.mass * pendulum1.length**2 * angular_velocity1**2
        + 0.5 * pendulum2.mass * (
            pendulum1.length**2 * angular_velocity1**2
            + pendulum2.length**2 * angular_velocity2**2
            + 2 * pendulum1.length * pendulum2.length
            * angular_velocity1 * angular_velocity2
            * np.cos(angle1 - angle2)
        )
    )

def potential_energy(angle1, angle2):
    return (
        -(pendulum1.mass + pendulum2.mass) * GRAVITATIONAL_ACCELERATION
        * pendulum1.length * np.cos(angle1)
        - pendulum2.mass * GRAVITATIONAL_ACCELERATION
        * pendulum2.length * np.cos(angle2)
    )

def total_energy(angle1, angle2, angular_velocity1, angular_velocity2):
    return kinetic_energy(angle1, angle2, angular_velocity1, angular_velocity2) + potential_energy(angle1, angle2)

initial_energy = total_energy(pendulum1.angle, pendulum2.angle, pendulum1.angular_velocity, pendulum2.angular_velocity)
