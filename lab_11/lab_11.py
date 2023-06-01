import csv
from datetime import datetime
import re
import pickle

### Zadanie 1

def find_regex(filename, regex):
    """
    Wyszukuje dopasowania do wyrażeń regularnych w podanym pliku.

    :param filename: Nazwa pliku do przeszukania.
    :param regex: Wyrażenie regularne do dopasowania.
    :return: Lista dopasowanych wyników.
    """
    finds = []
    with open(f'lab_11/{filename}', newline='', encoding="utf8",errors="ignore") as file:
        for line in file:
            matches = re.findall(regex, line)
            finds += matches
    return finds

# Wyrażenia regularne
numbers_regex = r'\d+'
numbers_w_3_d_regex = r'\d{3,}'
ip4s_regex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
word_w_fg_regex = r'[A-Z][a-z]+'
lines_w_4d_regex = r'.+\s.+\s.+\s.+\n'
urls_regex = r'[https?://].+[/]'

# Przeszukiwanie pliku "strings.txt" przy użyciu wyrażeń regularnych
filename = "strings.txt"
numbers = find_regex(filename, numbers_regex)
numbers_w_3_d = find_regex(filename, numbers_w_3_d_regex)
ip4s = find_regex(filename, ip4s_regex)
word_w_fg = find_regex(filename, word_w_fg_regex)
lines_w_4d = find_regex(filename, lines_w_4d_regex)
urls = find_regex(filename, urls_regex)

# Wyświetlanie wyników
print("Wszystkie liczby:", numbers)
print("Liczby co najmniej 3 cyfrowe:", numbers_w_3_d)
print("Adresy IPv4:", ip4s)
print("Wyrazy rozpoczynające się od wielkiej litery:", word_w_fg)
print("Linie z co najmniej 4 wyrazami:", lines_w_4d)
print("Adresy URL:", urls)

# Zad2
date_regex = r'[A-Z][a-z]{2}\s{1,2}\d{1,2}\s\d{2}:\d{2}:\d{2}'
ip_regex = r'\d\sip-\d{1,3}-\d{1,3}-\d{1,3}-\d{1,3}'
user_regex = r'-\d{1,3}\s\w+-?\w+\[?\d*\]?:\s'
comm_regex = r'-\d{1,3}\s\w+-?\w+\[?\d*\]?:\s.+\n'

dates = find_regex("auth.log", date_regex)
dates = [datetime.strptime(x, '%b %d %H:%M:%S').replace(year=2023).strftime('%Y-%m-%d %H:%M:%S') for x in dates]

ips = find_regex("auth.log", ip_regex)
ips = [x[5:].replace("-", ".") for x in ips]

users = find_regex("auth.log", user_regex)
users = [x[5:].split("[")[0].replace(":", "") for x in users]

comms = find_regex("auth.log", comm_regex)
comms = [x[x.find(": ") + 2:-1] for x in comms]
comms = ['"' + x + '"' for x in comms]

with open('zad2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=";")
    for row in zip(dates, ips, users, comms):
        writer.writerow(row)

# Zadanie 3
class Zad3:
    a: int
    b: int
    
    def __init__(self, x, y):
        self.a = x
        self.b = y
    
    def result(self):
        return self.a * self.b
    
    def __repr__(self) -> str:
        return f'({self.a}, {self.b})'

square = Zad3(2, 5)
    
with open('picled_inst', 'wb') as file:
    pickle.dump(square, file)

with open('picled_inst', 'rb') as file:
    square_un = pickle.load(file)
  
print(square_un.result())

# Test
with open('picled_class', 'wb') as file:
    pickle.dump(Zad3, file)

with open('picled_class', 'rb') as file:
    Zad3_un = pickle.load(file)

square2 = Zad3_un(5, 5)
print(square2.result())

# Zadanie 4
packed = [Zad3(x, x * 4 + 2) for x in range(1, 10)]
with open('picled_list', 'wb') as file:
    pickle.dump(packed, file)

with open('picled_list', 'rb') as file:
    unpacked = pickle.load(file)
    
print(unpacked)