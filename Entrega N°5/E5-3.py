  # -*- coding: utf8 -*-
"""
Created on Mon Aug 24 20:43:03 2020

@author: Ale
"""

import scipy as sp
from scipy.integrate import odeint
from scipy import sin, cos
import matplotlib.pylab as plt
from datetime import datetime
from leer_eof import leer_eof

# PARAMETROS DE LA TIERRA:

G = 6.674e-11                   # UNIDAD [Nm2 / Kg2]
masa = 5.972e24                 # UNIDAD [Kg]
omega = 7.27e-5                 # UNIDAD [rad / s] 

atmosfera =  6451000            # UNIDAD [m] ; Distancia desde el centro de la tierra hasta el punto de la atmósfera (80 km +). 
rtierra = 6371000               # UNIDAD [m] ; Distancia desde el centro de la tierra hasta el punto del exterior de la tierra. 

def satelite(z, t):
    
    a = z[0]
    b = z[1]
    c = z[2]
    
    J2 = 1.75553*(10**10)*1000**5
    J3 = -2.61913*(10**11)*1000**6
    
    zp = sp.zeros(6)
    z1 = z[0:3]
    r2 = sp.dot(z1,z1)
    r = sp.sqrt(r2)
    zp[0:3] = z[3:6]
    
    # DEFINIMOS NUESTRA E.D: 
    
    FxJ2 = J2 * (a / r**7) * (6 * c**2-3/2 * (a**2 + b**2))
    FyJ2 = J2 * (b / r**7) * (6 * c**2-3/2 * (a**2 + b**2))
    FzJ2 = J2 * (c / r**7) * (3 * c**2-9/2 * (a**2 + b**2))
    FJ2 = sp.array([FxJ2,FyJ2,FzJ2])
    
    FxJ3 = J3* a * c / r**9 * (10 * c**2-15/2 * (a**2 + b**2))
    FyJ3 = J3 * b * c / r**9 * (10 * c**2-15 / 2 * (a**2 + b**2))
    FzJ3 = J3 / r**9 * (4 * c**2 * (c**2-3 * (a**2 + b**2)) + 3/2 * (a**2 + b**2)**2)
    FJ3 = sp.array([FxJ3,FyJ3,FzJ3])
    
    rtetha = sp.array([[cos(omega*t),-sin(omega*t),0], [sin(omega*t),cos(omega*t),0], [0, 0, 1]])
    rthetap = sp.array([[-sin(omega*t)* omega,-cos(omega*t)* omega,0], [cos(omega*t)* omega,-sin(omega*t)* omega,0], [0, 0, 0]])
    rtheta2p = sp.array([[-cos(omega*t)* omega**2,sin(omega*t)* omega**2, 0], [-sin(omega*t)* omega**2,-cos(omega*t)* omega**2,0], [0, 0, 0]])

    zp[3:6] = ((-G * masa * z[0:3]) / r**3) - (rtetha.T @ (rtheta2p @ z[0:3] + 2 * rthetap @ z[3:6])) + FJ2[0:3] + FJ3[0:3]
    
    return zp

# LEEMOS EL ARCHIVO DADO POR EL PROFESOR: 

t, x, y, z, vx, vy, vz = leer_eof('S1A_OPER_AUX_POEORB_OPOD_20200827T121209_V20200806T225942_20200808T005942.EOF') 

# DATOS PARA LA SOLUCIÓN DEL PROBLEMA (CONDICIONES INICIALES): 
    
z0 = sp.array([x[0] ,y[0], z[0], vx[0], vy[0], vz[0]])
 
sol = odeint(satelite,z0,t)
X = sol[:,0]
Y = sol[:,1]
Z = sol[:,2]

# DEFINIMOS NUESTRO GRÁFICO: 

xl = [0, 18000, 36000, 54000, 72000, 90000]
x1 = ["0", "5", "10", "15", "20", "25"]
yl = [-5e6, 0, 5e6]
y1 = ["-5000", "0", "5000"]
csfont = {'fontname':'Arial'}
plt.grid(False)
plt.figure()

# DAMOS LAS CARACTERISTICAS:
    
plt.subplot(3,1,1)
plt.title("Posición", **csfont)
plt.plot(t, X, 'black')
plt.ylabel("X (Km)", **csfont)
plt.yticks(yl, y1, **csfont)
plt.xticks(xl, x1, **csfont)

plt.subplot(3,1,2)
plt.plot(t, Y, 'black')
plt.ylabel("Y (Km)", **csfont)
plt.yticks(yl, y1, **csfont)
plt.xticks(xl, x1, **csfont)

plt.subplot(3,1,3)
plt.plot(t, Z, 'black')
plt.ylabel("Z (Km)", **csfont)
plt.yticks(yl, y1, **csfont)
plt.xticks(xl, x1, **csfont)

plt.xlabel("Tiempo t (horas)", **csfont)
plt.tight_layout()








    

    
    
    
    
    
        





    
    
    




