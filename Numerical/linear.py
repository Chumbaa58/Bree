import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Generate some linearly related data
np.random.seed(0)
x = np.arange(0, 10, 0.5)
y = 2 * x + 1 + np.random.normal(size=len(x))

# Reshape x to be a column vector
x = x[:, np.newaxis]

# Perform linear regression
model = LinearRegression()
model.fit(x, y)

# Predict y from the model
y_pred = model.predict(x)

# Plotting the results
plt.figure(figsize=(8, 6))
plt.scatter(x, y, label='Data')
plt.plot(x, y_pred, color='red', label='Linear Regression')
plt.title('Linear Regression Example')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

print(f'Slope: {model.coef_[0]}, Intercept: {model.intercept_}')