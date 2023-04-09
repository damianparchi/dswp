import csv
import os
from datetime import datetime

# wczytanie pliku
with open('lab_06/zamowienia.csv', encoding='utf-8', errors='ignore') as f:
    reader = csv.DictReader(f, delimiter=';')
    rows = list(reader)

# przekształcenia
for row in rows:
    row['Utarg'] = row['Utarg'].replace('zł', '').replace(' ', '').replace(',', '.')
    row['Data zamowienia'] = datetime.strptime(row['Data zamowienia'], '%d.%m.%Y').strftime('%Y-%m-%d')

poland = [row for row in rows if row['Kraj'] == 'Polska']
germany = [row for row in rows if row['Kraj'] == 'Niemcy']

# zapis plików
with open('lab_06/zamowienia_polska.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=reader.fieldnames, delimiter=';')
    writer.writeheader()
    writer.writerows(poland)

with open('lab_06/zamowienia_niemcy.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=reader.fieldnames, delimiter=';')
    writer.writeheader()
    writer.writerows(germany)

# zwrócenie przekształconych danych
modified_rows = poland + germany

#Zadanie 2
def merge_files(file_list, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        header_written = False
        for filename in file_list:
            with open(filename, 'r', encoding='utf-8', errors='ignore') as infile:
                # Pomijamy nagłówek poza pierwszym plikiem
                header = next(infile)
                if not header_written:
                    outfile.write(header)
                    header_written = True

                # Kopiujemy zawartość pliku do wynikowego
                for line in infile:
                    outfile.write(line)

    # Sprawdzamy, czy plik wynikowy został utworzony i zwracamy jego nazwę
    if os.path.isfile(output_file):
        return output_file
    else:
        return None
    
file_list = ['lab_06/zamowienia_polska.csv', 'lab_06/zamowienia_niemcy.csv']
output_file = 'lab_06/połączone_zamowienia.csv'

merged_file = merge_files(file_list, output_file)

if merged_file:
    print(f'Pliki zostały połączone w {merged_file}.')
else:
    print('Nie udało się połączyć plików.')


#Zadanie 3

def n_min_max(numbers: list[float|int], n: int, min_max: bool=False) -> list:
    if type(all(numbers)) != str:
        sort_numbers = numbers.copy()
        sort_numbers.sort(reverse=min_max)
        return sort_numbers[:n]
    else:
        return ["Lista nie zawiera tylko wartości numerycznych"]
    
numbers = [1, 5, 8, -8, 17, 12]
print(n_min_max(numbers , 6, True))
print(n_min_max(numbers , 6))

#Zadanie 4
mieszana = [1, 2.3,"Zbyszek", 5, "Marian", 3.0]
wynik = dict()
for i in mieszana:
    typ_elementu = type(i).__name__
    if typ_elementu not in wynik:
        wynik[typ_elementu] = [i]
    else:
        wynik[typ_elementu] = [i]

print(wynik)

#Zadanie 5
import unidecode
nazwiska = ["Korek","Kowalski","Komwalewski","Adamczewski","Parchi", "Urun","Bronek","Franek", "Michalczewski", "Żeżyński", "Wor"]


def zad5(nazwiska):
    nazwiska_a_m = []
    nazwiska_n_z = []

    for nazwisko in nazwiska:
        pierwsza_litera = unidecode.unidecode(nazwisko[0]).upper()
        if 'A' <= pierwsza_litera <= 'M':
            nazwiska_a_m.append(nazwisko)
        else:
            nazwiska_n_z.append(nazwisko)

    with open('A-M_nazwiska.txt', 'w', encoding='utf-8') as plik_a_m:
        plik_a_m.write('\n'.join(nazwiska_a_m))

    with open('N-Ż_nazwiska.txt', 'w', encoding='utf-8') as plik_n_z:
        plik_n_z.write('\n'.join(nazwiska_n_z))
    
zad5(nazwiska)


#Zadanie 6

def zadanie_6(text):
    slowa = text.split()
    # odwracam kolejność liter w każdym słowie
    slowa_odwrocone = [slowo[::-1] for slowo in slowa]
    text_odwrocony = ' '.join(slowa_odwrocone)
    print(text_odwrocony)
    
zadanie_6("Ala ma kota")

#Zadanie 7
import random

def zadanie_7():
    talia = ['As pik', 'Król pik', 'Dama pik', 'Walet pik', '10 pik', '9 pik', '8 pik', '7 pik', '6 pik', '5 pik', '4 pik', '3 pik', '2 pik',
             'As kier', 'Król kier', 'Dama kier', 'Walet kier', '10 kier', '9 kier', '8 kier', '7 kier', '6 kier', '5 kier', '4 kier', '3 kier', '2 kier',
             'As trefl', 'Król trefl', 'Dama trefl', 'Walet trefl', '10 trefl', '9 trefl', '8 trefl', '7 trefl', '6 trefl', '5 trefl', '4 trefl', '3 trefl', '2 trefl',
             'As karo', 'Król karo', 'Dama karo', 'Walet karo', '10 karo', '9 karo', '8 karo', '7 karo', '6 karo', '5 karo', '4 karo', '3 karo', '2 karo']
    
    random.shuffle(talia)
    gracze = {}
    for i in range(10):
        # wyciągamy 5 kart dla gracza i dodajemy do jego ręki
        reka = [talia.pop() for _ in range(5)]
        gracze[f'Gracz {i+1}'] = reka
    
    for gracz, reka in gracze.items():
        print(f'{gracz}: {reka}')

# zadanie_7()

import unidecode

def zadanie_8(plik_in, domena, plik_out):
    with open(plik_in, 'r', encoding='utf-8') as plik_wejsciowy:
        linie = [linia.strip() for linia in plik_wejsciowy.readlines()]

    adresy = []
    for linia in linie:
        imie, nazwisko = linia.split()
        imie = unidecode.unidecode(imie)
        nazwisko = unidecode.unidecode(nazwisko)
        email = f"{imie.lower()}.{nazwisko.lower()}@{domena}"
        adresy.append((imie, nazwisko, email))

    with open(plik_out, 'w', encoding='utf-8') as plik_wyjsciowy:
        for imie, nazwisko, email in adresy:
            plik_wyjsciowy.write(f"{imie} {nazwisko}, {email}\n")


zadanie_8('imiona.txt', 'dswp.com', 'emaile.txt')

#Zadanie 9

import random

# losowy wybór hasła
hasla = ["Bez pracy nie ma kołaczy", "cicha woda brzegi rwie", "ciagnie swoj do swego"]
haslo = random.choice(hasla)

# konwersja polskich liter
haslo = haslo.lower()
haslo = haslo.replace('ą', 'a').replace('ę', 'e').replace('ć', 'c').replace('ł', 'l').replace('ń', 'n').replace('ó', 'o').replace('ś', 's').replace('ź', 'z').replace('ż', 'z')

# odgadywane hasło
stan = {}
for litera in haslo:
    if litera == ' ':
        stan[litera] = ' '
    else:
        stan[litera] = '_'

# wyświetlanie aktualnego stanu hasła
def wyswietl_stan():
    for litera in haslo:
        print(stan[litera], end=' ')
    print()

# pętla do odgadywania liter i hasła
while True:
    wyswietl_stan()

    # sprawdzenie czy gracz odgadł już całe hasło
    if '_' not in stan.values():
        print("Gratulacje, odgadłeś hasło!")
        break

    # pobranie litery od gracza
    litera = input("Podaj literę lub całe hasło: ").lower()

    # sprawdzenie czy gracz podał całe hasło
    if litera == haslo:
        print("Gratulacje, odgadłeś hasło!")
        break

    # sprawdzenie czy gracz podał tylko jedną literę
    if len(litera) != 1:
        print("Podaj tylko jedną literę lub całe hasło.")
        continue

    # sprawdzenie czy podana litera występuje w haśle
    if litera in haslo:
        for i in range(len(haslo)):
            if haslo[i] == litera:
                stan[haslo[i]] = litera
    else:
        print("Nie ma takiej litery w haśle.")


