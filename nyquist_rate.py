# Created by Generative AI
def calculate_nyquist_rate(max_frequency):
    """Calculates the Nyquist rate for a given maximum frequency.

    Args:
        max_frequency (float): The maximum frequency component in the signal (in Hz).

    Returns:
        float: The Nyquist rate (in Hz).
    """

    return 2 * max_frequency

if __name__ == "__main__":
    max_freq = float(input("Enter the maximum frequency of the signal (in Hz): "))
    nyquist_rate = calculate_nyquist_rate(max_freq)
    print(f"The Nyquist rate is: {nyquist_rate} Hz")
