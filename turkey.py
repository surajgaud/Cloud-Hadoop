__author__ = 'Suraj'

import numpy as np
from numpy import *
from scipy import signal
import matplotlib.pyplot as plt

#signal 1
A1 = 10.0
F1 = 2.0

#signal 2
A2 = 0.1
F2 = 20.0

t = np.arange(0.0,10.0,0.01)

S1 = A1*np.sin(F1,t)
S2 = A2*np.sin(F2,t)
#w1 = (2.*np.pi*F1)   #omega 1
#w2 = (2.*np.pi*F2)   #omega 2
#S1 = A1*np.sin(w1*t+np.pi/2) #signal 1
#S2 = A2*np.sin(w2*t+np.pi/2) #signal 3
S3 = signal.convolve(S1,S2,mode='same') # convolved signal 3
a=zeros(shape=(1000,))
a=S3[999:1000]
print len(S1)
print len(S2)


plt.subplot(3,1,1)
plt.plot(t,S1)
plt.subplot(3,1,2)
plt.plot(t,S2)
plt.subplot(3,1,3)
plt.plot(t,S3)
plt.show()


