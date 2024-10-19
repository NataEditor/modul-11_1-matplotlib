import matplotlib.pyplot as plt
import numpy as np

names = 'Nissan', 'Mitsubishi', 'Suzuki', 'Toyota', 'Honda', 'Chevrolet'
fraction = [3, 7, 8, 4, 12, 2]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red', 'blue']
explode = (0.3, 0, 0, 0, 0, 0)
plt.pie(fraction, explode=explode, labels=names, colors=colors, autopct='%1.1f%%', shadow=True, startangle=150)
plt.axis('equal')
plt.show()


