# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b91k4yIcrapRqaN5AoK0_24NoJKgB39R
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel('HW data.xlsx')
data.head()

X=data['Height (FT)'].values
Y=data['Weight (KG)'].values

from numpy.core.fromnumeric import mean
meanX=np.mean(X)
meanY=np.mean(Y)

n=len(X)
print(meanX)
print(meanY)
numrt=0
denom=0
for i in range(n):
  numrt+= (X[i]-meanX) * (Y[i]-meanY)
  denom+=(X[i]-meanX) ** 2
print(numrt)
print(denom)
m = numrt/denom
c= meanY -  (m * meanX)
print(m)
print(c)

x=np.linspace(1,10,100)
y=(m*x)+c
plt.plot(x,y,color="r",label="Regression Line")
plt.scatter(X,Y,label="Scatter Plot")
plt.xlabel("Heigh in Feet")
plt.ylabel("Weight in KG")
plt.legend()
plt.show()

distance=0
for i in range(n):
  hx= (m*X[i]) + c
  dist= (hx - Y[i]) ** 2
  distance += dist
costJ= distance/(2*n)
print(costJ)
ss_t=0
ss_r=0
for i in range(n):
  ypred= (m*X[i]) +c 
  ss_t+=(Y[i]-meanY) **2
  ss_r+=(Y[i]-ypred) **2

r2=1 - (ss_r/ss_t)
r2

ru = 0
rd=0
for i in range(n):
  yp=(m*X[i]) + c
  ru1=(yp-Y[i])**2
  ru+=ru1
  rd1=(Y[i]-meanY) ** 2
  rd+=rd1
r2= ru/rd
print(r2)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
X = X.reshape((n,1))
rg= LinearRegression()
rg=rg.fit(X,Y)
yp1=rg.predict(X)
r2=rg.score(X,Y)
print(r2)