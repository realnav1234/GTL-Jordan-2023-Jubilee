
# This is the code I used to generate and plot the poison berries. It is an optional read if you would like to read it.

import numpy as np
import matplotlib.pyplot as plt
import random

colors = []
true_poison_values = []

for i in range(100):

    x = random.random()
    colors.append(x)
    if x > 0.55:
        true_poison_values.append(1)
    else:
        true_poison_values.append(0)

plt.scatter(colors, true_poison_values)
plt.yticks([0,1])
plt.xlabel('color')
plt.ylabel('Poison vs. Safe')

plt.show()

def cost(separator, colors, true_poison_values):

    total_cost = 0

    for idx, berry_color in enumerate(colors):
        
        if berry_color > separator:
            predicted_poison_value = 1
        else:
            predicted_poison_value = 0
        
        berry_cost = (true_poison_values[idx] - predicted_poison_value) ** 2

        total_cost = total_cost + berry_cost
    
    average_cost = total_cost / len(colors)

    return average_cost

x = np.array([0.01*i for i in range(101)])
y = np.array([cost(i, colors, true_poison_values) for i in x])
poly = np.polyval(np.polyfit(x,y, 25), x)

# plt.scatter(x, y)
plt.plot(x, poly)
plt.xlabel('separator')
plt.ylabel('cost')

plt.show()

