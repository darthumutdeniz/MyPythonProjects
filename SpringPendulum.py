import matplotlib.pyplot as plt
import numpy as np

s0 = int(input("starting angle (degrees): "))/180 * np.pi
dds = 0
ds = int(input("Starting Anglular speed (degrees): "))/180 * np.pi
ds0 = ds
s = [s0]
r0 = int(input("Starting Length: "))
ddr = 0
dr = int(input("Starting radial speed: "))
r = [r0]
l = float(input("Equilibrium length: "))
g = -float(input("Gravity Acceleration: "))
k = float(input("Spring Constant: "))
m = float(input("Mass of the object: "))
dt = float(input("Chose for the value of delta T : "))
wantedTime = float(input("Simulation Duration: "))
t = [0]
n = wantedTime/dt

for i in range(0, int(n) + 1):
    dds = -g/r[i] * np.sin(s[i]) -2*dr*ds/r[i]
    ddr = g * np.cos(s[i]) + r[i]*(ds**2) - k*(r[i] - l)/m
    ds += dds * dt
    dr += ddr * dt
    s.append((s[i] + ds * dt) % (np.pi * 2))
    r.append(r[i] + dr * dt)
    t.append(i*dt)

plt.plot(t,s, label= "Angle Numeric Approximatoin")
plt.plot(t,r, label= "Radial Numeric Approximatoin")

plt.xlabel("Time Axis")
plt.ylabel("Theta and Radial axis")

plt.legend()
plt.show()
