import matplotlib.pyplot as plt
import numpy as np


def my_func(x,a,b,c,d):
    return (a*x**2 +b*x + c) / (3*x + 4*d)

plt.xkcd()

plt.style.use('seaborn-pastel')


a= -14; b = 165; c = -67; d = -7
legend = ' y = {}*x**2 + {}*x + {}'.format(a,b,c)
left = -100; right = 100; step = 0.5

data_x = []; data_y = []
pos_x = left
while pos_x <= right:
    try: 
        pos_y = my_func(pos_x, a,b,c,d)
        data_x.append(pos_x)
        data_y.append(pos_y)
    except:
        pass
    pos_x += step


plt.plot(data_x, data_y,linewidth = 3, color = '#A4A')



plt.grid(True)
plt.axhline(linewidth = 1.5, color = '#064')
plt.axvline(linewidth = 1.5, color = '#064')


plt.show()