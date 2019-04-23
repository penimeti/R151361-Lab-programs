import  matplotlib.pyplot as plt
import numpy as np
import cmath as cm
x=input("enter the samples")
N=len(x)
j=cm.sqrt(-1)
y=[ ]
for n in range(0,N):
	sum=0
	for k in range(0,N):
		sum=sum+(x[k]*(np.exp((-j)*(2*np.pi/N)*k*n)))
	y=np.append(y,sum)
print y
plt.stem(np.abs(y))
plt.show( )

