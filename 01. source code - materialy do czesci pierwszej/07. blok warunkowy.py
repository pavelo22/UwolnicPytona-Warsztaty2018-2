# podaj ocenę na podstawie progu procentowego
# 5 od 90%, 4+ od 80, 4 od 70, 3+ od 60, 3 od 50

# przyjmij dane od uzytkownika
# zweryfikuj dane - czy liczby
dane = str(input("Podaj procent: "))

if dane.isdigit():
    procent = int(dane)

    if procent >= 90:
        print("5")
    elif procent >= 80:
        print("4+")
    elif procent >= 70:
        print("4")
    elif procent >= 60:
        print("3+")
    elif procent >= 50:
        print("3")
    # jeśli mniej niż 50 to napisz "Siadaj Pała!"
    else:
        print("Siadaj pała!")

else:
    print("Podaj tylko liczbę!")
