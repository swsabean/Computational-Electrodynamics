"""
Problem 2.5 from "Computational Electrodynamics: The Finite-Difference Time-Domain Method"
by Allen Taflove and Susan C. Hagness.

This script calculates and plots the phase velocity error as a function of grid sampling density
(points per free-space wavelength) for the 1D FDTD method.
"""

import numpy as np
import matplotlib.pyplot as plt

def compute_phase_velocity_error(n_lambda):
    """
    Compute the phase velocity error for a given grid sampling density.

    Args:
        n_lambda (float): Grid sampling density (points per free-space wavelength)

    Returns:
        float: Phase velocity error (%)
    """
    phase_velocity = 2 * np.pi / (n_lambda * np.arccos(1 + 4 * (np.cos(np.pi / n_lambda) - 1)))
    return (1 - phase_velocity) * 100

def main():
    """
    Main function to calculate and plot the phase velocity error as a
    function of grid sampling density.
    """
    # Define grid sampling density range
    N_MIN = 3
    N_MAX = 80
    N_STEPS = 100

    N_range = np.linspace(N_MIN, N_MAX, N_STEPS)
    phase_velocity_errors = np.zeros(N_STEPS)

    for i, N_lambda in enumerate(N_range):
        phase_velocity_errors[i] = compute_phase_velocity_error(N_lambda)

    # Plot results
    plt.plot(N_range, phase_velocity_errors)
    plt.yscale('log')
    plt.xlabel('Grid Sampling Density (points per free-space wavelength)')
    plt.ylabel('Phase Velocity Error (%)')
    plt.savefig('/storage/emulated/0/Download/Problem2_5.png', dpi=300)
    plt.show()

if __name__ == "__main__":
    main()
