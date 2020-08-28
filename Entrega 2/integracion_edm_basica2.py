  # -*- coding: utf8 -*-
"""
Created on Mon Aug 24 20:43:03 2020

@author: Ale
"""

# La primera parte del código se baso en lo realizado en la clase del 24/08/2020.

import scipy as sp
from scipy.integrate import odeint
from scipy import sin, cos
import matplotlib.pylab as plt

# Parámetros de la tierra

G = 6.674e-11                   # Unidad [Nm2 / Kg2]
masa = 5.972e24                 # Unidad [Kg]
omega = 7.27e-5                 # Unidad [rad / s] 
atmosfera =  6451000

# Relación tierra - satélite

rtierra = 6371000
rtotal = 7071000                # Unidad de [m] ; Distancia desde el centro de la tierra hasta el punto del satélite. 
vy = 6515                       # Unidad de [m / s]

t = sp.linspace(0,12730,10000)
z0 = sp.array([rtotal, 0, 0, 0, vy, 0]) # Los valores 0 se deben a que posee posición en un inicio solo en el eje X, además de velocidad en el eje Y.


def satelite(z, t):
    
    # Definimos nuestra e.d:
    
    rtetha = sp.array([[cos(omega*t),-sin(omega*t),0], [sin(omega*t),cos(omega*t),0], [0, 0, 1]])
    rthetap = sp.array([[-sin(omega*t)* omega,-cos(omega*t)* omega,0], [cos(omega*t)* omega,-sin(omega*t)* omega,0], [0, 0, 0]])
    rtheta2p = sp.array([[-cos(omega*t)* omega**2,sin(omega*t)* omega**2, 0], [-sin(omega*t)* omega**2,-cos(omega*t)* omega**2,0], [0, 0, 0]])
    
    zp = sp.zeros(6)
    zp[0:3] = z[3:6]

    zp[3:6] = ((-G * masa * z[0:3]) / rtotal**3) - (rtetha.T @ (rtheta2p @ z[0:3] + 2 * rthetap @ z[3:6]))
    
    return zp

plt.figure(1)
    
sol = odeint(satelite,z0,t)

x = sol[:,0]
y = sol[:,1]
z = sol[:,2]

plt.hlines(y=6371000,xmin=0,xmax=12000, color="r", label = "Distancia del radio Tierra")
plt.hlines(y=6451000,xmin=0,xmax=12000, color="g", label = "Distancia del radio Atmosfera")
plt.hlines(y=7071000,xmin=0,xmax=12000, color="black", label = "Distancia del radio Satélite")

plt.legend()
plt.title("Satélite Sentinel 1A Dos órbitas")
plt.xlabel('Tiempo (s)')
plt.ylabel("Distancia (m)")
plt.grid(True)

plt.tight_layout()




    

    
    
    
    
    
        





    
    
    




