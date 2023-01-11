#########################################
#        EXPERIMENTAL DESIGN
#########################################

############################################################################
# Author: Nahuel Canelo
# Email: nahuelcaneloaraya@gmail.com
############################################################################


#######################
#   IMPORT LIBRARY
########################

import math
import numpy as np
import pandas as pd
import random
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


##################################
# CREATING MULTIPLE SIMULATIONS
##################################

def system(t, y, g, A, zL, f, d, L, c,time_rupture,leak_coefficient):
    q1, h2, q2 = y
    if t < time_rupture: # if the time is greater than or equal to 300, set the value of λ to 0.5
        λ = 0
    else:
        λ = leak_coefficient # otherwise, set the value of λ leak_coefficient
    q1_dot = (g*A/zL)*(h1 - h2) - (f(q1)/(2*A*d))*q1*abs(q1)
    h2_dot = (c**2/(g*A*zL))*(q1 - q2 - λ*math.sqrt(abs(h2)))
    q2_dot = ((g*A)/(L - zL))*(h2 - h3) - (f(q2)/(2*A*d))*q2*abs(q2)

    return [q1_dot, h2_dot, q2_dot]


appended_data=[]
for i in range(1000):
    print(i)

    # Define the constants
    g = 9.81  # acceleration due to gravity
    zL = random.uniform(10, 80)  # distance to the leak point
    L = zL + random.uniform(10, 20)  # length of the pipe
    f = lambda q: 0.05  # friction factor
    d = random.uniform(0.03, 0.05)  # diameter of the pipe
    A = (np.pi * d ** 2) / 4  # cross-sectional area of the pipe
    c = 422.754  # constant

    # Define the initial conditions
    t0 = 0  # initial time
    y0 = [0.00010, 0, 0]  # initial values of q1, h2, q2

    h1 = 10
    h3 = 3
    t_final = 1000
    time_rupture= random.uniform(100, 700)
    leak_coefficient= random.uniform(0,12*10**-5)


    # Extract the solution
    sol = solve_ivp(lambda t, y: system(t, y, g, A, zL, f, d, L, c,time_rupture,leak_coefficient), [t0, t_final], y0)
    t = sol.t
    q1 = sol.y[0]
    h2 = sol.y[1]
    q2 = sol.y[2]

    # Plot the solution
    plt.plot(t, q1, label='q1 (In)')
    plt.plot(t, q2, label='q2 (Out)')
    plt.xlim([0, 1000])
    plt.xlabel('Time (s)')
    plt.ylabel('Flow rate (m3/s)')
    plt.legend()
    plt.savefig(str(i)+'.png')
    plt.clf()

    # Creating artificial variables
    q1_100_sum = q1[-100:].sum()
    q1_100_mean = q1[-100:].mean()
    q1_100_max = q1[-100:].max()
    q1_100_min = q1[-100:].min()
    ratio_q1h1=q1_100_mean/h1
    ratio_q1h3=q1_100_mean/h3

    q2_100_sum = q2[-100:].sum()
    q2_100_mean = q2[-100:].mean()
    q2_100_max = q2[-100:].max()
    q2_100_min = q2[-100:].min()
    ratio_q2h1=q2_100_mean/h1
    ratio_q2h3=q2_100_mean/h3

    dif_q1q2=q1_100_mean-q2_100_mean
    ratio_dif_q1q2_h1=dif_q1q2/h1
    ratio_dif_q1q2_h3=dif_q1q2/h3


    if leak_coefficient==0:
        zL=0

    #Saving obtained variables
    vector = pd.DataFrame([{'D': d, 'L': L, 'h1': h1, 'h3': h3,'q1_100_sum': q1_100_sum,'q1_100_mean': q1_100_mean,
                            'q1_100_max': q1_100_max, 'q1_100_min': q1_100_min, 'ratio_q1h1': ratio_q1h1, 'ratio_q1h3': ratio_q1h3,
                            'q2_100_sum': q2_100_sum, 'q2_100_mean': q2_100_mean, 'q2_100_max': q2_100_max,'q2_100_min': q2_100_min,
                            'ratio_q2h1': ratio_q2h1, 'ratio_q2h3': ratio_q2h3, 'dif_q1q2': dif_q1q2, 'ratio_dif_q1q2_h1': ratio_dif_q1q2_h1,
                            'ratio_dif_q1q2_h3': ratio_dif_q1q2_h3, 'zl': zL}])

    appended_data.append(vector)


# Saving file
appended_data = pd.concat(appended_data)
data = appended_data
data.to_csv("simulaciones_fuga_agua.csv", sep=";", index=False)
