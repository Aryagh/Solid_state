import numpy as np
import matplotlib.pyplot as plt
a = 1
c = 2*np.pi/a

def e(kx,ky,kz):
    return ((kx+Gx)**2 + (ky+Gy)**2 + (kz+Gz)**2)/(c**2)

for h in range(-2,2):
    for k in range(-2,2):
        for l in range(-2,2):
            Gx,Gy,Gz = c*(-h+k+l),c*(h-k+l),c*(h+k-l)
#             Gx,Gy,Gz = c*(h+l/2),c*(k+l/2),c*(l/2)
            E = np.zeros(600)
            
            # GAMMA X
            for i,mu in enumerate(np.arange(0,1,.01)):
                E[i] = e(mu*c,0,0)

            # X W
            for i,mu in enumerate(np.arange(0,1,.01)):
                E[i+100] = e(c,mu*c/2,0)

            # W L
            for i,mu in enumerate(np.arange(0,1,.01)):
                E[i+200] = e(c - mu*c/2,c/2,mu*c/2)

            # L GAMMA
            for i,mu in enumerate(np.arange(0,1,.01)):
                E[i+300] = e(c/2 - mu*c/2,c/2 - mu*c/2,c/2 - mu*c/2)

            # GAMMA K
            for i,mu in enumerate(np.arange(0,1,.01)):
                E[i+400] = e(mu*c*3/4,mu*c*3/4,0)

            # K X
            for i,mu in enumerate(np.arange(0,1,.01)):
                E[i+500] = e(c*3/4 + mu*c/4,c*3/4 - mu*c*3/4,0)

            plt.plot(E,color='k')

x = np.array([0,100,200,300,400,500,600])
my_xticks = ['$\Gamma$','X','W','L','$\Gamma$','K','X']
plt.xticks(x, my_xticks)
plt.ylabel('$\epsilon / \epsilon_x$  ')
plt.title('Band Structure Of FCC Lattice')
plt.ylim(0,5)
plt.show()
