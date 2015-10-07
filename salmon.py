__author__ = 'Suraj'


from numpy import *
from scipy import signal
#import numpy as np
import matplotlib.pyplot as plt


#Signal 1

amp1=10.
freq1=2.0 #hz

#signal 2
amp2=0.1
freq2=20.0 #hz

t=arange(0.0,10.0,.01)

signal1=amp1*sin(freq1*t + pi/2
                 )
signal2=amp2*sin(t*freq2)
conv=signal.convolve(signal1,signal2,mode='full')
a=zeros(shape=(1000,))
a=conv[999:1999]

plt.subplot(3,1,1)
plt.plot(t,signal1)
plt.grid(True)

plt.subplot(3,1,2)
plt.plot(t,signal2)
plt.grid(True)

plt.subplot(3,1,3)
plt.plot(t,a)
plt.grid(True)

plt.show()