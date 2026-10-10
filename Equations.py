from Parameters import mass1, mass2, rod_length1, rod_length2, GRAVITATIONAL_ACCELERATION
import numpy as np

def angular_acceleration1(angle1, angle2, angular_velocity1, angular_velocity2):
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

def angular_acceleration2(angle1, angle2, angular_velocity1, angular_velocity2):
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