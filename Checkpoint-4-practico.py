#Ejercicio 1

lista = [1, 2, 3, "Python"]
print("List:", lista)

tupla = (10, 20, 30, "Barcelona")
print("Tupla:", tupla)

precio_unitario = 1.2  
cantidad = 3   
iva = 1.21        

float = precio_unitario * cantidad * iva
print("Float:" , float)

entero = 42
print("Integer:", entero)

from decimal import Decimal
precio_unitario_decimal = Decimal("1.2")
cantidad_decimal = Decimal("3")
iva_decimal = Decimal(1.21)

total_decimal = precio_unitario_decimal * cantidad_decimal * iva_decimal
print("Decimal:" , total_decimal)  

diccionario = {
    "nombre": "Brian",
    "edad": 25,
    "ocupacion": "Desarrollador",
}
print("Dictionary:", diccionario)

print()

#Ejercicio 2
import math

print(float)
float_redondeado_hacia_arriba = math.ceil(4.356)

print(float_redondeado_hacia_arriba)

print()

#Ejercicio 3
print(float)
Raiz_cuadrada_de_float = math.sqrt(4.356)

print(Raiz_cuadrada_de_float)

print()

#Ejercicio 4
Primer_elemento_de_diccionario = list(diccionario.items())[0]

print(Primer_elemento_de_diccionario)

print()

#Ejercicio 5
segundo_elemento_de_tupla = tupla[1]

print(segundo_elemento_de_tupla)

print()

#Ejercicio 6

lista.append(True)
print(lista)

print()

#Ejercicio 7
lista[0] = "Madrid"
print(lista)

print()

#Ejercicio 8
lista = [str(x) for x in lista]
lista.sort()
print(lista)

print()

#Ejercicio 9

Elemento_agregar_a_tupla = "Bilbao"
tupla = tupla + (Elemento_agregar_a_tupla,)

print(tupla)
