# -*- coding: utf-8 -*-
from timeit import timeit
import random


### zadanie 1

setup = """
from array import array
import random
"""

stmt_floats_array = """
array_of_floats = array('f', [random.random() for _ in range(1_000_000)])
"""
stmt_floats_list = """
list_of_floats = [random.random() for _ in range(1_000_000)]
"""

stmt_ints_array = """
array_of_ints = array('i', [random.randint(1, 100) for _ in range(1_000_000)])
"""
stmt_ints_list = """
list_of_ints = [random.randint(1, 100) for _ in range(1_000_000)]
"""

stmt_longs_array = """
array_of_longs = array('l', [random.randint(1, 1000) for _ in range(1_000_000)])
"""
stmt_longs_list = """
list_of_longs = [random.randint(1, 1000) for _ in range(1_000_000)]
"""

print(r"Czas inicjowania array('f') z milionem losowych wartości typu float:")
print(timeit(stmt_floats_array, setup, number=100))

print("Czas inicjowania listy z milionem losowych wartości typu float:")
print(timeit(stmt_floats_list, setup, number=100))

print("Czas inicjowania array('i') z milionem losowych wartości typu int:")
print(timeit(stmt_ints_array, setup, number=100))

print("Czas inicjowania listy z milionem losowych wartości typu int:")
print(timeit(stmt_ints_list, setup, number=100))

print("Czas inicjowania array('l') z milionem losowych wartości typu long:")
print(timeit(stmt_longs_array, setup, number=100))

print("Czas inicjowania listy z milionem losowych wartości typu long:")
print(timeit(stmt_longs_list, setup, number=100))


### zadanie 2