# EJERCICIOS TUPLAS

# Cómo definir una tupla y cómo acceder a sus elementos.

from pickle import TUPLE1


tupla = ('Casa', '2',345, 'Perro',99) 

print("Elementos de la tupla: ", tupla)

print("Elemento de la posición 0: ", tupla[0])

print("Elemento de la posición 1: ", tupla[1])

print("Elemento de la posición 2: ", tupla [2])

print("Elemento de la posición 3: ", tupla [3])

print("Elemento de la posición 4: ", tupla[4])

# Funciones asociadas al tipo de dato

# count: cuenta el número de veces que aparece el elemento indicado como parámetro dentro de la tupla.
# index: devuelve la posición de la primera aparición de izquierda a derecha en la tupla del elemento pasado como parámetro.

tupla = ('Casa', '2',99,345, 'Perro',99) 

print("Tupla elementos: ", tupla)

print("Número de elementos 99: ", tuple.count(99))

print("Posición ocupada por el elemento Perro: ", tuple.index("Perro"))

# Extraer pociones de ellas en otra tupla nueva

#Tupla[n:m] La instrucción extraerá una nueva tupla que empezará en el indice ny terminará en el m-1.

tupla (1,2,3,4,5,6,7,8,9)

print(tupla)

print(tupla[4:9]) 

print(tupla[:3])

print(tupla[2:])

#  funcion tupla concatenada "+" :  esta función se llama len(Tupla) y devuelve un entero que indica el número de elementos que la componen. Se utiliza de la siguiente manera:

tupla1= (29, "Televisión", 8763)
tupla2 =(1,2,3, "Videojuego") 
print("Número elementos de tupla1: ",len (tupla1)) 
print("Tupla1: ", tupla1) 
print("Numero elementos de tupla2: ", len(tupla2)) 
print("Tupla2: ", tupla2) 
tuplaconcatenada =tupla1+ tupla2 
print("Numero elementos de tuplaconcatenada: ",len (tuplaconcatenada)) 
print("tuplaconcatenada: ", tuplaconcatenada)

# funcion Tupla Resultante "*" : La tupla resultante de la multiplicación será una tupla compuesta por tantas veces la Tupla como valor tenga el número entero.

tupla = (1,2,3,4,5,6,7,8,9,0) 
print(tupla) 
tuplaresultante = tupla* 4 
print(tuplaresultante)