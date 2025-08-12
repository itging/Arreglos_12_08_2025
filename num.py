import numpy as np
vector = np.array([1, 2, 3, 4, 5])
print(vector) #imprimimos el vector 
# quiero imprimir el tercer elemento del vector
print(vector[2]) #imprimimos el tercer elemento del vector 
"""Los vectores no son las listas, no tienen un metodo append() para elementos
no tienen un metodo pop() para eliminar elementos, pero si tienen un metodo reshape() 
para cambiar su forma, adicionalmnte despues creado no se puede cambiar el tamaño del vector"""


vector1 =np.zeros(5)# Creamos un vector de ceros
print(vector1)
vector2 =np.ones(5)
print(vector2)
vector3 = np.arange(1,5,100)
print("rango",vector3)
vector4 =np.linspace(1,10)
print("linspance", vector4)
vector5 =np.random.rand(10)
print("Numero aleatorio: ",vector5)
vector6 =np.random.randint(1,10,10)
print("Vector de numeros aleatorios entre 1 y 10: ", vector6)