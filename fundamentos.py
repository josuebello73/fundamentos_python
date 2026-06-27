# variable
#name = "josue"

#last_name = "gonzalez"
# no esciribir en mayusculas, no usar puntos
#print(name)
#print(last_name)

# operadores matematicos
# num1 = 27
# num2 = 3
# suma = num1 + num2
# restas = num1 - num2
# multiplicacion = num1 * num2
# division = num1 / num2

# print(suma)
# print(restas)
# print(multiplicacion)
# print(division)

# print(f"El resultado de la suma es: {suma}")
# print(f"El resultado de la resta es: {restas}")
# print(f"El resultado de la multiplicación es: {multiplicacion}")
# print(f"El resultado de la división es: {division}")

# operadores de comparacion
# Mayor que >
# Menor que <
# Mayor igual >=
# Menor igual <=
# Igual ==
# Diferente !=

# print(f"¿{num1} es mayor que {num2}? {num1 > num2}")
# print(f"¿{num1} es menor o igual que {num2}? {num1 <= num2}")
# print(f"¿{num1} es igual a {num2}? {num1 == num2}")
# print(f"¿{num1} es diferente de {num2}? {num1 != num2}")

# condicionales
# if num1 > num2:
#     print(f"{num1} es mayor que {num2}")

# if num2 > num1:
#     print(f"{num1} es mayor que {num2}")
# else:
#     print(f"{num2} es menor que {num1}")

# condiciones anidados
# edad = 21
# genero = "mujer"
# dia = "jueves"
# if edad >= 18:
#     if genero == "mujer":
#         print("Eres mayor de edad y eres mujer, puedes pasar")
#         if dia == "jueves":
#             print("Hoy es jueves, puedes pasar gratis")
#         else:
#             print("Hoy no es jueves, no puedes pasar gratis")
#     else:
#         print("no puedes pasar, solo mujeres")
# elif edad < 18:
#     print("Eres menor de edad y no puedes pasar")

# if (edad >=18) and (genero == "mujer") and (dia == "jueves") or (dia == "sabado"):
#     print("Eres mayor de edad, eres mujer, puedes pasar gratis")
# else:
#     print("No cumples con los requisitos para pasar gratis")

#condicionales encadenados, para indenticar el fin de semana
# if dia == "viernes":
#     print("Hoy es viernes, el fin de semana esta cerca")
# elif dia == "sabado":
#     print("Hoy es sabado, el fin de semana esta aquí")
# elif dia == "domingo":
#     print("Hoy es domingo, el fin de semana ya terminó")    
# else:
#     print("Hoy es un día de semana, el fin de semana esta lejos")

#juego de piedra, papel o tijera
# player1 = "josue"
# player2 = "maria"   

# piedra = "piedra"
# papel = "papel"
# tijera = "tijera"

# piedra > tijera
# papel > piedra
# tijera > papel

# if player1 == piedra and player2 == tijera:
#     print(f"{player1} gana a {player2}")    
# else:
#     print(f"{player2} gana a {player1}")

# from os import name


name_list = ["josue", "maria", "juan", "pedro", "luis", "ricardo", "andrea",]
# age_list = [21, 22, 23, 24, 25]
# weight_list = [70, 80, 90, 100, 110]

# name_list2 = [
#               "ana",
#               "maria",
#               "juan", 
#               "pedro", 
#               "luis"
# print(len(name_list2))
# print(name_list2)
# print(name_list2[0])
# # print(name_list2[1])
# # print(name_list2[2])
# # print(name_list2[3])
# print(name_list2[4])

# mostrar una slice de la lista
# print(name_list2[0:3]) # muestra los elementos del 1 al 3

#el ultimo elemento de la lista
# print(name_list2[-4]) # muestra el ultimo elemento de la lista

# cambiar el valor de un elemento de la lista
# name_list2[0] = "Queisy"
# print(name_list2)

# # tuplas 
# name_tuple = (
#             "josue",
#             "maria", 
#             "juan",
#             "pedro",
#             "luis",
#     )

# print(name_tuple[0]) # muestra el primer elemento de la tupla

# diccionario
name_dict = {
    "name": "josue",
    "last_name": "gonzalez",
    "age": 21, 
    "weight": 70,
    "favorite_foods": ["pizza", "hamburguesa", "tacos"],
    "address": {
        "street": "calle 123",  
        "city": "Lecheria city"    
    }
}
# print(name_dict["address"]["city"])
# print(name_dict["favorite_foods"][1])


#bucles
# for name in name_list:
#   if name == "josue":
#     print(f"hola te encontre {name}")


for i in range(len(name_list)):
    # print(f"el valor de i es: {i}")
    print (f"hola {name_list[i]}")
