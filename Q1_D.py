import numpy as np
import matplotlib.pyplot as plt

# Given data
X_values = np.array([2, 2.1, 2.2, 2.7, 3, 3.4])
y_values = np.array([6, 7.752, 7.256, 36.576, 66, 123.168])

# Function to calculate divided differences
def divided_differences(X, y):
    n = len(X)
    table = np.zeros((n, n))
    table[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            table[i, j] = (table[i + 1, j - 1] - table[i, j - 1]) / (X[i + j] - X[i])

    return table

# Newton interpolation function
def newton_interpolation(X, y, x, divided_diff_table):
    n = len(X)
    result = y[0]

    for i in range(1, n):
        term = 1
        for j in range(i):
            term *= (x - X[j])
        result += term * divided_diff_table[0, i]

    return result

# cubic spline interpolating polynomial function
def cubic_spline_interpolation(X, y, x):
    result = 0

    for i in range(len(X)):
        term = y[i]
        for j in range(len(X)):
            if i != j:
                term *= (x - X[j]) / (X[i] - X[j])
        result += term

    return result

# Calculate divided differences
divided_diff_table = divided_differences(X_values, y_values)

# Calculate y at various points for plotting
x_values_plot = np.linspace(min(X_values), max(X_values), 1000)
y_newton_plot = [newton_interpolation(X_values, y_values, x, divided_diff_table) for x in x_values_plot]
y_cubic_spline_plot = [cubic_spline_interpolation(X_values, y_values, x) for x in x_values_plot]

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(X_values, y_values, 'o', label='Given Data')
plt.plot(x_values_plot, y_newton_plot, label='Newton Interpolation')
plt.plot(x_values_plot, y_cubic_spline_plot, label='cubic spline Interpolation')
plt.title('Comparison of Newton and cubic spline Interpolations')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
