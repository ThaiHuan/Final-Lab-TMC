import numpy as np

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
def newton_interpolation(X, y, x):
    n = len(X)
    result = y[0]

    for i in range(1, n):
        term = 1
        for j in range(i):
            term *= (x - X[j])
        result += term * divided_diff_table[0, i]

    return result

# Calculate divided differences
divided_diff_table = divided_differences(X_values, y_values)

# Calculate y at x = 2.5
x_interpolate = 2.5
y_interpolated = newton_interpolation(X_values, y_values, x_interpolate)

# Print the result
print(f"A) The interpolated value at x = {x_interpolate} is approximately {y_interpolated:.4f}")

import numpy as np

# Given data
X_values = np.array([2, 2.1, 2.2, 2.7, 3, 3.4])
y_values = np.array([6, 7.752, 30.256, 36.576, 66, 123.168])

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

# Calculate y at x = 2.5 using cubic spline interpolation
y_cubic_spline = cubic_spline_interpolation(X_values, y_values, 2.5)

# Print the result for cubic spline interpolation
print(f"B) The interpolated value at x = 2.5 using cubic spline interpolation is approximately {y_cubic_spline:.4f}")

# Reuse Newton interpolation function from previous solution
y_newton = newton_interpolation(X_values, y_values, 2.5)

#Comparison
print(f"The difference between cubic spline and Newton interpolations at x = 2.5 is {abs(y_cubic_spline - y_newton):.4f}")