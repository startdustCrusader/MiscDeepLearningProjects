import matplotlib.pyplot as plt
import numpy as np
import random
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

xdata = np.linspace(0,200,50)[:,np.newaxis]
noise = np.random.normal(20,10,xdata.shape) # (mean,stddev,shape)
ydata = 1000/(1+np.exp(-xdata/100 + 5)) + 0.6*noise

degree = 5
lw = 2
count = 0
colors = ['teal', 'yellowgreen', 'gold']
model = make_pipeline(PolynomialFeatures(degree), Ridge())
model.fit(xdata,ydata)

def Regression():
	#return(model.predict([float(n)]))
	print(n)