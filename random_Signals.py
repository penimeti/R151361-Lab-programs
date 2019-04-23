import numpy as np
from matplotlib import pyplot as plt
from scipy import signal
Fs=4000
f1=10
t=np.linspace(0,400,200)
u=np.sin(2*np.pi*f1*t/Fs)
x=signal.square(2*np.pi*5*t)
v=10*np.random.rand(x.shape[0])
y=10*np.random.rand(u.shape[0])
a=u+y
b=x+v
plt.subplot(411)
plt.plot(t,a)
plt.subplot(412)
plt.plot(t,b)
plt.subplot(413)
plt.plot(t,x)
plt.subplot(414)
plt.plot(t,v)
plt.show()
