import numpy as np

from parameters import GRAVITATIONAL_ACCELERATION
from pendulums import pendulum1, pendulum2

def angular_acceleration1(angle1, angle2, angular_velocity1, angular_velocity2):
    return (
    (
        -GRAVITATIONAL_ACCELERATION * (2 * pendulum1.mass + pendulum2.mass) * np.sin(angle1)
        - pendulum2.mass * GRAVITATIONAL_ACCELERATION * np.sin(angle1 - 2 * angle2)
        - 2 * pendulum2.mass * np.sin(angle1 - angle2)
        * (
            pendulum2.length * np.pow(angular_velocity2, 2)
            + pendulum1.length * np.pow(angular_velocity1, 2)
            * np.cos(angle1 - angle2)
        )
    )
    /
    (
        pendulum1.length
        * (
            2 * pendulum1.mass
            + pendulum2.mass
            - pendulum2.mass * np.cos(2 * (angle1 - angle2))
        )
    )
    )

def angular_acceleration2(angle1, angle2, angular_velocity1, angular_velocity2):
    return (
    (
        2 * np.sin(angle1 - angle2)
        * (
            pendulum1.length * np.pow(angular_velocity1, 2) * (pendulum1.mass + pendulum2.mass)
            + GRAVITATIONAL_ACCELERATION * (pendulum1.mass + pendulum2.mass) * np.cos(angle1)
            + pendulum2.length * pendulum2.mass * np.pow(angular_velocity2, 2)
            * np.cos(angle1 - angle2)
        )
    )
    /
    (
        pendulum2.length
        * (
            2 * pendulum1.mass
            + pendulum2.mass
            - pendulum2.mass * np.cos(2 * (angle1 - angle2))
        )
    )
    )