import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams
rcParams['figure.figsize'] = 5, 3

def plot(f,Nxlim,Pxlim):
    x=np.linspace(Nxlim,Pxlim,100)
    return plt.plot(x,f(x),),plt.axhline(0,color='k'),plt.axvline(0,color='k'),plt.xlabel('x',fontsize=20),plt.ylabel('f(x)',fontsize=20),plt.legend(loc=4),plt.show()
