#a = 5
#b = 2.7
#c = 'Hola mor' ##Se puede hacer con los dos
#texto1 = "Esto es un texto largo"
#texto2 = 'Esto es un texto no tan largo'
#texto3 = """
#vio que lindo
#"""
#print ("LA variable a es: ",type(a))
#print ("La variable b es de tipo {}".format (type(b)))
#print(f"La variable c es de tipo{type(c)}")
#nombre = input("Por favor ingrese su nombre: ")
#print (f"Hola {nombre}, gusto conocerlo")
#num1 = int (input ("Ingrese el número 1: "))
#num2 = int (input ("Ingrese el número 2: "))
#suma = (num1 + num2)
#print (f"La suma es = {suma}")
#find
# saludo = "Hola, bienvenido"
# # v1 = saludo.find("a")
# # print(f"\tLa a se encuentra en posición: {v1}")
# # print ("*"*64)
# # print ("Los metodos asociados a los Strings son: ")
# # print (dir(saludo))
# # print("\n")
# saludo_upper =saludo.upper()
# print (f"{saludo}\t {saludo_upper}")
# #4 split
# print("*"*64)
# texto = "Hoy hace mucho calor"
# texto_split= texto.split(" ")
# unido= ("2").join(texto_split)
# print(f"\Texto original es = {texto}")
# print(f"\Texto original es = {texto_split}")
# print(f"texto unido = {unido}")
# a = 2
# b = 5
# if 1==1:
#     print ("SI")
# else: 
#     print ("NO")
# ###### elseif ####
# if a<b:
#     print (f"{a} es menor que {b}")
# elif b==a:
#     print (f"{a} es igual que {b}")
# else:
#     print (f"{a} mayor que {b}")
###For loop####
#               #start, stop, step 
# for i in range(2,11,2):
#     print(i)
# for l in 'texto':
#     print(l)
# for j in range (1):
#     for k in 'hola':
#         print (j,k)
############### WHILE LOOP ############
######## Lists #######
list=[]
lista=['ole', 2, 3,'vio']
#### Slicing ####
nueva_lista = lista[2:]#Si no especifico nada en el final está seguira hasta el fin de la lista y si no especifico nada cogerá todo
print (f"Lista [0:3] = {lista[0:3]}")
# print (f"{dir(list)}")
###### Lista anidadas ############
lista3=['nice', lista, 100, 54]
print (lista3)
elemento= lista3[1][2]
print (f"elemento = {elemento}")
