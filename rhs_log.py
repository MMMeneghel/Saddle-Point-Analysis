import math 
import numpy as np
from matplotlib import pyplot as plt

#function to calculate the logarithm of the elements of a list
def Log(norm): 
  for i, item in enumerate(norm):
      norm[i] = math.log(item)

#minimum square method to fit a straight line to a set of data points, linear regression
def mmq(x, y):
    n = len(x)
    x_ = np.mean(x)
    y_ = np.mean(y)
    m = (n*np.sum(x*y) - np.sum(x)*np.sum(y))/(n*np.sum(x**2) - (np.sum(x))**2)
    c = y_ - m*x_
    return m, c 

#function to calculate the r squared value, which is a measure of how well the line fits the data (regression model)
def r_squared(x, y, m, c):
    y_ = np.mean(y)
    y_pred = m*x + c
    ss_res = np.sum((y - y_pred)**2)
    ss_tot = np.sum((y - y_)**2)
    r2 = 1 - (ss_res/ss_tot)
    return r2

#----------------------------------------------------------------------------------------------------------------------------------------------------------#
#Arrays, for each alpha, with the values of the relation between the norm of the previous iteration and the norm of the current iteration

#xdiv = 5
#alpha = 0.1
n1 = [0.15231, 0.0221501, 0.00518877, 0.00137366, 0.00037565, 0.000103679, 2.86916e-05, 7.946e-06, 2.20109e-06, 6.09756e-07, 1.6892e-07, 4.6796e-08, 1.2964e-08, 3.59142e-09, 9.94935e-10, 2.75628e-10, 7.63576e-11]
r_n1 = [6.87626, 4.26886, 3.77733, 3.65676, 3.62319, 3.61358, 3.61082, 3.61002, 3.60979, 3.60973, 3.60971, 3.6097, 3.6097, 3.6097, 3.6097, 3.6097]

#alpha = 0.1e-1
n2 = [0.0172662, 0.000356789, 1.18287e-05, 4.27272e-07, 1.56965e-08, 5.787e-10, 2.1352e-11, 7.87945e-13]
r_n2 = [48.3933, 30.1629, 27.6843, 27.2209, 27.1237, 27.1028, 27.0984]

#alpha = 0.1e-2
n3 = [0.001753, 3.78256e-06, 1.30535e-08, 4.88698e-11, 1.85805e-13]
r_n3 = [463.443, 289.772, 267.108, 263.017]

#alpha = 0.1e-3
n4 = [0.000175572, 3.80524e-08, 1.31854e-11, 4.99062e-15]
r_n4 = [4613.96, 2885.94, 2642.04]

#alpha = 0.1e-4
#n5 =
#r_n5 =

#----------------------------------------------------------------------------------------------------------------------------------------------------------#
#xdiv = 6
#alpha = 0.1
n6 = [0.190554, 0.0377731, 0.0124113, 0.00468992, 0.00185431, 0.000745016, 0.000301055, 0.000121905, 4.93983e-05, 2.00224e-05, 8.11639e-06, 3.29021e-06, 1.33379e-06, 5.407e-07, 2.19192e-07, 8.88572e-08, 3.60214e-08, 1.46026e-08, 5.91967e-09, 2.39975e-09, 9.72824e-10, 3.94369e-10, 1.59871e-10, 6.48096e-11]
r_n6 = [5.0447, 3.04344, 2.64638, 2.52921, 2.48895, 2.47468, 2.4696, 2.46779, 2.46714, 2.46691, 2.46683, 2.4668, 2.46679, 2.46679, 2.46679, 2.46679, 2.46679, 2.46679, 2.46679, 2.46679, 2.46679, 2.46679, 2.46679]

#alpha = 0.1e-1
n7 = [0.0228905, 0.00078727, 4.48466e-05, 2.79249e-06, 1.77217e-07, 1.12958e-08, 7.20727e-10, 4.5997e-11, 2.93569e-12]
r_n7 = [29.0759, 17.5547, 16.0597, 15.7575, 15.6888, 15.6728, 15.669, 15.6682]

#alpha = 0.1e-2
n8 = [0.00234696, 8.71713e-06, 5.32667e-08, 3.53226e-10, 2.38103e-12, 1.61229e-14]
[269.236, 163.651, 150.801, 148.35, 147.68]
r_n8 =

#alpha = 0.1e-3
n9 = [0.000235308, 8.81009e-08, 5.42247e-11, 3.61979e-14, ]
[2670.9, 1624.74, 1498.01, ]
r_n9 =

#alpha = 0.1e-4
n10 =
r_n10 =

#----------------------------------------------------------------------------------------------------------------------------------------------------------#


norm = [norm1, norm2, norm3, norm4, norm5, norm6, norm7, norm8, norm9, norm10]

for n in norm:
  Log(n)
  m, c = mmq(np.array(list(range(1, len(n)+1))), np.array(n))
  r2 = r_squared(np.array(list(range(1, len(n)+1))), np.array(n), m, c)
  print(m, c)
  print(r2)



#Plotting log(norm) for each alpha
  

#Plotting norm[0]/norm[1] for each alpha


#Plotting log(norm[0]/norm[1]) for each alpha




plt.figure(1)
plt.plot(list(range(1, len(norm1)+1)), norm1)
plt.title('Log1')
plt.grid(True)

plt.figure(1)
plt.plot(norm2)
plt.title('Log1')
plt.grid(True)

plt.figure(1)
plt.plot(norm3)
plt.title('Log1')
plt.grid(True)

plt.figure(1)
plt.plot(norm4)
plt.title('Log1')
plt.grid(True)

plt.figure(1)
plt.plot(norm5)
plt.title('Log1')
plt.grid(True)
plt.show()

plt.figure(2)
plt.plot(norm6)
plt.title('Log2')
plt.grid(True)

plt.figure(2)
plt.plot(norm7)
plt.title('Log2')
plt.grid(True)

plt.figure(2)
plt.plot(norm8)
plt.title('Log2')
plt.grid(True)

plt.figure(2)
plt.plot(norm9)
plt.title('Log2')
plt.grid(True)

plt.figure(2)
plt.plot(norm10)
plt.title('Log2')
plt.grid(True)
plt.show()