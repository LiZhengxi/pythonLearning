import numpy as np 
import matplotlib.pyplot as plt

a = np.random.rand(3,3).reshape(1,9)


b = np.ones([3,3],dtype=np.float32,).reshape(1,9)

plt.plot(a,b,'rv')

plt.show()
