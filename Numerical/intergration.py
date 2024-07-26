import scipy.integrate as spi

# Define a function to integrate
def f(x):
    return x**2

# Perform numerical integration
result, error = spi.quad(f, 0, 1)

print(f'Integral of x^2 from 0 to 1: {result:.6f}')