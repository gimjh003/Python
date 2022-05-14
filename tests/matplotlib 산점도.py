import matplotlib.pyplot as plt
import random

x = []
y = []
for i in range(100):
    x.append(random.randint(1, 100))
    y.append(random.randint(1, 100))
plt.scatter(x, y)
plt.show()