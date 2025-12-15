print ("Welcome to Time Distance Graph")

import matplotlib.pyplot as plt

##Data
x = [1, 2, 3, 4, 5, 7, 9]
y = [3, 4, 8, 10, 11, 22, 12]

##Plot
plt.plot(x, y)
plt.xlabel("Distance")
plt.ylabel("Time")
plt.title("Distance Time Graph")

plt.show()



x = [1, 2, 3, 4, 5, 7, 9]
y = [3, 4, 8, 10, 11, 22, 0]

velocity = [a/b for a, b in zip(x, y)]

print("Velocity= ", velocity)