import numpy as np
import matplotlib.pyplot as plt

def get_user_function():
    """Gets a mathematical function string from the user."""
    while True:
        try:
            func_str = input("Enter a function of t (e.g., 'sin(t)' or 't**2'): ")
            f = lambda t: eval(func_str)
            f(0)  # Test evaluation
            return f
        except Exception as e:
            print(f"Invalid function: {e}")

def sample_signal(f, t_start, t_end, num_samples):
    """Samples a continuous-time signal from the given function."""
    t = np.linspace(t_start, t_end, num_samples)
    return t, f(t)

if __name__ == "__main__":
    f = get_user_function()
    t_start = float(input("Enter start time: "))
    t_end = float(input("Enter end time: "))
    num_samples = int(input("Enter number of samples: "))

    t, signal = sample_signal(f, t_start, t_end, num_samples)

    plt.plot(t, signal)
    plt.xlabel("Time")
    plt.ylabel("Signal")
    plt.title("Continuous-Time Signal")
    plt.show()
