c=3e8
l0=607.4*10**-9
pi=3.14152695
h=4*10**-4
dRm=0.06
dRl=0.286
hs=1.054e-27
mu0=9.27e-21
dl=l0**2/2/h*dRm/dRl
# print(dl)


l1=l0-dl
l2=l0+dl
omega=2*pi*c*(1/l1-1/l2)
Hsi=5500/10000

print(1.5*mu0*Hsi/hs)
print(omega)
