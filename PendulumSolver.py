import matplotlib.pyplot as plt
import numpy as np

s0 = int(input("starting angle (degrees): "))/180 * np.pi
dds = 0
ds = int(input("Starting Anglular speed (degrees): "))/180 * np.pi
ds0 = ds
s = [s0]
t = [0]
dt = float(input("Chose for the value of delta T : "))
wantedTime = float(input("Simulation Duration: "))
g = float(input("Gravity Acceleration: "))
l = float(input("Lenght of the Rope: "))
n = wantedTime/dt

for i in range(0, int(n) + 1):
    dds = -g/l * np.sin(s[i])
    ds += dds * dt
    s.append(s[i] + ds * dt)
    t.append(i*dt)

x = np.arange(0,wantedTime, dt)
w = np.sqrt(g/l)
y = s0 * np.cos(x * w) + ds0/w * np.sin(x * w)

plt.plot(x,y, label= "Small Angle Approximation")
plt.plot(t,s, label= "Numeric Approximatoin")

plt.xlabel("Time Axis")
plt.ylabel("Theta axis")

plt.legend()
plt.show()
