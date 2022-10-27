# DICCIONARIOS

# MANIPULACIÓN: ejercicio que vamos a realizar referente a diccionarios será crear uno y mostrar algunos elementos del mismo. Para acceder a los elementos del diccionario deberás de utilizar la clave del elemento. El código fuente es el siguiente:


# 1. Consiste en crear un diccionario y mostrar algunos elementos del mismo, accediendo a ellos usando la clave del elemento.
# print ( "------Ejercicio 1-------" )
diassemanaingles = {"Lunes":"Monday",
                    "Martes" : "Tuesday",
                    "Miercoles": "Wednesday",
                    "Jueves": "Thursday",
                    "Viernes": "Friday"}
print(diassemanaingles)
diassemanaingles["Sabado"] = "Saturday"
print(diassemanaingles)
diassemanaingles["Domingo"] = "Sunday"
print(diassemanaingles)
diassemanaingles["Lunes"] = "MondayBORRAR"
print(diassemanaingles)

# 2

diassemanaingles = {"Lunes" : "Monday",
                    "Martes" :"Tuesday",
                    "Jueves": "Thursday",
                    "Miercoles": "Wednesday", 
                    "Viernes": "Friday"}
print("Número de elementos del diccionario: ",len(diassemanaingles)) 
print("Elemento mayor del diccionario: ",max(diassemanaingles)) 
print("Elemento menor del diccionario: ",min (diassemanaingles))