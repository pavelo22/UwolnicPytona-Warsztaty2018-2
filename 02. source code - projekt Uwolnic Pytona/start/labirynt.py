class Labirynt:
    def __init__(self):
        self.plansza = list()
        self.wysokosc = None
        self.szerokosc = None
        self.start = (0, 0)
        self.stop = (0, 0)
        self.krok = None

    def zaladuj_mape(self, nazwa_pliku="labirynt-maly"):
        """
        Załaduj plik mapy z dysku
        Utwórz strukturę mapy w pamięci (self.plansza)
        Ustal rozmiary (self.szerokość i self.wysokość)
        """
        pass

    def wydrukuj_plansze(self):
        pass

    def znajdz_start_i_stop(self):
        """
        Znajdź współrzędne początkowego i końcowego punktu w labiryncie (self.start i self.stop)
        """
        pass

    def zbadaj_komorke(self, y, x, krok):
        """
        Zbadaj komórkę - którzy sąsiedzi to kandydaci do następnego ruchu?
        Ustaw wartość dla kandydata
        Zbadaj czy pyton został odnaleziony
        Zwróć zmienne kandydaci i znaleziony
        """

        kandydaci = list()
        znaleziony = False

        return kandydaci, znaleziony

    def wylewanie_wody(self):
        self.znajdz_start_i_stop()
        if self.stop == self.start:
            print("Brak danych dla metody 'wylewanie_wody()")
            return

        self.plansza[self.start[0]][self.start[1]] = '0'

        lista_pozycji = list()
        lista_pozycji.append(self.start)

        self.krok = 1
        znaleziony = False
        while not znaleziony:
            lista_kandydatow = list()
            for element in lista_pozycji:
                y = element[0]
                x = element[1]

                kandydaci, znaleziony = self.zbadaj_komorke(y, x, self.krok)

                if znaleziony:
                    break
                if len(kandydaci) > 0:
                    lista_kandydatow.extend(kandydaci)

            self.krok += 1
            lista_pozycji = list(lista_kandydatow)

    def odtworz_sciezke(self):
        """
        Wracamy po śladach w wodzie
        """
        if self.stop == self.start:
            print("Brak danych dla metody 'odtworz_sciezke()'")
            return

        y = self.stop[0]
        x = self.stop[1]

        while self.krok >= 0:
            self.plansza[y][x] = '*'
            if self.plansza[y - 1][x] == str(self.krok):
                y = y - 1
            elif self.plansza[y + 1][x] == str(self.krok):
                y = y + 1
            elif self.plansza[y][x - 1] == str(self.krok):
                x = x - 1
            elif self.plansza[y][x + 1] == str(self.krok):
                x = x + 1

            self.krok = self.krok - 1

        """
        Czyścimy planszę z pozostałości (mylne tropy)
        """

        for y in range(self.wysokosc):
            for x in range(self.szerokosc):
                if self.plansza[y][x] not in (' ', '*', '#', 'P', 'S', '0'):
                    self.plansza[y][x] = ' '


if __name__ == '__main__':
    plansza = Labirynt()
    plansza.zaladuj_mape()
    plansza.wydrukuj_plansze()

    print()

    plansza.wylewanie_wody()
    plansza.odtworz_sciezke()
    plansza.wydrukuj_plansze()
