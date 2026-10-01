from Parameters import (
    mass1, mass2,
    rod_length1, rod_length2,
    GRAVITATIONAL_ACCELERATION
)
import numpy as np

def Kinetic_Energy(angle1, angle2, angular_velocity1, angular_velocity2):
    kinetic_energy = (
        0.5 * mass1 * rod_length1**2 * angular_velocity1**2
        + 0.5 * mass2 * (
            rod_length1**2 * angular_velocity1**2
            + rod_length2**2 * angular_velocity2**2
            + 2 * rod_length1 * rod_length2
            * angular_velocity1 * angular_velocity2
            * np.cos(angle1 - angle2)
        )
    )
    return kinetic_energy

def Potential_Energy(angle1, angle2):
    potential_energy = (
        -(mass1 + mass2) * GRAVITATIONAL_ACCELERATION
        * rod_length1 * np.cos(angle1)
        - mass2 * GRAVITATIONAL_ACCELERATION
        * rod_length2 * np.cos(angle2)
    )
    return potential_energy

def Total_Energy(angle1, angle2, angular_velocity1, angular_velocity2):
    total_energy = Kinetic_Energy(angle1, angle2, angular_velocity1, angular_velocity2) + Potential_Energy(angle1, angle2)
    return total_energy