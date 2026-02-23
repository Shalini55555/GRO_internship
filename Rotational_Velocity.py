import numpy as np

# Function to calculate the rotational velocity from radial velocity(v_r_max) and distance from GC (R)
def rot_vel(v_r_max, R , R0 , V0=220):
    V_star= v_r_max + (R/R0) * V0
    return V_star

v_r_max = -8.315
R= 8.44
R0=8.5

V_star=rot_vel(v_r_max,R,R0)   # Rotational velocity
print(V_star)
