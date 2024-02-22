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
n1 = [1.69112, 0.252053, 0.05527, 0.0144527, 0.00394067, 0.00108676, 0.000300674, 8.3265e-05, 2.30645e-05, 6.3894e-06, 1.77005e-06, 4.90357e-07, 1.35844e-07, 3.7633e-08, 1.04255e-08, 2.8882e-09, 8.00121e-10]
r_n1 = [6.7094, 4.56039, 3.82419, 3.66758, 3.62609, 3.6144, 3.61105, 3.61009, 3.60981, 3.60973, 3.60971, 3.6097, 3.6097, 3.6097, 3.6097, 3.6097]

#alpha = 0.1e-1
n2 = [1.85717, 0.0392603, 0.00124843, 4.48341e-05, 1.64525e-06, 6.06435e-08, 2.23743e-09, 8.25662e-11]
r_n2 = [47.3041, 31.4478, 27.8455, 27.2507, 27.1299, 27.1041, 27.0986]

#alpha = 0.1e-2
n3 = [1.88004, 0.00414888, 1.37672e-05, 5.12707e-08, 1.94747e-10]
r_n3 = [453.145, 301.359, 268.52, 263.269]

#alpha = 0.1e-3
n4 = [1.88242, 0.000417242, 1.39054e-07, 5.19766e-11]
r_n4 = [4511.57, 3000.58, 2675.32]

#alpha = 0.1e-4
#n5 =
#r_n5 =

#----------------------------------------------------------------------------------------------------------------------------------------------------------#
#xdiv = 6
#alpha = 0.1
n6 = [2.01676, 0.405784, 0.127965, 0.0479861, 0.0189326, 0.00760138, 0.00307092, 0.00124339, 0.000503831, 0.000204214, 8.27809e-05, 3.35575e-05, 1.36037e-05, 5.51471e-06, 2.23558e-06, 9.06273e-07, 3.6739e-07, 1.48935e-07, 6.03759e-08, 2.44755e-08, 9.92203e-09, 4.02225e-09, 1.63056e-09, 6.61007e-10]
r_n6 = [4.97003, 3.17106, 2.66671, 2.53457, 2.49068, 2.47528, 2.46981, 2.46786, 2.46717, 2.46692, 2.46684, 2.4668, 2.46679, 2.46679, 2.46679, 2.46679, 2.46679, 2.46679, 2.46679, 2.46679, 2.46679, 2.46679, 2.46679]

#alpha = 0.1e-1
n7 = [2.36338, 0.082134, 0.00458851, 0.000284997, 1.80774e-05, 1.15212e-06, 7.3509e-08, 4.69133e-09, 2.99418e-10]
r_n7 = [28.7747, 17.8999, 16.1002, 15.7654, 15.6905, 15.6732, 15.6691, 15.6682]

#alpha = 0.1e-2
n8 = [2.41797, 0.00907044, 5.4472e-05, 3.60448e-07, 2.42873e-09, 1.64283e-11]
r_n8 = [266.577, 166.516, 151.123, 148.41, 147.839]

#alpha = 0.1e-3
n9 = [2.42377, 0.000916481, 5.5449e-07, 3.69311e-10]
r_n9 = [2644.65, 1652.84, 1501.42]

#alpha = 0.1e-4
#n10 =
#r_n10 =

#----------------------------------------------------------------------------------------------------------------------------------------------------------#
norm = [n1, n2, n3, n4]

r_norm = [r_n1, r_n2, r_n3, r_n4]

for n in norm:
  Log(n)
  m, c = mmq(np.array(list(range(1, len(n)+1))), np.array(n))
  r2 = r_squared(np.array(list(range(1, len(n)+1))), np.array(n), m, c)
  #print(m, c)
  #print(r2)

for n in r_norm:
  Log(n)
  m, c = mmq(np.array(list(range(1, len(n)+1))), np.array(n))
  r2 = r_squared(np.array(list(range(1, len(n)+1))), np.array(n), m, c)
  #print(m, c)
  #print(r2)

#Plotting log(norm) for each alpha
  

#Plotting norm[0]/norm[1] for each alpha


#Plotting log(norm[0]/norm[1]) for each alpha




#plt.figure(1)
#plt.plot(list(range(1, len(norm1)+1)), norm1)
#plt.title('Log1')
#plt.grid(True)
#
#plt.figure(1)
#plt.plot(norm2)
#plt.title('Log1')
#plt.grid(True)
#
#plt.figure(1)
#plt.plot(norm3)
#plt.title('Log1')
#plt.grid(True)
#
#plt.figure(1)
#plt.plot(norm4)
#plt.title('Log1')
#plt.grid(True)


plt.figure(figsize=(5, 2.7), layout='constrained')
plt.plot(n1, label='α = 0.1') 
plt.plot(n2, label='α = 0.1e-1')
plt.plot(n3, label='α = 0.1e-2')
plt.plot(n4, label='α = 0.1e-3')
plt.xlabel('Iteration')
plt.ylabel('log(norm)')
plt.title("dSol vs Iteration")
plt.legend()
plt.show()

plt.figure(figsize=(5, 2.7), layout='constrained')
plt.plot(r_n1, label='α = 0.1') 
plt.plot(r_n2, label='α = 0.1e-1')
plt.plot(r_n3, label='α = 0.1e-2')
plt.plot(r_n4, label='α = 0.1e-3')
plt.xlabel('Iteration')
plt.ylabel('log(norm)')
plt.title("dSol vs Iteration")
plt.legend()
plt.show()
