valores = [1, 2, 3, 4, 5, 6, 9.5]

#crea una lista que tenga el valor de los numeros  de la lista y elevalo al cuadrado
valores_cuadrado = [n * n for n in valores]
#print(valores_cuadrado)


#Crea una lista valores_pares formada por los números de la lista valores que (¡adivinaste!) sean pares.

valores = [1, 2, 3, 4, 5, 6, 9.5] 
valores_pares = [n for n in valores if n % 2 ==0  ]
#print(valores_pares) 

# ejerccion de pasar de Fahrenheit a una nueva lista con valores Celsius
# formula °C = (°F - 32) * (5/9)

temperatura_fahrenheit = [32, 212, 275]

grados_celsius = [(n-32)*(5/9) for n  in temperatura_fahrenheit ]
print(grados_celsius)
