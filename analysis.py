import math 
import numpy as np
from matplotlib import pyplot as plt


#function to calculate the logarithm of the elements of a list
def Log(n): 
    for i, item in enumerate(n):
        n[i] = math.log(item)

        
class Analysis:
    def __init__(self, norm, divisão):
        self.norm = norm #list of norms for each alpha
        self.div = divisão #xdiv value

    #function to calculate the slope and intercept of a linear regression, minimum square method to fit a straight line to a set of data points
    def mmq(self, x, y):
        n = len(x)
        x_mean = np.mean(x)
        y_mean = np.mean(y)
        m = (n*np.sum(x*y) - np.sum(x)*np.sum(y))/(n*np.sum(x**2) - np.sum(x)**2)
        c = y_mean - m*x_mean
        return m, c

    #function to calculate the r squared value, which is a measure of how well the line fits the data (regression model)
    def r_squared(x, y, m, c):
        y_ = np.mean(y)
        y_pred = m*x + c
        ss_res = np.sum((y - y_pred)**2)
        ss_tot = np.sum((y - y_)**2)
        r2 = 1 - (ss_res/ss_tot)
        return r2
    
    def analysis(self):
        for n in self.norm:
            Log(n)
            #m, c = self.mmq(np.array(list(range(1, len(self.norm)+1))), np.array(self.norm))
            #r2 = self.r_squared(np.array(list(range(1, len(self.norm)+1))), np.array(self.norm), m, c)
            #return m, c, r2

    def plot(self):
        plt.figure(figsize=(5, 2.7), layout='constrained')
        for i, item in enumerate(self.norm):
            plt.plot(item, label='α = 1.0e-{}'.format(i+1))
        plt.xlabel('Iterations')
        plt.ylabel('log(norm)')
        plt.title("xdiv = {}".format(self.div))
        plt.legend()
        plt.show()
