# integration numerique par la methode des rectangles avec alpha = a

import numpy as np
import matplotlib.pyplot as plt
import time

def compute_integrale_rectangle(x, y, nbi):
    
    integrale =0.
    for i in range(nbi):
        integrale = integrale + y[i]*(x[i+1]-x[i])
        
    return integrale

def plot_integrale(x, y, nbi):
  
    for i in range(nbi):
        # dessin du rectangle
        x_rect = [x[i], x[i], x[i+1], x[i+1], x[i]] # abscisses des sommets
        y_rect = [0   , y[i], y[i]  , 0     , 0   ] # ordonnees des sommets
        plt.plot(x_rect, y_rect,"r")
t0=time.time()
xmin = 0
xmax = 3*np.pi/2
nbx = 20
nbi = nbx - 1 # nombre d'intervalles

x = np.linspace(xmin, xmax, nbx)
y = np.cos(x)
plt.plot(x,y,"bo-")

integrale = compute_integrale_rectangle(x, y, nbi)
t1=time.time()

plot_integrale(x, y, nbi)   

print("integrale =", integrale)
print("Time spent is",t1 - t0)
plt.show()
