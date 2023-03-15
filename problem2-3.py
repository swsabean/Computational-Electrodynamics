"""
This module plots the numerical dispersion in the FDTD scheme by calculating
constant attenuation and numerical phase velocity. It is a solution to
Problem 2.3 from the text "Computational Electrodynamics: The Finite-Difference
Time-Domain Method, Second Edition" by Allen Taflove and Susan C. Hagness.
"""
import numpy as np
import matplotlib.pyplot as plt

# Define stability factor (Courant number)
S = 0.5

N_transition = 2 * np.pi * S / np.arccos(1 - 2 * S ** 2)

# Define grid sampling density range
N_MIN = 1
N_MAX = 10
N_STEPS = 100

N_range = np.linspace(N_MIN, N_MAX, N_STEPS)
a_range = np.linspace(N_MIN, N_transition, N_STEPS)

phase_velocities = np.zeros(N_STEPS)
attenuation = np.zeros(N_STEPS)

for i, N_lambda in enumerate(N_range):
    if N_lambda < N_transition:
        phase_velocities[i] = 2 / N_lambda
    else:
        phase_velocities[i] = (
            2 * np.pi
            / (N_lambda * np.arccos(1 + 4 * (np.cos(np.pi / N_lambda) - 1)))
        )
        
for i, N_lambda in enumerate(a_range):
    zeta = 1 + (1 / S) ** 2 * (np.cos(2 * np.pi * S / N_lambda) - 1)
    attenuation[i] = -np.log(-zeta - np.sqrt(zeta ** 2 - 1))

plt.rcParams.update({'font.size': 12})
fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.plot(a_range, attenuation, 'b--', linewidth=2)
ax1.set_xlabel('Grid Sampling Density (points per free-space wavelength)', fontsize=14)
ax1.set_ylabel('Constant Attenuation (nepers/grid cell)', color='b', fontsize=14)
ax1.tick_params('y', colors='b')
ax1.set_ylim(0, 6)
ax1.set_xlim(1,10)

ax2 = ax1.twinx()
ax2.plot(N_range, phase_velocities, 'r-', linewidth=2)
ax2.set_ylabel('Numerical Phase Velocity (normalized to $c$)', color='r', fontsize=14)
ax2.tick_params('y', colors='r')
ax2.set_ylim(0.0, 2.0)

plt.title('Numerical Dispersion in FDTD Scheme', fontsize=16)
fig.tight_layout()

plt.savefig('/storage/emulated/0/Download/Problem2_3.png', dpi=300)
plt.show()
