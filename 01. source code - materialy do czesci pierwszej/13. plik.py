# otwieram swoj plik

sciezka = "10. petla while.py"
plik = open(sciezka)

# czytamy jedną linijkę z pliku
linijka = plik.readline()

print(linijka)

# pamietamy o zamykaniu pliku
plik.close()