import matplotlib.pyplot as plt
# from functions import parsing
from math import pi
import numpy as np
plt.rc('text', usetex=True)
# plt.rc('text.latex', unicode=True)
plt.rc('text.latex', preamble=[r'\usepackage[utf8x]{inputenc}',
                               r'\usepackage[russian]{babel}',
                               r'\usepackage{amsmath}',
                               r'\usepackage{amssymb}'])

plt.rc('font', family='serif')


def f(x):
  a= 6581
  b=0.04164
  c= -7785
  d= -1.144
  f=a*np.exp(b*x)+c*np.exp(d*x)
  return f



x = np.linspace(0.4, 2.4, 1000)
plt.plot(x, f(x), 'darkblue')
plt.xlabel(r'I, $\text{А}$', fontsize='16')
plt.ylabel(r'H, $\text{Эрстед}$', fontsize='16')
plt.minorticks_on()
plt.grid(which='major', linestyle='-')
plt.grid(which='minor', linestyle=':')
plt.savefig('kurwa.pdf')
plt.show()
