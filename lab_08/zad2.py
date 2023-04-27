# -*- coding: utf-8 -*-
from datetime import datetime
import random
from array import array

# zapisanie tablicy do pliku oraz jej wczytanie
tab_of_floats = array('f', [random.random() for _ in range(1_000_000)])

start_time = datetime.now()
with open('floats_array.bin', 'wb') as file_arr:
    tab_of_floats.tofile(file_arr)
end_time = datetime.now()

print(f"Czas zapisu tablicy do pliku: {end_time - start_time}")

start_time = datetime.now()
tab_of_floats_loaded = array('f')
file_arr  = open('floats_array.bin', 'rb')
tab_of_floats_loaded.fromfile(file_arr, 1_000_000)
file_arr.close()
end_time = datetime.now()

print(f"Czas ładowania tablicy z pliku: {end_time - start_time}")


# i analogiczna operacja dla listy
list_of_floats = [random.random() for _ in range(1_000_000)]

start_time = datetime.now()
with open('floats_list.txt', 'w') as file_arr:
    file_arr.writelines('\n'.join([str(x) for x in list_of_floats]))
end_time = datetime.now()

print(f"Czas zapisu listy do pliku: {end_time - start_time}")

start_time = datetime.now()
with open('floats_list.txt', 'r') as file_list:
    list_of_floats_loaded = file_list.readlines()

list_of_floats_loaded = [float(x.strip()) for x in list_of_floats_loaded]
end_time = datetime.now()

print(f"Czas ładowania listy z pliku: {end_time - start_time}")
