import matplotlib.pyplot as plt
import numpy as np
import random
import pymysql

xdata = np.linspace(0,200,50)[:,np.newaxis]
noise = np.random.normal(20,10,xdata.shape) # (mean,stddev,shape)
ydata = 100/(1+np.exp(-xdata/5 + 5)) + noise

#changes
