# deklarowanie list
lista = []
print(lista)

listaX = list() #to samo co powyżej
print(listaX)

print("-"*20)

lista1 = [2, 3, 4, 5, 6, 7, 8]
print(lista1)

lista2 = ["kwiatek", "woda", "doniczka", "ziemia"]
print(lista2)

zakres = range(2,5)
print(zakres)

lista3 = list(zakres)
print(lista3)

# w listach mogą być różne elementy
lista4 = ["zero", 1, 2.0, range(5)]

print("-"*20)
print("Zawartość listy przed dodaniem elementu")
print(lista2)
lista2.append("grabki")
print("Zawartość listy po dodaniu elementu")
print(lista2)

