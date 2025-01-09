# proyecto de adivinar  un numero aleatorio

nombre =  input("Por favor ingresa tu nombre: ")

print(f"Hola {nombre} tenemos un juego, debes adivinar un numero de 1 a 100  tienes 8 intentos. ")



numero_secreto = 20
turnos = 8


while turnos > 0:
    numero_usuario = int(input("por favor ingresa tu numero para participar: "))        
    if numero_usuario <= 0 or numero_usuario >100 :
        print("numero no permitido")
    elif numero_usuario == numero_secreto:
        print(f"!!!!!!!!!!!haz acertado el numero secreto {numero_secreto} ingresaste {numero_usuario}, te quedaban {turnos} turnos")    
    elif  numero_usuario < numero_secreto:
        turnos -= 1
        print(f"el numero ingresado es menor a numero secreto te quedan {turnos} turnos")
    elif  numero_usuario > numero_secreto:
        turnos -= 1
        print(f"el numero ingresado es mayor a numero secreto te quedan {turnos} turnos")
    elif numero_usuario == numero_secreto:
        print(f"!!!!!!!!!!!haz acertado el numero secreto {numero_secreto} ingresaste {numero_usuario}, te quedaban {turnos} turnos")
    else:
        print("Ingresaste un caracter no valido")
print(f"No has logrado adivinar le numero mejor suerte para la proxima numero de intentos {turnos}")        
        
                   
        
    
    
     
