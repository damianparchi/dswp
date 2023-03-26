#Zadanie1

A = [1/x for x in range(1, 11)]

B = [2**x for x in range(10)]

C = [x for x in B if x % 4 == 0]

print(A,'\n', B,'\n', C,'\n')

#Zadanie2

import random

# macierz 4x4 o losowych wartościach
macierz = [[random.randint(0, 9) for j in range(4)] for i in range(4)]
print(macierz)

# przekątna
przekatne = [macierz[i][i] for i in range(4)]
print(przekatne)

#Zadanie3

text = 'Ala ma kota.'
generator = ( (x,[ord(y) for y in x]) for x in text.split(" "))
for x in generator:
    print(x)


#Zadanie 4 
import math
from typing import Union, Tuple, List

def row_kwadratowe(a: float, b: float, c: float) -> Union[float, Tuple[float, float], int]:
    delta = b**2 - 4 * a * c
    if (delta < 0):
        # brak pierwiastków
        return -1
    elif (delta == 0):
        # jeden pierwiastek
        x = (-b) / (2 * a)
        return x
    else:
        # równanie ma dwa pierwiastki
        x1 = (- b - math.sqrt(delta)) / (2 * a)
        x2 = (- b + math.sqrt(delta)) / (2 * a)
        return x1, x2

print(row_kwadratowe(6,1,3))
print(row_kwadratowe(1,2,1))
print(row_kwadratowe(1,4,1))

#Zadanie 5

def rzut_kostka(n: int) -> List[Tuple[str, int]]:
    tab_wyników = []
    for i in range(n):
        oczka = random.randint(1, 6)
        ilosc = 1
        for j in range(i):
            if tab_wyników[j][0] == f"oczka: {oczka}":
                ilosc += 1
        tab_wyników.append((f"oczka: {oczka}", ilosc))
    return tab_wyników

liczba = int(input('Podaj liczbę całkowitą: '))
print(rzut_kostka(liczba))

#Zadanie 6
def sort_strings(*strings: str) -> list:
    return sorted(strings)

input_strings = input("Podaj wyrazy oddzielone przecinkiem: ")
strings_list = input_strings.split(",")
sorted_strings_list = sort_strings(*strings_list)
print(sorted_strings_list)
