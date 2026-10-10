from Parameters import mass1, mass2, rod_length1, rod_length2, GRAVITATIONAL_ACCELERATION
import numpy as np

def kinetic_energy(angle1, angle2, angular_velocity1, angular_velocity2):
    return (
        0.5 * mass1 * rod_length1**2 * angular_velocity1**2
        + 0.5 * mass2 * (
            rod_length1**2 * angular_velocity1**2
            + rod_length2**2 * angular_velocity2**2
            + 2 * rod_length1 * rod_length2
            * angular_velocity1 * angular_velocity2
            * np.cos(angle1 - angle2)
        )
    )

def potential_energy(angle1, angle2):
    return (
        -(mass1 + mass2) * GRAVITATIONAL_ACCELERATION
        * rod_length1 * np.cos(angle1)
        - mass2 * GRAVITATIONAL_ACCELERATION
        * rod_length2 * np.cos(angle2)
    )

def total_energy(angle1, angle2, angular_velocity1, angular_velocity2):
    return kinetic_energy(angle1, angle2, angular_velocity1, angular_velocity2) + potential_energy(angle1, angle2)