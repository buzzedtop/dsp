#Created by Generative AI
import numpy as np
from scipy.interpolate import interp1d

def interpolate_signal(x, y, new_x, kind='linear'):
    """Interpolates a signal given the original x and y values and the new x values.

    Args:
        x (array-like): Original x values.
        y (array-like): Original y values.
        new_x (array-like): New x values to interpolate at.
        kind (str, optional): Interpolation method. Defaults to 'linear'.

    Returns:
        array-like: Interpolated y values.
    """

    f = interp1d(x, y, kind=kind)
    return f(new_x)

if __name__ == "__main__":
    # Example usage
    x = np.arange(0, 10)
    y = np.sin(x)

    new_x = np.arange(0, 9.5, 0.5)
    new_y = interpolate_signal(x, y, new_x, kind='cubic')

    print("Original x:", x)
    print("Original y:", y)
    print("New x:", new_x)
    print("Interpolated y:", new_y)
