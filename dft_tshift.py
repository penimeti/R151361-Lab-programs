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
k=input("enter the shift value")
x1=[3,4,5,7,8,9,2,1]
N1=len(x1)
x2=[ ]
for n in range(N1):
	v=x1[n-k]
	x2.append(v)
N2=len(x2)
print(x2)
a1=dft(x1,N1)
a2=dft(x2,N2)
print(a2)
#j=cm.sqrt(-1)
b=[]
for k in range(N1):
	s=np.exp(-1j*2*np.pi*k/N1)
	b.append(s)
print(b)
b1=[]
for i in range(N1-1):
	s=b[i]*a1[i]
	b1.append(s)
g1=np.angle(a1)
g2=np.angle(a2)
g3=np.angle(b1)
g4=np.angle(x2)
plot.subplot(4,1,1)
plot.stem(x1)
plot.subplot(4,1,2)
plot.stem(x2)
plot.subplot(4,1,3)
plot.plot(g1)
plot.subplot(4,1,4)
plot.plot(g3)
plot.show( )
