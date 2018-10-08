# możemy mieć kilka argumentów wymaganych oraz kilka domyślnych
# argumenty domyślne muszą być podane po argumentach wymaganych
def wypisz_dane(imie, nazwisko, kurs="Python", ilosc_dni=15):
    print(imie, nazwisko, kurs, ilosc_dni)

# argumenty wymagane (inaczej: pozycyjne) muszą być podane
wypisz_dane("Tadeusz", "K")

# tutaj podajemy wszystkie wartości argumentów
wypisz_dane("Jan", "Kowalski", "Java", 80)

# kolejność argumentów można zmieniać, ale trzeba użyć nazw zmiennych
wypisz_dane("Gosia", "Nowak", ilosc_dni=30, kurs="JavaScript")
wypisz_dane(kurs="Java", imie="Gosia", ilosc_dni=23, nazwisko="Kowalska")