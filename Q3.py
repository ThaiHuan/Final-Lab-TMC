import numpy as np
import matplotlib.pyplot as plt

def f(x, y, dy):
    return -0.5 * dy - 7 * y

def runge_kutta_4th_order(f, x, y, dy, h):
    k1_y = h * dy
    k1_dy = h * f(x, y, dy)
    
    k2_y = h * (dy + 0.5 * k1_dy)
    k2_dy = h * f(x + 0.5 * h, y + 0.5 * k1_y, dy + 0.5 * k1_dy)
    
    k3_y = h * (dy + 0.5 * k2_dy)
    k3_dy = h * f(x + 0.5 * h, y + 0.5 * k2_y, dy + 0.5 * k2_dy)
    
    k4_y = h * (dy + k3_dy)
    k4_dy = h * f(x + h, y + k3_y, dy + k3_dy)
    
    y_next = y + (k1_y + 2 * k2_y + 2 * k3_y + k4_y) / 6
    dy_next = dy + (k1_dy + 2 * k2_dy + 2 * k3_dy + k4_dy) / 6
    
    return y_next, dy_next

# Corrected initial conditions
x_0 = 0
y_0 = 4
dy_0 = 0  # Should be the derivative at the initial point

# Parameters
x_end = 5
h = 0.5

# Lists to store results
x_values = [x_0]
y_values = [y_0]

# Solve using RK4 method
while x_values[-1] < x_end:
    y_next, dy_next = runge_kutta_4th_order(f, x_values[-1], y_values[-1], dy_0, h)
    x_values.append(x_values[-1] + h)
    y_values.append(y_next)

# Plot the results
plt.plot(x_values, y_values, label='Fourth-Order RK Method')
plt.title('Solution using Fourth-Order RK Method')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
