#from  random import randint
from  random import *

aleatorio = round(uniform(1,5),1)
#print(aleatorio)

###########################
#aleatorio de 1 a 10 
aleatorio = randint(1,10)
#print(aleatorio)


##############

#Implementa la función random() de la librería random que te permita obtener un número decimal entre 0 y 1, y almacena dicho valor en una variable llamada aleatorio

aleatorio =  random()
print(aleatorio)

#Utiliza el método choice() de la librería random para obtener un elemento al azar de la lista de nombres a continuación, y almacena el nombre escogido en una variable llamada sorteo.

nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]

sorteo = choice(nombres)
print(sorteo)