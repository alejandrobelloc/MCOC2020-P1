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
from datetime import datetime

# Parámetros de la tierra

G = 6.674e-11                   # Unidad [Nm2 / Kg2]
masa = 5.972e24                 # Unidad [Kg]
omega = 7.27e-5                 # Unidad [rad / s] 
atmosfera =  6451000

# Relación tierra - satélite

rtierra = 6371000
rtotal = 7071000                # Unidad de [m] ; Distancia desde el centro de la tierra hasta el punto del satélite. 

ti = "2020-08-06T22:59:42.000000"
ti = ti.split("T")
ti = "{} {}".format(ti[0],ti[1])
ti = datetime.strptime(ti, '%Y-%m-%d %H:%M:%S.%f')

tf = "2020-08-08T00:59:42.000000"
tf = tf.split("T")
tf = "{} {}".format(tf[0],tf[1])
tf = datetime.strptime(tf, '%Y-%m-%d %H:%M:%S.%f')

deltaT = (tf-ti).total_seconds()

# Los datos son los siguientes

# <TAI>TAI=2020-08-06T23:00:19.000000</TAI>
# <UTC>UTC=2020-08-06T22:59:42.000000</UTC>
# <UT1>UT1=2020-08-06T22:59:41.796580</UT1>
# <Absolute_Orbit>+33792</Absolute_Orbit>
# <X unit="m">297739.219251</X>
# <Y unit="m">2508313.547347</Y>
# <Z unit="m">-6616305.115811</Z>
# <VX unit="m/s">2396.505505</VX>
# <VY unit="m/s">-6747.044106</VY>
# <VZ unit="m/s">-2451.164493</VZ>

xi = 297739.219251
yi = 2508313.547347
zi = -6616305.115811
vxi = 2396.505505 
vyi = -6747.044106                     
vzi = -2451.164493

# <TAI>TAI=2020-08-08T01:00:19.000000</TAI>
# <UTC>UTC=2020-08-08T00:59:42.000000</UTC>
# <UT1>UT1=2020-08-08T00:59:41.796971</UT1>
# <Absolute_Orbit>+33808</Absolute_Orbit>
# <X unit="m">1757541.908660</X>
# <Y unit="m">6851804.667799</Y>
# <Z unit="m">209566.915093</Z>
# <VX unit="m/s">1591.064635</VX>
# <VY unit="m/s">-171.465449</VY>
# <VZ unit="m/s">-7426.871314</VZ>

xf = 1757541.908660
yf = 6851804.667799
zf = 209566.915093
vxf = 1591.064635
vyf = -171.465449
vzf = -7426.871314

t = sp.linspace(0, deltaT, 9361)
z0 = sp.array([xi, yi, zi, vxi, vyi, vzi]) # Los valores 0 se deben a que posee posición en un inicio solo en el eje X, además de velocidad en el eje Y.


def satelite(z, t):
    
    # Definimos nuestra e.d:
    
    rtetha = sp.array([[cos(omega*t),-sin(omega*t),0], [sin(omega*t),cos(omega*t),0], [0, 0, 1]])
    rthetap = sp.array([[-sin(omega*t)* omega,-cos(omega*t)* omega,0], [cos(omega*t)* omega,-sin(omega*t)* omega,0], [0, 0, 0]])
    rtheta2p = sp.array([[-cos(omega*t)* omega**2,sin(omega*t)* omega**2, 0], [-sin(omega*t)* omega**2,-cos(omega*t)* omega**2,0], [0, 0, 0]])
    
    zp = sp.zeros(6)
    zp[0:3] = z[3:6]

    zp[3:6] = ((-G * masa * z[0:3]) / rtotal**3) - (rtetha.T @ (rtheta2p @ z[0:3] + 2 * rthetap @ z[3:6]))
    
    return zp

sol = odeint(satelite,z0,t)
x = sol[:,:]
pos_final = sp.array([xf, yf, zf, vxf, vyf, vzf]) - sol[-1]

for el in pos_final:
    print (el)
    
# Al correr el código, muestra lo solicitado!






    

    
    
    
    
    
        





    
    
    




