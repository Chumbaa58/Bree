import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)

def differentiate(f, x, h=1e-6):
    return (f(x + h) - f(x)) / h

x = np.linspace(0, 2*np.pi, 100)
df_dx = differentiate(np.sin, x)

plt.figure(figsize=(8, 6))
plt.plot(x, np.cos(x), label='Analytical Derivative') 
plt.plot(x, df_dx, label='Numerical Derivative', linestyle='--')
plt.title('Differentiation of sin(x)')
plt.xlabel('x')
plt.ylabel('f\'(x)')
plt.legend()
plt.grid(True)
plt.show()