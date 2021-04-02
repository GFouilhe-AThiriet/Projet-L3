import numpy as np
import pylab as pl 

x=np.linspace(-np.pi,np.pi,100)
y=np.sin(x)


pl.plot(x,y,label="sin")
pl.show()