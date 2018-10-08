# sprawdź czy liczba jest podzielna przez 3, 5, 7

# przyjmij dane
dane = input("Podaj liczbę: ")

# sprawdzamy czy zawiera tylko cyfry
if dane.isdigit():
    liczba = int(dane)

    # sprawdzamy czy podzielna przez 3
    if liczba % 3 == 0:
        # napisz że podzielna przez 3
        print("Liczba {} jest podzielna przez 3".format(liczba))
    # sprawdzamy czy jest podzielna przez 5
    if liczba % 5 == 0:
        # napisz że jest podzielna przez 5
        print("Liczba {} jest podzielna przez 5".format(liczba))
    # sprawdzamy czy jest podzielna przez 7
    if liczba % 7 == 0:
        # napisz że podzielna przez 7 
        print("Liczba {} jest podzielna przez 7".format(liczba))
