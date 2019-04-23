import numpy as np
import matplotlib.pyplot as plot
import cmath as cm
def dft(x,N):
	c=0
	r=[ ]
	for k in range(N-1):
		j=cm.sqrt(-1)
		for n in range (0,N-1,1):
			c=c+(x[n]*np.exp((-(j*2*np.pi*k*n/N))))
		r.append(c)
		c=0
	return r
x1=[1,2,3,4,5,6,7,8]
N1=len(x1)
x2=[0,5,7,3,1,8,2]
N2=len(x2)
a1=dft(x1,N1)
a2=dft(x2,N2)
a3=a1+a2
a4=x1+x2
n=N1+N2-1
a5=dft(a4,n)
g1=np.abs(a1)
g2=np.abs(a2)
g3=np.abs(a3)
g4=np.abs(a5)
plot.subplot(4,1,1)
plot.stem(g1)
plot.subplot(4,1,2)
plot.stem(g2)
plot.subplot(4,1,3)
plot.stem(g3)
plot.subplot(4,1,4)
plot.stem(g4)
plot.show( )
