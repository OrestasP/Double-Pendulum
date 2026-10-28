from typing import Final

# Constants
GRAVITATIONAL_ACCELERATION: Final[float] = 9.81
# nsteps = 150000
h = 0.0001
nsteps = int(float(input("How many seconds would you like to simulate?: ")) / h)