import __main__
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from Energy import potential_energy, kinetic_energy, total_energy
from Equations import angular_acceleration1, angular_acceleration2
from Parameters import mass1, mass2, rod_length1, rod_length2, GRAVITATIONAL_ACCELERATION


# Initial Conditions
theta1 = 0.0
omega1 = 1.0
theta2 = 0.3
omega2 = 1.0
initial_energy = total_energy(theta1, theta2, omega1, omega2)

def main():
    # State vector
    state = [theta1, omega1, theta2, omega2]
    
    # Temporary states used to evaluate the intermediate RK4 stages.
    state_mid2 = [0.0] * len(state)
    state_mid3 = [0.0] * len(state)
    state_mid4 = [0.0] * len(state)
    
    nsteps = 1000000
    h = 0.00001     # Integration time step (s)
    
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
        xresult1[i] = rod_length1 * np.sin(state[0])
        yresult1[i] = -rod_length1 * np.cos(state[0])

        xresult2[i] = xresult1[i] + rod_length2 * np.sin(state[2])
        yresult2[i] = yresult1[i] - rod_length2 * np.cos(state[2])

        total_energy_list.append(total_energy(state[0], state[2], state[1], state[3]))
        kinetic_energy_list.append(kinetic_energy(state[0], state[2], state[1], state[3]))
        potential_energy_list.append(potential_energy(state[0], state[2]))

        relative_energy_error.append((total_energy_list[i] - initial_energy) / abs(initial_energy))

        # Shows the what time is being calculated
        if i % 1000 == 0:
            current_time = i * h
            print(f"Calculating t = {current_time:.2f} s")
        


    # Plotting / animating the double pendulum
    fig = plt.figure()

    limit = rod_length1 + rod_length2
    axis = plt.axes(xlim = (-limit, limit), ylim = (-limit, limit))

    axis.set_aspect('equal')

    line, = axis.plot([], [], 'o-', lw = 3, ms = 10, color = "black")

    fps = 60
    skip = int(1 / (fps * h))

    def init():
        line.set_data([], [])
        return line,


    def animate(frame):
        index = frame * skip

        x = [0, xresult1[index], xresult2[index]]
        y = [0, yresult1[index], yresult2[index]]

        line.set_data(x, y)

        return line,

    anim = animation.FuncAnimation(fig, animate, init_func = init, frames = nsteps // skip, interval = 1000 / fps , blit = True)
    plt.show()
    
    # To save the animation as a video uncomment below
    # anim.save('ThePendulum1.mp4', writer = 'ffmpeg', fps = 60)
    
    # Plotting Energy
    plt.figure
    
    time = np.arange(len(total_energy_list)) * h
    
    plt.plot(time, total_energy_list, label = "Total Energy", color = "green")
    plt.plot(time, kinetic_energy_list, label = "Kinetic Energy", color = "blue")
    plt.plot(time, potential_energy_list, label = "Potential Energy", color = "red")
    
    plt.xlabel("Time (s)")
    plt.ylabel("Energy (J)")
    plt.title("Energy vs Time")
    plt.grid(True)
    plt.legend()
    plt.show()

    # Plotting relative energy error
    plt.figure()
    
    plt.plot(time, relative_energy_error, label = "Relative Energy Error", color = "purple")
    
    plt.xlabel("Time (s)")
    plt.ylabel("Relative Energy Error")
    plt.title("Relative Energy error vs Time")
    plt.grid(True)
    plt.show()

    # Outputs
    print(f"Angle1 = {state[0]}\nAngular Velocity 1 = {state[1]}\nAngle2 = {state[2]}\nAngular Velocity 2 = {state[3]}")
    
    max_error = np.max(np.abs(relative_energy_error))
    print(f"Maximum relative energy error: {max_error:.6e}")

    print(f"Initial energy: {total_energy_list[0]:.8e} J")
    print(f"Minimum energy: {np.min(total_energy_list):.8e} J")
    print(f"Maximum energy: {np.max(total_energy_list):.8e} J")



if __name__ == "__main__":
    main()