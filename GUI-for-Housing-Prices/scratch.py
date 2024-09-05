import pymysql
import numpy as np

conn = pymysql.connect("localhost","root","","boston_housing")
myCursor = conn.cursor()

xdata = np.linspace(0,200,50)[:,np.newaxis]
noise = np.random.normal(20,10,xdata.shape) # (mean,stddev,shape)
ydata = 100/(1+np.exp(-xdata/5 + 5)) + noise

L = []
for i in range(len(xdata)):
	L.append([float(xdata[i][0]),float(ydata[i][0])])

with conn.cursor() as cursor:
    cursor.executemany("insert into pricevssqft(sqft,price) values(%s,%s)",L)
    conn.commit()

#myCursor.executemany("insert into pricevssqft(sqft,price) values(%d,%d)",L)
#conn.commit()

print('done lol')


conn.close()