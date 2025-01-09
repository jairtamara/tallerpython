nombres = ["jair","daniel","david","henry","miguel"]

for i in nombres:
    nombre_posicion = nombres.index(i) + 1
    print(f"hola  {i} estas en la posicion {nombre_posicion}")
  
  
#######  
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

for a in  alumnos_clase:
    print(f"Hola {a}")

################
#suma de numeros de una lista 
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0

for n in lista_numeros:
    suma_numeros = suma_numeros + n
print(suma_numeros)    

#Suma de numeros pares e inpares por separado
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares =0

for n in lista_numeros:
    if n % 2 == 0: 
        suma_pares = suma_pares + n
    else:
        suma_impares = suma_impares + n

print(f"la suma de numeros pares es {suma_pares} la suma de numeros impares es {suma_impares}")        
