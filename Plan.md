# Double Pendulum Project Plan

## Project Goal

Build a polished double pendulum simulation that demonstrates:

- Classical mechanics
- Lagrangian mechanics
- Numerical integration
- Scientific computing
- Software engineering
- Validation and testing
- Data visualization
- Chaotic dynamics
- Technical communication


The repository should contain:

- A correct double pendulum model
- A custom numerical integrator
- Real-time animation
- Energy-conservation analysis
- A chaos experiment
- Automated tests
- Numerical-method comparisons
- A polished README
- A short scientific write-up
- Screenshots or GIFs
- A portfolio-ready presentation

# Phase 1 — Mathematical Model

## Goal

Derive the equations of motion correctly before building the rest of the software.

## Tasks

- [x] Define the generalized coordinates
- [x] Construct the Lagrangian
- [x] Apply the Euler-Lagrange equations
- [x] Solve explicitly Theta_double_dot for both coordinates
- [x] Convert the equations into four first-order ODEs


# Phase 2 — Core Simulation

## Goal

Implement a minimal working numerical simulation.

## Tasks

- [x] Create a function for the equations of motion

- [x] Implement RK4 manually
- [x] Create a simulation loop
- [ ] Store the full state history
- [ ] Plot Theta1
- [ ] Plot Theta2
- [ ] Plot angular velocities

# Phase 3 — Validation

## Goal

Verify that the simulation is numerically and physically credible.

## Energy Conservation

- [ ] Create kinetic, potential, total energy functions
- [ ] Make sure the total energy remains approximately constant.
- [ ] Plot a relative energy error.

## Timestep Experiment

- [ ] Compare multiple timesteps
- [ ]Measure how the energy error changes.

## Physical Sanity Checks

Test cases such as:

- [ ] Small initial angles
- [ ] Equal masses
- [ ] Equal rod lengths
- [ ] Zero initial angular velocities
- [ ] One mass much larger than the other
- [ ] Stable downward equilibrium

# Phase 4 — Visualization

## Goal

Create a clear real-time animation.

## Tasks

- [ ] Convert angular coordinates to Cartesian coordinates
- [ ] Draw both rods
- [ ] Draw both masses
- [ ] Animate using Matplotlib
- [ ] Display simulation time
- [ ] Add a trace for the second mass
- [ ] Add pause/reset controls

## Optional Additions

- Current total energy
- Playback speed
- Trail length control
- Show/hide trajectory

