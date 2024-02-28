import math 
import numpy as np
from matplotlib import pyplot as plt


#-------------------------------------------------------------------------------------------------------------------------------------------#
#xdiv = 5 
ti_5 = [55+86, 58+44, 54+23, 54+18]
#td_5 =

#xdiv = 6
ti_6 = [102+292, 107+104, 94+59, 96+42]
#td_6 =

#xdiv = 7
ti_7 = [168+721, 167+205, 168+110, 174+96]
#td_7 =

#xdiv = 8
ti_8 = [250+1510, 270+403, 266+220, 245+144]
#td_8 =

#xdiv = 9
ti_9 = [392+3077, 412+714, 438+325, 411+213]
#td_9 =

#xdiv = 10
ti_10 = [580+5676, 599+1207, 635+601, 555+322]
#td_10 =

#xdiv = 11
ti_11 = [922+10565, 934+2003, 903+801, 816+437]
#td_11 =

#xdiv = 12
ti_12 = [1192+18555, 1380+3210, 1206+1223, 1148+765]
#td_12 =

#xdiv = 13
ti_13 = [1888+28774, 1891+4997, 1816+1654, 1738+987]
#td_13 =

#xdiv = 14
ti_14 = [2551+46952, 2335+7119, 2192+2310, 2193+1286]
#td_14 =

#xdiv = 15
ti_15 = [0, 3085+11070, 3084+3310, 3283+1653]
#td_15 =

#-------------------------------------------------------------------------------------------------------------------------------------------#

time_iterative = [ti_5, ti_6, ti_7, ti_8, ti_9, ti_10, ti_11, ti_12, ti_13, ti_14, ti_15]
#time_direct = [td_5, td_6, td_7, td_8, td_9, td_10, td_11, td_12, td_13, td_14, td_15]

alpha1 = np.zeros(len(time_iterative))
alpha2 = np.zeros(len(time_iterative))
alpha3 = np.zeros(len(time_iterative))
alpha4 = np.zeros(len(time_iterative))


for i, item in enumerate(time_iterative):
    alpha1[i] = item[0]

for i, item in enumerate(time_iterative):
    alpha2[i] = item[1]

for i, item in enumerate(time_iterative):
    alpha3[i] = item[2]

for i, item in enumerate(time_iterative):
    alpha4[i] = item[3]

alphas = [alpha1, alpha2, alpha3, alpha4]

plt.figure(figsize=(5, 2.7), layout='constrained')
for i, item in enumerate(alphas):
    plt.plot(item, label='α = 1.0e-{}'.format(i+1))
plt.xlabel('Element Divisions')
plt.ylabel('Time (ms)')
plt.title("α")
plt.legend()
plt.show()