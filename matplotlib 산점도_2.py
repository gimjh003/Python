import matplotlib.pyplot as plt
import random

x = []
y = []

for i in range(100):
    x.append(random.randint(1, 100))
    y.append(random.randint(1, 100))

color = []
area = []

import math

for i in range(100):
    color.append(random.randint(1, 100))
    area.append(math.pi*random.randint(1, 100)**2)

plt.scatter(x, y, s=area, c=color, alpha=0.3) # alpha는 투명도
plt.show()