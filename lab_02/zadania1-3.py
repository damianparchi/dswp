#Zadanie 1
text = input('Wczytaj linię danych rozdzielonych jakimś separatorem (spacja, średnik, itd.)\n')
separator_źródłowy = input('Podaj separator z powyższego zdania:\n')
separator_docelowy = input('Podaj separator docelowy:\n')

split_text = text.split(separator_źródłowy)
text = separator_docelowy.join(split_text)
print('Tekst:\n'+text+'\n')

#Zadanie 2
lorem_ipsum = 'Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker'

#Zadanie 3
litera_1 = 'Damian'[2]
litera_2 = 'Parchimowicz'[3] 
liczba_liter1 = lorem_ipsum.lower().count(litera_1.lower())
liczba_liter2 = lorem_ipsum.lower().count(litera_2.lower())
print(f'W tekście jest {liczba_liter1} liter {litera_1.lower()} oraz {liczba_liter2} liter {litera_2.lower()}')