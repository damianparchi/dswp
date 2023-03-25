#Zadanie 1

liczba = int(input('Podaj liczbę całkowitą: '))

print('Liczba w postaci binarnej: ', bin(liczba))
print('Liczba w postaci ósemkowej: ', oct(liczba))
print('Liczba w postaci szesnastkowej: ', hex(liczba))

#Zadanie 2

i = input('Podaj liczbę: ')

if i.isdigit():
    print("liczba jest liczbą typu int.")
else:
    try:
        float(i)
        print("liczba jest liczbą typu float.")
    except ValueError:
        print("Podana liczba nie jest liczbą typu float ani int.")

#Zadanie 3

import sys
liczba = int(input("Podaj liczbę całkowitą: "))

# Zamieniamy liczbę na string
liczba_str = str(liczba)

# Ustawiam wartość początkową sumy i potęgi 10
sum = 0
potega = len(liczba_str) - 1

# przechodzę w pętli przez każdy string liczby i sumuję wynik mnożenia
for cyfra in liczba_str:
    cyfra_int = int(cyfra)
    sum += cyfra_int * (10 ** potega)
    potega -= 1

print("Podaną liczbę całkowitą możemy zapisać jako: ")

for i, cyfra in enumerate(liczba_str):
    cyfra_int = int(cyfra)
    potega = len(liczba_str) - i - 1
    
    if i == 0:
        print(f"{cyfra_int} * 10^{potega}" + f" = {sum}")
    else:
        print(f" + {cyfra_int} * 10^{potega}" + f" = {sum}")


#Zadanie 4

tekst = input('Podaj tekst: ')
zakodowany_tekst = ""
for znak in tekst:
    try:
        zakodowany_tekst += this.d[znak]
    except:
        zakodowany_tekst += znak
print(zakodowany_tekst)

#Zadanie 5

tekst = input("Podaj tekst: ")

# podziel zdanie na wyrazy
wyrazy = tekst.split()
# posortuj je według długości
sortuj_wyrazy = sorted(wyrazy, key=len)

print("Wyrazy posortowane według długości:")
for wyrazy in sortuj_wyrazy:
    print(wyrazy)


#Zadanie 6

from random import randint
tab = []
tab.append(['Koleżanki i koledzy ','Z drugiej strony ','Podobnie ', 'Nie zapominajmy jednak, że ', 'W ten oto sposób ', 'Praktyka dnia codziennego dowodzi, że ', 'Wagi i znaczenia tych problemów nie trzeba szerzej uzasadniać, ponieważ ', 'Różnorakie i bogate doświadczenia ', 'Troska organizacji, a szczególnie ', 'Wyższe założenia ideowe, a także '])
tab.append(['realizacja nakreślonych zadań programowych ', 'zakres i miejsce szkolenia kadr ', 'stały wzrost ilości i zakres naszej aktywności ', 'aktualna struktura organizacji ', 'nowy model działalności organizacyjnej ', 'dalszy rozwój różnych form działalności ', 'stałe zabezpieczenie informacyjno programowe naszej działalności ', 'wzmacnianie i rozwijanie struktur ', 'konsultacja z szerokim aktywem ', 'rozpoczęcie powszechnej akcji kształtowania postaw '])
tab.append(['zmusza nas do przeanalizowania ', 'spełnia istotną rolę w kształtowaniu ', 'wymaga sprecyzowania i określenia ', 'pomaga w przygotowaniu i realizacji ', 'zabezpiecza udział szerokiej grupie w kształtowaniu ', 'spełnia ważne zadania w wypracowaniu ', 'umożliwia w większym stopniu tworzenie ', 'powoduje docenianie wagi ', 'przedstawia intersującą próbę sprawdzenia ', 'pociąga za sobą proces wdrażania i unowocześniania '])
tab.append(['istniejących warunków administracyjno- finansowych. ', 'dalszych kierunków rozwoju. ', 'systemu powszechnego uczestnictwa. ', 'postaw uczestników wobec zadań stawianych przez organizację. ', 'nowych propozycji. ', 'kierunków postępowego wychowania. ', 'systemu szkolenia kadry odpowiadającego potrzebom. ', 'odpowiednich waruknków aktywizacji. ', 'modelu rozwoju. ', 'form oddziaływania. '])


liczba = int(input('Podaj liczbę zdań do wygenerowania: '))
tekst = ""
for i in range(liczba):
    for x in range(4):
        random = randint(0, 9)
        tekst += tab[x][random]
print(tekst)








        
