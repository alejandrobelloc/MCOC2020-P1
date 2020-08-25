# -*- coding: utf8 -*-
"""
Created on Mon Aug 24 20:43:03 2020

@author: Ale
"""

# La primera parte del código se baso en lo realizado en la clase del 24/08/2020.

import scipy as sp
from scipy.integrate import odeint 
import matplotlib.pylab as plt

# Parametros: 

cm = 0.01
inch = 2.54 * cm    
g = 9.81
masa = 15.

# Datos para el calculo del coef. de arrastre:

ρ = 1.225 
cd = 0.47 
diamb = 8.5 * inch
radiob = diamb / 2
areab = sp.pi * (radiob**2)
CD = 0.5 * ρ * cd * areab

viento = [0, 10., 20.]

def bala(z,t):
    
    zp = sp.zeros(4)
    
    zp[0] = z[2]
    zp[1] = z[3]
    
    v = z[2:4] 
    v[0] = v[0] - i  
    v2 = sp.dot(v,v)
    vnorma = sp.sqrt(v2)
    FD = -CD * v2 * (v / vnorma)
    
    zp[2] = FD[0] / masa
    zp[3] = FD[1] / masa - g
    
    return zp
    
t = sp.linspace(0, 30, 1001)

vi = 100*1000 / 3600
z0 = sp.array([0, 0, vi, vi])

plt.figure(1)

for i in viento: 
    
    sol = odeint(bala, z0, t)
    x = sol[:, 0]
    y = sol[:, 1]
    
    plt.plot(x, y, label = f"V = {i} m/s")
    
# Damos las características a nuestro grafico: 
    
plt.title("Trayectoria para distintos vientos")
plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.grid(True)

plt.xlim([0, 150])
plt.ylim([0, 50])

plt.legend()
plt.tight_layout()

plt.savefig("Entrega 1.png",dpi=500)

    

    
    
    
    
    
        





    
    
    




