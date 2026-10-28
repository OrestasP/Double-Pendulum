import numpy as np

from energy import (
    kinetic_energy, 
    potential_energy, 
    total_energy, 
    initial_energy)
from parameters import h, nsteps
from pendulums import pendulum1, pendulum2
from equations import angular_acceleration1, angular_acceleration2

def rk4_solve(angle1, angular_velocity1, angle2, angular_velocity2):
    # State vector
    state = [angle1, angular_velocity1, angle2, angular_velocity2]
    
    # Temporary states used to evaluate the intermediate RK4 stages.
    state_mid2 = [0.0] * len(state)
    state_mid3 = [0.0] * len(state)
    state_mid4 = [0.0] * len(state)
    
    xresult1 = [0.0] * nsteps
    yresult1 = [0.0] * nsteps

    xresult2 = [0.0] * nsteps
    yresult2 = [0.0] * nsteps
        
    total_energy_list = []
    kinetic_energy_list = []
    potential_energy_list = []
    relative_energy_error = []
    

    for i in range(nsteps):
        
        # RK4 stage 1: k1 = F(y_n)
        k1 = [state[1], angular_acceleration1(state[0], state[2], state[1], state[3]), state[3], angular_acceleration2(state[0], state[2], state[1], state[3])]
        for j in range(len(state)):
            state_mid2[j] = state[j] + (h / 2) * k1[j]
        
        # RK4 stage 2: k2 = F(y_n + h*k1/2)
        k2 = [state_mid2[1], angular_acceleration1(state_mid2[0], state_mid2[2], state_mid2[1], state_mid2[3]), state_mid2[3], angular_acceleration2(state_mid2[0], state_mid2[2], state_mid2[1], state_mid2[3])]

        # RK4 stage 3: k3 = F(y_n + h*k2/2)
        for j in range(len(state)):
            state_mid3[j] = state[j] + (h / 2) * k2[j]
        k3 = [state_mid3[1], angular_acceleration1(state_mid3[0], state_mid3[2], state_mid3[1], state_mid3[3]), state_mid3[3], angular_acceleration2(state_mid3[0], state_mid3[2], state_mid3[1], state_mid3[3])]

        # RK4 stage 4: k4 = F(y_n + h*k3)
        for j in range(len(state)):
            state_mid4[j] = state[j] + h * k3[j]
        k4 = [state_mid4[1], angular_acceleration1(state_mid4[0], state_mid4[2], state_mid4[1], state_mid4[3]), state_mid4[3], angular_acceleration2(state_mid4[0], state_mid4[2], state_mid4[1], state_mid4[3])]

        # Advance state: y_(n+1) = y_n + h/6 * (k1 + 2k2 + 2k3 + k4)
        for j in range(len(state)):
            state[j] = state[j] + (h / 6) * (k1[j] + 2 * k2[j] + 2 * k3[j] + k4[j])
        
        # Saving the value of each angle at every step, and converting to cartesian coordinates
        xresult1[i] = pendulum1.length * np.sin(state[0])
        yresult1[i] = -pendulum1.length * np.cos(state[0])

        xresult2[i] = xresult1[i] + pendulum2.length * np.sin(state[2])
        yresult2[i] = yresult1[i] - pendulum2.length * np.cos(state[2])

        total_energy_list.append(total_energy(state[0], state[2], state[1], state[3]))
        kinetic_energy_list.append(kinetic_energy(state[0], state[2], state[1], state[3]))
        potential_energy_list.append(potential_energy(state[0], state[2]))

        relative_energy_error.append((total_energy_list[i] - initial_energy) / abs(initial_energy))

        # Shows the what time is being calculated
        if i % 1000 == 0:
            current_time = i * h
            print(f"Calculating t = {current_time:.2f} s")
    return (
        xresult1,
        yresult1,
        xresult2,
        yresult2,
        total_energy_list,
        kinetic_energy_list,
        potential_energy_list,
        relative_energy_error
    )