import numpy as np
import matplotlib.pyplot as plt

def quantize(signal, levels):
    """Quantizes a continuous-time signal to a given number of levels."""

    # Find the minimum and maximum values of the signal
    min_val = np.min(signal)
    max_val = np.max(signal)

    # Calculate the quantization step size
    step_size = (max_val - min_val) / levels

    # Quantize the signal
    quantized_signal = np.round((signal - min_val) / step_size) * step_size + min_val

    return quantized_signal

# Generate a sample continuous-time signal
t = np.linspace(0, 1, 1000)
signal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 10 * t)

# Quantize the signal to different levels
quantized_signal_2 = quantize(signal, 2)
quantized_signal_4 = quantize(signal, 4)
quantized_signal_8 = quantize(signal, 8)

# Plot the original and quantized signals
plt.figure(figsize=(10, 6))
plt.plot(t, signal, label="Original Signal")
plt.plot(t, quantized_signal_2, label="2 Levels")
plt.plot(t, quantized_signal_4, label="4 Levels")
plt.plot(t, quantized_signal_8, label="8 Levels")
plt.title("Signal Quantization")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.show()
