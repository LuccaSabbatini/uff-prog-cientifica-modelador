import json
import numpy as np
import matplotlib.pyplot as plt


def finiteDifferenceCoeficients(h, k):
    a = 2 * ((h / k) ** 2 + 1)
    b = -((h / k) ** 2)
    return [a, -1, -1, b, b]


with open("methods/mdf/input.json", "r") as file:
    data = json.load(file)

n = len(data["coords"])
coords = np.array(data["coords"])
connect = data["connect"]
restrictions = np.array(data["boundary_values"])

# Calculate the finite difference coefficients
# math absolute value of the difference between the x coordinates of the first two points
h = abs(coords[1, 0] - coords[0, 0])
k = 100
coeficients = finiteDifferenceCoeficients(h, k)

# Initialize A, b, and x
A = np.zeros((n, n), dtype=np.float64)
b = np.zeros((n, 1), dtype=np.float64)
x = np.zeros((n, 1), dtype=np.float64)

# Fill A and b
for i in range(n):
    x[i, 0] = coords[i, 0]
    A[i, i] = coeficients[0]
    if i > 0:
        A[i, i - 1] = coeficients[1]
    if i < n - 1:
        A[i, i + 1] = coeficients[2]
    if i > 1:
        A[i, i - 2] = coeficients[3]
    if i < n - 2:
        A[i, i + 2] = coeficients[4]
    b[i, 0] = coords[i, 1]

# Apply the boundary conditions
for i in range(len(restrictions)):
    A[restrictions[i][0], :] = 0
    A[restrictions[i][0], restrictions[i][0]] = 1
    b[restrictions[i][0], 0] = restrictions[i][1]


# Solve the linear system
T_result = np.linalg.solve(A, b)

# Plot the results
plt.plot(x, T_result)
plt.show()
