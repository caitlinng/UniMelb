import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parameters
a = 2
a0 = 1

timepoints = np.linspace(0, 15, 50)

# Differential equations (computational)
def expmodel(t, x): 
    dxdt = a*x
    return dxdt

# Solve differential
sol = solve_ivp(expmodel, (timepoints[0], timepoints[-1]), [a0])

# True solution
def expsltn(t):
    return a0 * np.exp(a*t)

sltn_x = []
sltn_y = []

for i in timepoints:
    y = expsltn(i)
    sltn_x.append(i)
    sltn_y.append(y)

# For each x value, calculate y (ae^(at))

# Plotting
fig1, ax1 = plt.subplots()
ax1.plot(sol.t,sol.y[0])

# On the same graph, plot true solutions
ax1.plot(sltn_x, sltn_y, 'o')

# Formatting
ax1.set_title("Exponential Growth")
ax1.set_xlabel("Time")
ax1.set_ylabel("Value")
ax1.legend(('Computed','Solved'))

plt.show()