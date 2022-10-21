# EJERCICIOS LISTAS

# Métodos propios

lista = [45, 32,3,78]
print("Lista original: ", lista)
# funcion apppend: añade un elemento a la lista
lista.append(995)
lista.append(7)
print("Lista despues de usar append:", lista)
# Funcion sort: ordena la lista 
lista.sort
print("Lista ordenada: ", lista)
# Funcion reverse: invierte el orden de la lista
lista.reverse()
print("Lista al revés: ", lista)
# Funcion extend:
lista_extend =[1,5,87,45]
lista.extend(lista_extend)
print("Lista despues de extend:", lista)
# Funcióń count:cuenta el numero de veces que aparece el elemento indicado como parametro dentro de la lista
print("Numero de elementos 45:", lista.count(45))
# Funcion insert: añade el elemento pasado como parámetro a la lista en la posición indicada tambien por parametro
lista.insert(4,111)
print("Lisra despues de insert:", lista)
# Funcion remove: elimina la primera ocurrencia empezando por la izquierda de la lista del elemento indicado como parametro.
lista.remove(45)
print("Lista despues de remove:", lista)
# Funcion index: devuelve la posicion de la primera ocurrencia de izquierda a derecha en la lista, del elemento pasado como parámetro
print("Posicion del elemento 111:",lista.index(111))
# Funcion pop: Elimina el ultimo elemento de la lista y lo devuelve como resultado de la operaciion.
lista.pop()
print("Lista despues de pop:", lista)
# Función clear: elimina todos los elementos de la lista
lista.clear()
print("Lista despues de clear:", lista)