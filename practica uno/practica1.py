import numpy as np;
import matplotlib.pyplot as plt; 

#### Ejercicio 4

coef = np.array([[1,1,1],[4,2,1],[9,3,1]])
coef_res = np.array([1,2,0])
res = np.linalg.solve(coef,coef_res)

print (res)

xx = np.array([1,2,3])
yy = np.array([1,2,0])

x = np.linspace(0,4,100)
f = lambda t:res[0]*t **2 + res[1]*t + res[2]
plt.plot(xx,yy,'*')
plt.plot(x,f(x))
plt.show()








