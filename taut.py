import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filename = 'Book1.xlsx'
data = pd.read_excel(filename)
data = data[data.WL >= 300]
data = data[data.WL <= 900]
data = data.to_numpy()
x = data[:,0]
y = data[:,1]

ax1 = plt.subplot(121)
ax2 = plt.subplot(122)

ax1.plot(x,y,'.')
ax1.set_ylabel('a')
ax1.set_xlabel('nm')

# max
arg = data[:,1].argmax()
print('max: ',data[arg,0],'nm')

# Taut Plot
h_bar = 4.1e-15
C = 3*1e8
n = len(x)
new_x = np.dot(h_bar*1e9*C,np.ones(n)/x)
new_y = np.sqrt(y*new_x)

df1 = np.gradient(new_y,new_x)
df2 = np.gradient(df1,new_x)
p = abs(df2).argmin()


ax2.plot(new_x,new_y,'.')
b = new_x[p] - new_y[p] / df1[p]
print(b,'ev')
ax2.plot([b,new_x[p]],[0,new_y[p]])
ax2.set_ylabel('$(ahv)^2$')
ax2.set_xlabel('$hv$')
plt.title('Tauk Plot')
plt.show()
