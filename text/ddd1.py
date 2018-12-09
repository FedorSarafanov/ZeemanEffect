from math import pi 
import numpy as np 
c=3e8
l0=585.25*10**-9 
h=4*10**-3 
dRm=5 
dRl=28 
mu0=9.27*10**(-21) 

def H(x): 
	a= 6581 
	b=0.04164 
	c= -7785 
	d= -1.144 
	H=a*np.exp(b*x)+c*np.exp(d*x) 
	return H 

dl=l0**2/2/h*dRm/dRl 
l1=l0-dl 
l2=l0+dl 
omega=2*pi*c*(1/l1-1/l2) 
HH=H(1.43)
# domega=2*pi*c/dl 
print('dl=',dl,'м') 
print('domega=',omega) 
plank=6.626070*10**(-27)/2/pi #эрг*с 
g=omega*plank/mu0/HH 
# print(H(1.4))
print('g=',g)

print('наше e/m =',2*3e10*omega/(HH))
e=4.8e-10
m=9.10938356e-28
print('ненаше e/m =',e/m)