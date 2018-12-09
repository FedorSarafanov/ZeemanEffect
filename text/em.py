from math import pi
e=1.60217662e-19
m=9.10938356e-31
print(e/m)

H=5500 #ersted
Hsi=H/10**4 #Tl

c=3e8 #m/s

Omega=e*Hsi/(2*m*c)
print(Omega)
dl=2*pi*c/Omega
print(dl)