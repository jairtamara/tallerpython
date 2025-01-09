#lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

#for i,n  in enumerate(lista_nombres):
 #   print(f'{n} se encuentra en el índice {i}')

##############
# recorer un String

lista_indices = list("Python")

#for i , c in list(enumerate(lista_indices)):
   ## print( i , c)
   # print(type(lista_indices))
    
####
# imprimir solo los nombres que empiezen por la letr M
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]


for indice,nombre in enumerate(lista_nombres):
   
    if nombre.startswith("M"):
        print(indice,nombre)
          
    