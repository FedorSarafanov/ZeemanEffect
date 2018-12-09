c=3e8
l0=585.25*10**-9
pi=3.14159265
h=4*10**-3
dRm=5
dRl=23

dl=l0**2/2/h*dRm/dRl
print(dl)
l1=l0-dl
l2=l0+dl
omega=2*pi*c*(1/l1-1/l2)
print('omefa',omega)
Hsi=5525/10000
print(omega*2*c/Hsi)

k=(0.04+0.05+0.08+0.07)/4
d=(1.92-1.65+1.86-1.58+1.81-1.50)/3
# print(k,d)