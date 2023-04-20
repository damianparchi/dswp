from typing import Any

#Zadanie 1

def extract_numbers(vals: list[Any]) -> list[int | float]:
    return list(filter(lambda x: isinstance(x, (int, float)), vals))

wartosci = [5.6, "45", 5, False, True, 4.1, None]

print(extract_numbers(wartosci))

#Zadanie 2
slowa = input("Wprowadź listę wyrazów oddzielonych spacją: ").split()
posortowane_slowa = sorted(slowa, key=lambda x: len(x), reverse=True)
print(posortowane_slowa)


#Zadanie 3
from typing import List, Union

def sort_mixed_list(dane: List[Union[int, str]], reversed: bool = False) -> List[Union[int, str]]:
    return sorted(dane, key=lambda x: (isinstance(x, str), x), reverse=reversed)

wartosci = [7, 'znak', 'string', 'text', 'mixed', 5, 3, 'sort', 4]
posort_dane = sort_mixed_list(wartosci)
print(posort_dane)  

sorted_data_reversed = sort_mixed_list(wartosci, reversed=True)
print(sorted_data_reversed)

#Zadanie 4

import csv
from datetime import datetime

def format_date(date_str):
    date = datetime.strptime(date_str, '%d.%m.%Y')
    return date.strftime('%Y-%m-%d')

def process_row(row):
    row['Utarg'] = row['Utarg'].replace(' z�', 'zł').replace(',', '.').replace(' ', '')
    row['Data zamowienia'] = format_date(row['Data zamowienia'])
    return row

with open('lab_06/zamowienia.csv', encoding='utf-8', errors='ignore') as file:
    reader = csv.DictReader(file, delimiter=';')

    orders = []
    for row in reader:
        orders.append(row)

    poland_orders = list(filter(lambda row: row['Kraj'] == 'Polska', orders))
    germany_orders = list(filter(lambda row: row['Kraj'] == 'Niemcy', orders))

    poland_orders = list(map(process_row, poland_orders))
    germany_orders = list(map(process_row, germany_orders))

    fieldnames = orders[0].keys()

    with open('lab_07/zamowienia_polska.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        writer.writerows(poland_orders)

    with open('lab_07/zamowienia_niemcy.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        writer.writerows(germany_orders)


#Zadanie 5

def sortuj_slownik(d, funkcja):
    return dict(sorted(d.items(), key=lambda x: funkcja(filter(lambda y: isinstance(y, int), x[1])), reverse=True))


d = {'Jan': [1, 3, 4, 7], 'Damian': [4, 5, 7], 'Pawel': [6, 7, 8, 9, 10]}
sorted_d = sortuj_slownik(d, sum)
print(sorted_d)

sorted_d = sortuj_slownik(d, min)
print(sorted_d)

sorted_d = sortuj_slownik(d, max)
print(sorted_d)
