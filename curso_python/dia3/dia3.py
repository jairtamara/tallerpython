#ingresando texto
texto = input("ingresa tu texto: ")
texto = texto.lower()
#lista de letras a buscar 
letras = []
#llenando lista letra a buscar
letras.append(input("ingresa la primera letra: ").lower())   
letras.append(input("ingresa la primera letra:  ").lower())   
letras.append(input("ingresa la primera letra: ").lower())   

print("\n")
print("Cantidad de letras")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Hemos encontrado la letra '{letras[0]}' repetidas {cantidad_letras1} veces ")
print(f"Hemos encontrado la letra '{letras[1]}' repetidas {cantidad_letras2} veces ")
print(f"Hemos encontrado la letra '{letras[2]}' repetidas {cantidad_letras3} veces ")


#cantidad de palabras
palabras = texto.split()
print("\n")

print("CANTIDAD DE PALABRAS")

print(f"hemos encontrado {len(palabras)} palabras en tu texto")


print("\n")

print("letras de inicio y fin")


letras_inicio = texto[0]
letras_fin = texto[-1]

print(f"la letra inicio es '{letras_inicio}' y letra final es  '{letras_fin}'")

print("\n")

print("Texto reverse")

palabras.reverse()

texto_invertido = ' '.join(palabras)

print(f"El texto invertido es : '{texto_invertido}' ")

print("\n")

print("Buscando la pabra python")

palabra_python = "python" in texto
dic = {True:"si",False:"no"}

print(f"la palabra python '{dic[palabra_python]}' encuentra en el texto")