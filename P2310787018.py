import matplotlib.pyplot as plt

v0 = float(input("Enter initial velocity (m/s): "))
a = float(input("Enter deceleration (m/s^2): "))

time = [t/10 for t in range(int(10*v0/a)+1)]
distance = [v0*t - 0.5*a*t**2 for t in time]
velocity = [v0 - a*t for t in time]

plt.subplot(2, 1, 1)
plt.plot(time, distance)
plt.title('Braking Distance over Time')
plt.xlabel('Time (s)')
plt.ylabel('Distance (m)')

plt.subplot(2, 1, 2)
plt.plot(time, velocity)
plt.title('Velocity over Time')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')

plt.tight_layout()
plt.show()