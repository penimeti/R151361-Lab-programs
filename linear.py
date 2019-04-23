import numpy as np
import cmath as cm
from matplotlib import pyplot as plt
x1=input ("enter the sequence1")
x2=input("enter the seqence2")
z1=[]
z2=[]
z1=np.append(z1,x1)
z2=np.append(z2,x2)
z=z1+z2
def dft(x):
	N=len(x)
	j=cm.sqrt(-1)
	y=[ ]
	for k in range(0,N):
   		sum=0
   		for n in range(0,N):
     			sum=sum+(x[n]*(np.exp((-j)*(2*np.pi/N)*n*k)))
    		y=np.append(y,sum)
	return y
a=dft(x1)
b=dft(x2)
c=a+b
d=dft(z)
print a
#print b
#print c
#print d
plt.subplot(211)
plt.stem(np.abs(c))
plt.subplot(212)
plt.stem(np.abs(d))
plt.show()
