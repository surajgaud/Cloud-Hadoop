#Suraj Gaud - tan960
#homework - 3


import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

#signal 1
A1 = 10.0
W1 = 2.0

#signal 2
A2 = 0.1
W2 = 20.0

t = np.arange(0.0,10.0,0.01)
#added the phase to match the similar output like the one you gave in the problem
S1 = A1*np.sin(W1*t + np.pi/2) #signal 1
S2 = A2*np.sin(W2*t + np.pi/2) #signal 3
S3 = signal.convolve(S1,S2,mode='full') # convolved signal 3
print len(S1)
print len(S2)
#since the length of both the signals is 1000
convolved = np.delete(S3,np.s_[0:999]) #this is to extract the last
                                       #half of the resulting signal



plt.subplot(3,1,1)
plt.title('Signal 1')
plt.plot(t,S1)
plt.subplot(3,1,2)
plt.title('Signal 2')
plt.plot(t,S2)
plt.subplot(3,1,3)
plt.title('Resulting Signal from convolution')
plt.plot(t,convolved)
plt.tight_layout()

#save the plot as pdf
plt.savefig('suraj_hw3_out.pdf', format='pdf')
