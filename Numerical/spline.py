import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Generate some data points
x = np.arange(0, 2*np.pi+np.pi/4, 2*np.pi/8)
y = np.sin(x)

# Perform cubic spline interpolation
cs = CubicSpline(x, y)

# Plotting the results
x_interp = np.linspace(0, 2*np.pi, 100)
plt.figure(figsize=(8, 6))
plt.plot(x_interp, np.sin(x_interp), label='True Function')
plt.plot(x_interp, cs(x_interp), linestyle='--', label='Cubic Spline Interpolation')
plt.scatter(x, y, color='red', label='Data Points')
plt.title('Cubic Spline Interpolation Example')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()