import numpy as np

def discretize_signal(continuous_signal, sampling_rate):
    """
    Discretizes a continuous-time signal using a given sampling rate.

    Args:
        continuous_signal (function): A function that represents the continuous-time signal.
        sampling_rate (float): The sampling rate in Hz.

    Returns:
        numpy.ndarray: The discretized signal.
    """

    # Generate time values for the continuous signal
    t_continuous = np.arange(0, 10, 1/sampling_rate)

    # Evaluate the continuous signal at the generated time values
    signal_values = continuous_signal(t_continuous)

    return signal_values

if __name__ == "__main__":
    # Example continuous-time signal (sine wave)
    def continuous_signal(t):
        return np.sin(2 * np.pi * 2 * t)

    # Sampling rate
    sampling_rate = 100

    # Discretize the signal
    discrete_signal = discretize_signal(continuous_signal, sampling_rate)

    # Print the first few values of the discrete signal
    print(discrete_signal[:10])
