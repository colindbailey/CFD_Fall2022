# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 08:52:15 2021

@author: baileycd2
"""
#this code will show how the Runge Kutta method is used in python
import numpy as np
import matplotlib.pyplot as plt

def RungeKutta(f,x0,t):
    x = np.zeros(len(t))
    x[0] = x0
    for n in range (0,len(t)-1):
        e1 = h*f(x[n],t[n]) #defines all of the parts of the runge kutta
        e2 = h*f(x[n]+(e1/2),t[n])
        e3 = h*f(x[n]+(e2/2),t[n])
        e4 = h*f(x[n]+e3,t[n])
        x[n+1] = x[n] + ((e1 +(2*e2)+(2*e3)+e4)/6) #puts them all together
    return x

t0 = 0 #intial time point
tf = 1 #final time point
n = 0 #used to change the time step
h = 10 ** (-n) # this creates the time step
print ('Time Step = ', h)

t = np.arange(t0,tf+h,h) #creates an array of the time step
x0 = 1 #intial value
f = lambda x, t: -x #defines f for the function
x = RungeKutta(f,x0,t) #runs the rungekutta function
x_true = np.exp(-t) #has the true value of the function that the runge kutta will be compared to

E = abs(x - x_true) #error between them

Ex = np.log(E)

tx = np.log(t)

#this will plot the true value versus the runge kutta and you can see the difference
plt.plot(t,x,'b.-',t,x_true,'r-')
# plt.plot(tx,Ex)
# plt.plot(t,E)
plt.legend(['RungeKutta','True'])
plt.grid(True)
plt.title("Solution of $x'=-x, x(0)=1$, Time step = "+str(h))
plt.xlabel ('Time')
plt.ylabel ('Value')
plt.show()