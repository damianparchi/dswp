from datetime import datetime

# Formatowanie floata
print(f'{3.141592653589793:f}')

# Dystans 5 spacji pomiędzy znakiem a liczbą dziesiętną
print(f'{10:=+5}')

# Obcinanie długich stringów
print(f'{"xylophoneeee":.9}!')

# Wyrównanie i długość stringa (akapit = 5 spacji)
print(f'{"loremipsumloremipsumloremipsum":{">"}{35}}')

# Datetime
print(f'{datetime.now():%Y-%m-%d %H:%M}')
