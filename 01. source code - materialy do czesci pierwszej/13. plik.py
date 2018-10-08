# otwieram swoj plik

sciezka = "08. listy.py"
plik = open(sciezka)

# czytamy jedną linijkę z pliku
linijka = plik.readline()

print(linijka)

# pamietamy o zamykaniu pliku
plik.close()