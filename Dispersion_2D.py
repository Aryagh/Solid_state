from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

a = 1
l = np.pi/a
w = np.zeros([100,100])
for i,kx in  enumerate(np.arange(-l,l,l/100*2)):
    for j,ky in enumerate(np.arange(-l,l,l/100*2)):
        w[i,j] = np.sqrt(2 - np.cos(kx*a) - np.cos(ky*a))

x = np.arange(-l,l,l/100*2)
y = np.arange(-l,l,l/100*2)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(x,y,w, 100)
ax.set_xlabel('$K_x$');
ax.set_ylabel('$K_y$');
ax.set_zlabel('$\omega$');

plt.show()
