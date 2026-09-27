from typing import Final
import numpy as np

# Constants
GRAVITATIONAL_ACCELERATION: Final[float] = 9.81

# Pendulum parameters
mass1 = 2.0
mass2 = 2.0
rod_length1 = 2.0
rod_length2 = 2.0

# Initial Conditions
angle1 = 2.0
angle2 = 2.0
angular_velocity1 = 2.0
angular_velocity2 = 2.0


def angular_acceleration1(mass1, mass2, angle1, angle2, angular_velocity1, angular_velocity2, rod_length1, rod_length2):
    return (
    (
        -GRAVITATIONAL_ACCELERATION * (2 * mass1 + mass2) * np.sin(angle1)
        - mass2 * GRAVITATIONAL_ACCELERATION * np.sin(angle1 - 2 * angle2)
        - 2 * mass2 * np.sin(angle1 - angle2)
        * (
            rod_length2 * np.pow(angular_velocity2, 2)
            + rod_length1 * np.pow(angular_velocity1, 2)
            * np.cos(angle1 - angle2)
        )
    )
    /
    (
        rod_length1
        * (
            2 * mass1
            + mass2
            - mass2 * np.cos(2 * (angle1 - angle2))
        )
    )
    )

def angular_acceleration2(mass1, mass2, angle1, angle2, angular_velocity1, angular_velocity2, rod_length1, rod_length2):
    return (
    (
        2 * np.sin(angle1 - angle2)
        * (
            rod_length1 * np.pow(angular_velocity1, 2) * (mass1 + mass2)
            + GRAVITATIONAL_ACCELERATION * (mass1 + mass2) * np.cos(angle1)
            + rod_length2 * mass2 * np.pow(angular_velocity2, 2)
            * np.cos(angle1 - angle2)
        )
    )
    /
    (
        rod_length2
        * (
            2 * mass1
            + mass2
            - mass2 * np.cos(2 * (angle1 - angle2))
        )
    )
    )
