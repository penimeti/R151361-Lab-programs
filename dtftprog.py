import matplotlib.pyplot as plt
import numpy as np 
import cmath as cm
x=input("enter the values")
l=len(x)
j=cm.sqrt(-1)
w=np.linspace(0,2*(np.pi),1000)
y=[ ]
for i in range(0,1000):
	sum=0
	for n in range(0,l):
		sum=sum+x[n]*np.exp((-j)*w[i]*n)
	y=np.append(y,sum)
print y
plt.subplot(121)
plt.title("magnitude")
plt.plot(w,np.abs(y))
plt.subplot(122)
plt.title("phase")
plt.plot(w,np.angle(y))
plt.show( )
	

