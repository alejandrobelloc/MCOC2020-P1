# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 18:14:45 2020

@author: Ale
"""

from matplotlib.pylab import *
from scipy.integrate import odeint
import numpy as np

# DATOS: 
    
m = 1             # MASA EN KG
f = 1.            # FRECUENCIA EN HZ
E = 0.2           
w = 2 * pi * f
k = m * (w**2)
c = 2 * E * w * m

# DEFINICIONES GENERALES CLASE 31/08/2020

def solucion(z,t):
    
    zp = zeros(2)
    
    zp[0] = z[1]
    
    z1 = z[0]
    
    z2 = z[1]
    
    zp[1] = -(c * z2 + k * z1) / m
    
    return zp 

def eulerint(zp, z0, t, Nsubdivisiones = 1):
    
    Nt  = len(t)
    Ndim = len(array(z0))
    
    z = zeros((Nt, Ndim))
    
    z[0,:] = z0[0]
    
    for i in range(1, Nt):
        
        t_anterior = t[i-1]
        dt =  (t[i] - t[i-1]) / Nsubdivisiones
        z_temp = z[i-1, :]
        
        for k in range (Nsubdivisiones):
            
            z_temp += dt * solucion(z_temp, t_anterior + k * dt)
        
        z[i,:] = z_temp
               
    return z

# DATOS PARA LA ENTREGA:
    
t = linspace(0, 4., 100)
z0 = [1,1]

real = exp(-c*t/2)*cos(w*t)

# PARA EL GRÁFICO DE LA SOLUCIÓN ODEINT: 
    
sol = odeint(solucion, z0, t)
z_odeint = sol[:, 0]
plt.plot(t, z_odeint, label = "Odeint", color = "blue")

# PARA EL GRÁFICO DE EULER CON SUS RESPECTIVAS NSUBDIVISIONES:
    
zp = sol[:, :]
sol = eulerint(zp, z0, t, Nsubdivisiones = 1) 
euler = sol[:,0]
plt.plot(t, euler, ":,", label = "Eulerint Nsubdivisión = 1", color = "green")

sol = eulerint(zp, z0, t, Nsubdivisiones = 10)
euler = sol[:,0]
plt.plot(t, euler, ":,", label = "Eulerint Nsubdivisión = 10", color = "red")

sol = eulerint(zp, z0, t, Nsubdivisiones = 100)
euler = sol[:,0]
plt.plot(t, euler, ":,", label = "Eulerint Nsubdivisión = 100", color = "orange")

# PARA LA RESOLUCIÓN ANALÍTICA DE LA EDO OSCILADOR ARMÓNICO:

plt.plot(t, real, color = "black", label = "Analítica", linewidth = 2)

# FINALMENTE, CARACTERÍSTICAS DEL GRÁFICO: 

csfont = {'fontname':'CMU Serif'}
plt.grid(True)
plt.legend(loc='upper right', fontsize = 9, shadow = True, facecolor = "oldlace")
plt.title("Oscilador Armónico", **csfont, fontsize = 15)
plt.xlabel("Tiempo", **csfont, fontsize = 12)
plt.ylabel("Posicion en x(t)", **csfont, fontsize = 12)
