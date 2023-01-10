###########################################
#        ENVIRONMENT CREATION
###########################################

############################################################################
# Author: Nahuel Canelo
# Email: nahuelcaneloaraya@gmail.com
############################################################################


#######################
#   IMPORT LIBRARY
########################

import math
import numpy as np
import matplotlib.pyplot as plt


################################
# DEFINING WORKING ENVIRONMENT
################################

def system(t, y, g, A, zL, f, d, L, c):
    q1, h2, q2 = y
    if t < 300: # if the time is greater than or equal to 300, set the value of λ to 0.5
        λ = 0
    else:
        λ = 12*10**-5 # otherwise, set the value of λ to 0.1
    q1_dot = (g*A/zL)*(h1 - h2) - (f(q1)/(2*A*d))*q1*abs(q1)
    h2_dot = (c**2/(g*A*zL))*(q1 - q2 - λ*math.sqrt(abs(h2)))
    q2_dot = ((g*A)/(L - zL))*(h2 - h3) - (f(q2)/(2*A*d))*q2*abs(q2)

    return [q1_dot, h2_dot, q2_dot]

# Define the constants
g = 9.81 # acceleration due to gravity
zL = 12 # distance to the leak point
f = lambda q: 0.05 # friction factor
d = 0.052 # diameter of the pipe
A = (np.pi * d ** 2) / 4 # cross-sectional area of the pipe
L = 57.76 # length of the pipe
c = 422.754 # constant of velocity

# Define the initial conditions
t0 = 0 # initial time
y0 = [0.00010,0, 0] # initial values of q1, h2, q2

h1=10
h3=3
t_final=800

# Solve the system of differential equations
from scipy.integrate import solve_ivp
sol = solve_ivp(lambda t, y: system(t, y, g, A, zL, f, d, L, c), [t0, t_final], y0)

# Extract the solution
t = sol.t
q1 = sol.y[0]
#h2 = sol.y[1]
q2 = sol.y[2]

# Plot the solution
plt.plot(t, q1, label='q1 (In)')
plt.plot(t, q2, label='q2 (Out)')
plt.ylim([0.0030, 0.0038])
plt.xlim([0, 800])
plt.xlabel('Time (s)')
plt.ylabel('Flow rate (m3/s)')
plt.legend()
plt.show()