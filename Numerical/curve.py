import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Generate some data points
np.random.seed(0)
x_data = np.linspace(0, 5, 50)
y_data = 2.5 * np.sin(1.5 * x_data) + np.random.normal(size=50)

# Define the function to fit
def func(x, a, b):
    return a * np.sin(b * x)

# Perform curve fitting
params, params_covariance = curve_fit(func, x_data, y_data, p0=[2, 1.5])

# Plotting the results
plt.figure(figsize=(8, 6))
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_data, func(x_data, *params), color='red', label='Fitted function')
plt.title('Curve Fitting Example')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

print(f'Fitted parameters: a = {params[0]}, b = {params[1]}')