import matplotlib.pyplot as plot 
import numpy as np
x=input("enter x samples:")
h=input("enter h samples:")
lx=len(x)
lh=len(h)
y=[ ]
for n in range (lx+lh-1):
	sum=0
	for k in range(lx):
		if(n-k<lh and n-k>=0):
			sum=sum+x[k]*h[n-k]
	y=np.append(y,sum)
print y			
y1=np.convolve(x,h)
print y1
			