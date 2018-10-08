sciezka = "08. listy.py"

# otwieramy plik w trybie tekstowym, tylko do odczytu
plik = open(sciezka, 'r')

# read() czyta zawartość, od miejsca w którym jest kursor
# aż do końca pliku
tresc = plik.read()
print(tresc)

# pamiętaj o zamykaniu pliku
plik.close()
