import tkinter as tk
from labirynt import Labirynt

# Klasa odpowiedzialna za sterowanie aplikacją
class Window:
    def __init__(self):
        self.labirynt = Labirynt()
        self.labirynt.zaladuj_mape('labirynt')

        self.plansza = self.labirynt.plansza
        self.liczba_wierszy = self.labirynt.wysokosc
        self.liczba_kolumn = self.labirynt.szerokosc

        tytul = 'Uwolnić Pytona'
        self.rozmiar_komorki = 20

        self.szerokosc = self.liczba_kolumn * self.rozmiar_komorki
        self.wysokosc = self.liczba_wierszy * self.rozmiar_komorki

        self.master = tk.Tk()
        self.master.title(tytul)

        self.przygotuj_uklad_obiektow()
        self.przygotuj_przyciski()

    def przygotuj_uklad_obiektow(self):
        # Utworzenie głównego ekranu
        self.frame = tk.Frame(self.master, width=self.szerokosc, height=self.wysokosc)
        self.frame.pack()

        # Utworzenie siatki
        self.canvas = CanvasGrid(self.frame, width=self.szerokosc + self.rozmiar_komorki,
                                 height=self.wysokosc + self.rozmiar_komorki)
        self.canvas.plansza = self.plansza
        self.canvas.step = self.rozmiar_komorki
        self.canvas.size_x = self.liczba_kolumn
        self.canvas.size_y = self.liczba_wierszy
        self.canvas.fill_grid()
        self.canvas.pack()

    def przygotuj_przyciski(self):
        # Utworzenie przycisku start i przypisanie akcji
        self.wyrysuj_button = tk.Button(self.master, text='Wyrysuj mapkę', command=self.wyrysuj_labirynt)
        self.wyrysuj_button.pack()

        # Utworzenie przycisku "Znajdź Pytona - pokaż ścieżkę" i przypisanie akcji
        self.ucieczka_button = tk.Button(self.master, text='Znajdź Pytona - pokaż ścieżkę',
                                         command=self.znajdz_i_narysuj_sciezke)
        self.ucieczka_button.config(state="disabled")
        self.ucieczka_button.pack()

        # # Utworzenie przycisku "Znajdź Pytona - pokaż postępy" i przypisanie akcji
        self.pozar_button = tk.Button(self.master, text='Znajdź Pytona - pokaż postepy',
                                      command=self.znajdz_i_narysuj_postepy)
        self.pozar_button.config(state="disabled")
        self.pozar_button.pack()

    def wyrysuj_labirynt(self):
        # blokowanie przycisku 'wyrysuj'
        self.wyrysuj_button.config(state="disabled")

        # odblokowanie pozostałych przycisków
        self.ucieczka_button.config(state="active")
        self.pozar_button.config(state="active")
        self.update()

    def znajdz_i_narysuj_sciezke(self):
        # blokowanie pozostałych przycisków
        self.ucieczka_button.config(state="disabled")
        self.pozar_button.config(state="disabled")
        # wylanie wody
        self.labirynt.wylewanie_wody()
        # odtworzenie najkrótszej ścieżki
        self.labirynt.odtworz_sciezke()
        self.update()

    def znajdz_i_narysuj_postepy(self):
        self.ucieczka_button.config(state="disabled")
        self.pozar_button.config(state="disabled")
        self.labirynt.wylewanie_wody()
        self.update()
        photo = tk.PhotoImage(file="gad.gif")
        label = tk.Label(image = photo)
        label.image = photo
        label.pack()

    def update(self):
        self.canvas.paint_grid()

# Klasa pomocnicza, reprezentująca pola w labiryncie
class CanvasGrid(tk.Canvas):

    # marginesy
    START_X = 10
    START_Y = 10

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.plansza = None
        self.size_x = 0
        self.size_y = 0
        self.step = 0
        self.grid = []

    # Utworzenie siatki z kwadratów
    def fill_grid(self, color='white'):
        self.size_y = len(self.plansza)
        self.size_x = len(self.plansza[0])

        y = CanvasGrid.START_Y

        for wiersz in range(self.size_y):
            x = CanvasGrid.START_X
            # utworzenie wiersza
            self.grid.append([])

            # utworzenie komórek w wierszu
            for kolumna in range(self.size_x):
                rect = self.create_rectangle(x, y, x + self.step, y + self.step, fill=color)
                self.grid[wiersz].append(rect)
                x += self.step
            y += self.step

    def paint_grid(self):
        """
        Wyrysowanie aktualnego stanu labiryntu
        """
        kolory = {' ': 'white',
                  '#': 'gray',
                  'P': 'yellow',
                  'S': 'red',
                  '*': 'blue'
                  }

        # Dla każdej komórki na planszy...
        for row in range(self.size_y):
            for column in range(self.size_x):
                value = self.plansza[row][column]
                if value in kolory:
                    color = kolory[value]
                else:
                    wartosc = hex(int(value))[2:].zfill(2)

                    color = '#' + '0000' + wartosc
                # ... ustaw jej kolor
                self.itemconfig(self.grid[row][column], fill=color)


if __name__ == '__main__':
    # Utworzenie okna
    okno_glowne = Window()

    # Główna pętla aplikacji
    okno_glowne.master.mainloop()
