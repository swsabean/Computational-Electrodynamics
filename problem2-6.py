"""
Problem 2.6 from "Computational Electrodynamics: The Finite-Difference Time-Domain Method"
by Allen Taflove and Susan C. Hagness.

This script calculates and plots the phase velocity error as a function of grid sampling density
(points per free-space wavelength) for the 2D FDTD method.
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
    phase_velocity = 2 * np.pi / (n_lambda * np.arccos(1 + 2 * (np.cos(np.sqrt(2) * np.pi / n_lambda) - 1)))
    return (1 - phase_velocity) * 100

def main():
    """
    Main function to calculate and plot the phase velocity error as a
     function of grid sampling density.
    """
    # Define grid sampling density range
    n_min = 3
    n_max = 80
    n_steps = 100

    n_range = np.linspace(n_min, n_max, n_steps)
    phase_velocity_errors = np.zeros(n_steps)

    for i, n_lambda in enumerate(n_range):
        phase_velocity_errors[i] = compute_phase_velocity_error(n_lambda)

    # Plot results
    plt.plot(n_range, phase_velocity_errors)
    plt.yscale('log')
    plt.xlabel('Grid Sampling Density (points per free-space wavelength)')
    plt.ylabel('Phase Velocity Error (%)')
    plt.savefig('/storage/emulated/0/Download/Problem2_6.png', dpi=300)
    plt.show()

if __name__ == "__main__":
    main()
