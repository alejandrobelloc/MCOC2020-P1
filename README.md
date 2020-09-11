# MCOC2020-P1

# Entrega N°1

* A continuación se puede observar el gráfico que se realizó para la entrega N°1:

![alt text](https://github.com/alejandrobelloc/MCOC2020-P1/blob/master/Entrega%201/Entrega%201.png?raw=true)

# Entrega N°2

* A continuación se puede observar los gráficos de la entrega N°2, "Primeras predicciones con la EDM básica del satélite". 

![alt text](https://github.com/alejandrobelloc/MCOC2020-P1/blob/master/Entrega%202/Gr%C3%A1fico%201.png?raw=true)

 * ¿Cuanto debe valer v_tv t de modo que el satélite efectivamente orbite sin caer de vuelta dentro de la atmosfera (asuma que esta comienza a una altura de 80km)? ¿Cómo encontró Vt?
 
   - Como se puede observar en el gráfico anterior, se observa en color celeste la superficie de la tierra, en color rojo la superficie de la atmósfera y en color negro, la órbita que realiza el satélite, en este caso, el SENTINEL A1. 
   
   - En este caso, se realizaron 2 orbitas completas, variando la velocidad inicial que poseía el satelite, para ir observando como se comportaba en función de la atmosfera y la tierra. A partir de esto, se observaba que a velocidades menores al 6515 el satélite pasaría por la atmosfera y se adentraría en la tierra, que es lo que justamente NO se pedía en la entrega. Si aumentabamos la velocidad por sobre el 6515, el satélite se mantenía en orbita, sobre la atm y la tierra, por lo que cumplía. Por lo anterior, es que escogí el punto exacto de velocidad igual a 6515 metros por segundo, lo que tomaba un tiempo transcurrido de 12730 segundos , tomandolo como la mínima velocidad aproximada, que debe llevar el satélite para que no pierda su órbita. 

![alt text](https://github.com/alejandrobelloc/MCOC2020-P1/blob/master/Entrega%202/Gr%C3%A1fico%202.png?raw=true)
![alt text](https://github.com/alejandrobelloc/MCOC2020-P1/blob/master/Entrega%202/Gr%C3%A1fico%203.png?raw=true)

# Entrega N°4
![alt text](https://github.com/alejandrobelloc/MCOC2020-P1/blob/master/Entrega%20N%C2%B04/Gr%C3%A1fico%20E4.png?raw=true)

# Entrega N°5
* A continuación se observa el gráfico para la parte 1. de esta entrega, en la cual se puede analizar la posición en x,y,z que se tiene del satélite (En este caso el 1A) en función del tiempo (0 hrs, hasta las 27 hrs aprox.), donde se puede ver una relativa regularidad en el eje Z, variando de manera constante sus valores entre -5000 y +5000km cada 1.5 Hrs, en cambio, tanto en el eje x, y se analiza una distorsión en función del tiempo, de la posición del satélite. 

![alt text](https://github.com/alejandrobelloc/MCOC2020-P1/blob/master/Entrega%20N%C2%B05/E5-1.png?raw=true)
   
* Con lo realizado, es decir sin ninguna mejora en el sistema del orden de la ecuación diferencial, para una mejor convergencia del valor real y predicho por el modelo que estoy dando, se puede observar una deriva mucho mayor en el caso de Eulerint para practicamente todo el rango de horas que se pueden observar en el gráfico, no viendose una posible igualación entre ambos métodos, pues en el caso de odeint, aumenta un poco, pero es casi insignificativo a comparación de la deriva anteriormente expuesta. 
* Con lo anterior, se puede mencionar que al final del tiempo (25,5 a 26 Hrs), la deriva de Odeint es cercana a los 100 KM, y la de Eulerint se asemeja a unos 19.000, lo que tomó un tiempo muy breve en calcularlo y generar el gráfico, pues la complejidad de la EDO no es tan alta, debido a los pocos terminos que esta posee. 

![alt text](https://github.com/alejandrobelloc/MCOC2020-P1/blob/master/Entrega%20N%C2%B05/E5-2.png?raw=true)


![alt text](https://github.com/alejandrobelloc/MCOC2020-P1/blob/master/Entrega%20N%C2%B05/E5-3.png?raw=true)
![alt text](https://github.com/alejandrobelloc/MCOC2020-P1/blob/master/Entrega%20N%C2%B05/E5-4.png?raw=true)


   
