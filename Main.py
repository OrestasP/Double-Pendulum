import __main__
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from Energy import Potential_Energy, Kinetic_Energy, Total_Energy
from Parameters import mass1, mass2, rod_length1, rod_length2, GRAVITATIONAL_ACCELERATION


# Initial Conditions
theta1 = 0.0
omega1 = 1.0
theta2 = 0.3
omega2 = 1.0

def main():
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

    angle1 = [0.0] * nsteps
    angle2 = [0.0] * nsteps

    xresult1 = [0.0] * nsteps
    yresult1 = [0.0] * nsteps

    xresult2 = [0.0] * nsteps
    yresult2 = [0.0] * nsteps
    
    Total_Energy_List = []
    Kinetic_Energy_List = []
    Potetial_Energy_List = []

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
        
        # Saving the value of each angle at every step, and converting to cartesian coordinates
        xresult1[i] = rod_length1 * np.sin(y1[0])
        yresult1[i] = -rod_length1 * np.cos(y1[0])

        xresult2[i] = xresult1[i] + rod_length2 * np.sin(y1[2])
        yresult2[i] = yresult1[i] - rod_length2 * np.cos(y1[2])

        Total_Energy_List.append(Total_Energy(y1[0], y1[2], y1[1], y1[3]))
        Kinetic_Energy_List.append(Kinetic_Energy(y1[0], y1[2], y1[1], y1[3]))
        Potetial_Energy_List.append(Potential_Energy(y1[0], y1[2]))



        # Shows the what time is being calculated
        if i % 1000 == 0:
            current_time = i * h
            print(f"Calculating t = {current_time:.2f} s")



    fig = plt.figure()

    limit = rod_length1 + rod_length2
    axis = plt.axes(xlim = (-limit, limit), ylim = (-limit, limit))

    axis.set_aspect('equal')


    line, = axis.plot([], [], lw = 2)

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
    
    # anim.save('ThePendulum1.mp4', writer = 'ffmpeg', fps = 60)
    
    
    fig_energy = plt.figure()
    time = np.arange(len(Total_Energy_List)) * h
    plt.plot(time, Total_Energy_List, label = "Total Energy", color = "green")
    plt.plot(time, Kinetic_Energy_List, label = "Kinetic Energy", color = "blue")
    plt.plot(time, Potetial_Energy_List, label = "Potential Energy", color = "red")
    plt.xlabel("Time (s)")
    plt.ylabel("Energy (J)")
    plt.title("Energy vs Time")
    plt.grid(True)
    plt.legend()
    plt.show()

    print(f"Angle1 = {y1[0]}\nAngular Velocity 1 = {y1[1]}\nAngle2 = {y1[2]}\nAngular Velocity 2 = {y1[3]}")

if __name__ == "__main__":
    main()