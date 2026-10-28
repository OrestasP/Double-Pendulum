import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

from parameters import h, nsteps
from pendulums import pendulum1, pendulum2
from rk4_solver import rk4_solve

def main():
    # Solve equations of motion
    (xresult1, 
     yresult1, 
     xresult2, 
     yresult2, 
     total_energy_list, 
     kinetic_energy_list, 
     potential_energy_list, 
     relative_energy_error) = rk4_solve(pendulum1.angle, pendulum1.angular_velocity, pendulum2.angle, pendulum2.angular_velocity)
   
    # Plotting / animating the double pendulum
    fig = plt.figure()

    limit = pendulum1.length + pendulum2.length
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
        axis.set_title(
        'Time {:.2f} s'.format(index * h), fontsize=20)
        line.set_data(x, y)

        return line,

    anim = animation.FuncAnimation(fig, animate, init_func = init, frames = nsteps // skip, interval = 1000 / fps , blit = False)
    # To save the animation as a video uncomment below
    #anim.save('ThePendulum1.mp4', writer = 'ffmpeg', fps = 60)
    plt.show()
    
    # Plotting the total, kinetic, and potential energy over time
    plt.figure()
    
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
    
    # Calculate the maximum absolute relative energy error
    max_error = np.max(np.abs(relative_energy_error))
    print(f"Maximum relative energy error: {max_error:.6e}")

    # Report the range of total energy throughout the simulation
    print(f"Initial energy: {total_energy_list[0]:.8e} J")
    print(f"Minimum energy: {np.min(total_energy_list):.8e} J")
    print(f"Maximum energy: {np.max(total_energy_list):.8e} J")



if __name__ == "__main__":
    main()