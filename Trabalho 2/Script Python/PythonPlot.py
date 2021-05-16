# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 19:39:11 2020

@author: Ciro André Pitz
"""

import numpy as np
import matplotlib.pyplot as plt


# parametros
beta = 3740

T = np.arange(273.0,323,0.0001) #0.0001 para aumentar a precisão, 0.1 tava alterando significativamente o valor do RT min

r1 = .1
r2 = 0.235
r3 = 1
r4 = 10

vo = 0.517
c = 8.34 #coeficiente da equação (iii)


RT = 12e3*np.exp(beta*((1/T)-(1/298)))
RTmin = np.min(RT)
RTmax = np.max(RT)

print(RTmin)
print(RTmax)

Vi1 = vo/((1/(1+r1)) - (1/(1+c*r1)))
Vi2 = vo/((1/(1+r2)) - (1/(1+c*r2)))
Vi3 = vo/((1/(1+r3)) - (1/(1+c*r3)))
Vi4 = vo/((1/(1+r4)) - (1/(1+c*r4)))


v01 = Vi1*((1/(1+r1)) - (1/(1+r1*RTmax/RT)))
v02 = Vi2*((1/(1+r2)) - (1/(1+r2*RTmax/RT)))
v03 = Vi3*((1/(1+r3)) - (1/(1+r3*RTmax/RT)))
v04 = Vi4*((1/(1+r4)) - (1/(1+r4*RTmax/RT)))

v0linear = (T - 273)/96.71


plt.plot(T, v01,color='red')
plt.plot(T, v02,color='green')
plt.plot(T, v03,color='blue')
plt.plot(T, v04,color='orange')
plt.plot(T, v0linear,color='black')
plt.ylabel('V0 (V)')
plt.xlabel('T (K)')
plt.legend(['r = 0.1','r = 0.235','r = 1','r = 10','linear'])
plt.grid()
plt.show()


plt.plot(T, 100*abs(v01 - v0linear)/vo,color='red')
plt.plot(T, 100*abs(v02 - v0linear)/vo,color='green')
plt.plot(T, 100*abs(v03 - v0linear)/vo,color='blue')
plt.plot(T, 100*abs(v04 - v0linear)/vo,color='orange')
plt.ylabel('NL (%)')
plt.xlabel('T (K)')
plt.legend(['r = 0.1','r = 0.235','r = 1','r = 10'])
plt.ylim(0,10)
plt.grid()
plt.show()
