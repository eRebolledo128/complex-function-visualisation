import numpy as np
import matplotlib.pyplot as plt

size = 1.5

# creates x and y
x = np.linspace(-size,size,1000)
y = np.linspace(-size,size,1000)

# creates argand plane
xy, yx = np.meshgrid(x,y)
z = xy + 1j*yx
print("argand plane\n",z)

# applies function
#### change function ####
f = 0
for n in range(20):
    f = f + z**2**n
print("function\n",f)

u = f.real
v = f.imag

# modulus and argument
mod = np.sqrt(u**2 + v**2)
print("modulus\n",mod)

arg = np.arctan(v/u)
print("argument\n",arg)

plt.imshow(arg, cmap='hsv')
plt.show()
