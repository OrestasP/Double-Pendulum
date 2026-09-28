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
theta1 = 0.0
omega1 = 10.0
theta2 = 0.0
omega2 = 10.0


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

# State vector
y1 = [theta1, omega1, theta2, omega2]
y_mid2 = [0.0] * len(y1)
y_mid3 = [0.0] * len(y1)
y_mid4 = [0.0] * len(y1)


nsteps = 1000000
h = 0.00001

for i in range(nsteps):
    
    # RK4 stage 1: k1 = F(y_n)
    k1 = [y1[1], angular_acceleration1(y1[0], y1[2], y1[1], y1[3]), y1[3], angular_acceleration2(y1[0], y1[2], y1[1], y1[3])]
    for j in range(len(y1)):
        y_mid2[j] = y1[j] + (h / 2) * k1[j]
    
    # RK4 stage 2: k2 = F(y_n + h*k1/2)
    k2 = [y_mid2[1], angular_acceleration1(y_mid2[0], y_mid2[2], y_mid2[1], y_mid2[3]), y_mid2[3], angular_acceleration2(y_mid2[0], y_mid2[2], y_mid2[1], y_mid2[3])]

    # RK4 stage 3: k3 = F(y_n + h*k2/2)
    for j in range(len(y1)):
        y_mid3[j] = y1[j] + (h / 2) * k2[j]
    k3 = [y_mid3[1], angular_acceleration1(y_mid3[0], y_mid3[2], y_mid3[1], y_mid3[3]), y_mid3[3], angular_acceleration2(y_mid3[0], y_mid3[2], y_mid3[1], y_mid3[3])]

    # RK4 stage 4: k4 = F(y_n + h*k3)
    for j in range(len(y1)):
        y_mid4[j] = y1[j] + h * k3[j]
    k4 = [y_mid4[1], angular_acceleration1(y_mid4[0], y_mid4[2], y_mid4[1], y_mid4[3]), y_mid4[3], angular_acceleration2(y_mid4[0], y_mid4[2], y_mid4[1], y_mid4[3])]

    # Advance state: y_(n+1) = y_n + h/6 * (k1 + 2k2 + 2k3 + k4)
    for j in range(len(y1)):
        y1[j] = y1[j] + (h / 6) * (k1[j] + 2 * k2[j] + 2 * k3[j] + k4[j])
    
    # Shows the what time is being calculated
    if i % 1000 == 0:
        current_time = i * h
        print(f"Calculating t = {current_time:.6f} s")


print(f"Angle1 = {y1[0]}\nAngular Velocity 1 = {y1[1]}\nAngle2 = {y1[2]}\nAngular Velocity 2 = {y1[3]}")



