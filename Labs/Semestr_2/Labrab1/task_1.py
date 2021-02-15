import matplotlib.pyplot as plt
import numpy as np


plt.style.use('ggplot')


x = np.linspace(-5,5,100)
y = 9.5*x**3 - 500


fig, ax = plt.subplots()


ax.plot(x,y, color = 'black', lw = 4)
ax.vlines(0, y.min(), y.max(),color = 'blue',lw = 2)
ax.hlines(0, x.min(), x.max(),color = 'blue',lw = 2)


fig.set_figwidth(4); fig.set_figheight(8)


plt.show()