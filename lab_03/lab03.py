#zadanie1

list = [i for i in range(1,11)]
print(list)

list1 = list[:5]
list2 = list[5:]

print(list1)
print(":")
print(list2)

#zadanie2

listzad2 = [0] + list1 + list2

sortlist = listzad2.copy()
sortlist.sort(reverse=True)

print(listzad2)
print(":")
print(sortlist)


#zadanie3

tekst = input("Wprowadź dowolny tekst: ")
unique = set(tekst.lower())
sorted = sorted(unique)
result = "".join(sorted)
print(result)


#zadanie4

slownik = {
1: "styczeń",
2: "luty",
3: "marzec",
4: "kwiecień",
5: "maj",
6: "czerwiec",
7: "lipiec",
8: "sierpień",
9: "wrzesień",
10: "październik",
11: "listopad",
12: "grudzień"
}

#zadanie5

slownik = {
    'pl': {
        1: 'styczeń',
        2: 'luty',
        3: 'marzec',
        4: 'kwiecień',
        5: 'maj',
        6: 'czerwiec',
        7: 'lipiec',
        8: 'sierpień',
        9: 'wrzesień',
        10: 'październik',
        11: 'listopad',
        12: 'grudzienń'
    },
    'en':{
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }
}
    
# Dostęp do miesiąca kwietnia w języku polskim
print(slownik['pl'][4])

# Dostęp do miesiąca kwietnia w języku angielskim
print(slownik['en'][4])


#zadanie6

tekst = 'Marianna'
dictionary = dict.fromkeys(tekst, 1)
print(dictionary)


#zadanie7

import string

text = input("Wprowadź tekst: ")

# text_lower = text.lower()

lowercase_count = sum(1 for char in text if char in string.ascii_lowercase)
uppercase_count = sum(1 for char in text if char in string.ascii_uppercase)

print(f"Znaki pokrywające się z małymi literami: {lowercase_count} ({lowercase_count/len(text)*100:.2f}%)")
print(f"Znaki pokrywające się z dużymi literami: {uppercase_count} ({uppercase_count/len(text)*100:.2f}%)")