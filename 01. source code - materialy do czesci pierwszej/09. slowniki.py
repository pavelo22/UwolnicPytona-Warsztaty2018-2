
slownik = { 'klucz':'gerda', 0:'wartosc dla klucza zero' }
print('Liczba elementów:', len(slownik))
print('-'*30)
print('Element pod kluczem 0 (nie mylić z indeksem!):', slownik[0])
print('-'*30)
print('Cały słownik:', slownik)
print('-'*30)

for klucz, wartosc in slownik.items():
    print("klucz: {}, wartosc: {}".format(klucz, wartosc))
print('-'*30)

print('Same klucze')
for klucz in slownik.keys():
    print(klucz)
print('-'*30)

print('Same wartości')
for wartosc in slownik.values():
    print(wartosc)
print('-'*30)

# tak dodajemy parę klucz:wartość do słownika
slownik.update({'telefon':'3434-3434-32'})
print(slownik)

# usuwamy klucz
klucz = 'klucz'
if klucz in slownik:
    slownik.pop(klucz)
print(slownik)