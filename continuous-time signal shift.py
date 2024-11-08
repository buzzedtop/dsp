#Created by Generative AI
import numpy as np
import matplotlib.pyplot as plt

def shift_signal(x, t, shift):
    """Shifts a continuous-time signal x(t) by a given amount 'shift'."""
    return x(t - shift)

def signal(t):
    """Example signal: a sine wave."""
    return np.sin(2 * np.pi * t)

# Create a time vector
t = np.linspace(0, 2, 1000)

# Create the original signal
x = signal(t)

# Shift the signal by 0.5 seconds
shifted_x = shift_signal(signal, t, 0.5)

# Plot the original and shifted signals
plt.plot(t, x, label='Original Signal')
plt.plot(t, shifted_x, label='Shifted Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.show()
