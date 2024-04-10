#operaciones entre arreglos 

import numpy as np 
a= np.array([-1,10,15,20,25])
print(a)

b=np.array([3,4,7,9,56])
print(b)

c= a+b # se puede sumar +, multiplicar *,restar -, dividir / 
print(c)

d=b**2 #los astericos represtan los exponentes 
print(d)
f=np.sin(b)
print(f)

g=(b<2)
print(g)

h=a@b #@ es para hacer el producto punto 
print(h)

b=b+1 #aqui estamos modificando b
print (b)

#la clase ndarray define:

z=a.sum() # suma todos los elementos del arreglo
print(z)

l= a.min() #saca el numero menor del arreglo 
print(l)

m= a.mean() # saca la media del arreglo.
print(m)

y= np.array([[5,10,-1,20,25], [3,6,4,8,12]])
print(y)

print(y.sum(axis=0))

print(np.sqrt(y))

print(np.exp(y))

a= np.array([[5,10,-1,20,25], [3,6,4,8,12]])
b= np.array([[10,2,3,4,5], [6,7,8,9,10]])

print(a)
print(b)

c= np.add(a,b)
print(c)

u= np.array([7.4,8.9,6.7])
print(a.round(decimals=2))


 
