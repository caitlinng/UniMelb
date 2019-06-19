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

a_values = np.linspace(0,10,5)

fig1, ax1 = plt.subplots()
sltns_x = []
sltns_y = []

for i in range(5):
    a = a_values.item(i)
    print a
    def expmodel(t, x): 
        dxdt = a*x
        return dxdt
    
    sol = solve_ivp(expmodel, (timepoints[0], timepoints[-1]), [a0])
    sltns_x.append(sol.t)
    sltns_y.append(sol.y[0])

print sltns_y

ax1.plot(sltns_x[0], sltns_y[0], 'b', sltns_x[1], sltns_y[1], 'g', sltns_x[2], sltns_y[2], 'r')

# Formatting
ax1.set_title("Exponential Growth")
ax1.set_xlabel("Time")
ax1.set_ylabel("Value")

plt.show()
