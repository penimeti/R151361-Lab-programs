import  numpy as np
x=input("enter x values")
h=input("enter h values")
h1=np.zeros(len(h))
n=len(h1)
i=0
while(i<len(h1)):
	h1[i]=h[n-1]
	print(h1[i])
	i=i+1
	n=n-1
y=np.convolve(x,h1)
print y