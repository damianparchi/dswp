with open('lab_06/zamowienia.csv', 'r') as file:
    content = file.read()

rows = content.splitlines()
headers = rows[0].split('\t')
orders = []

for row in rows[1:]:
    values = row.split('\t')
    order = {headers[i]: values[i] for i in range(len(headers))}
    orders.append(order)

print(orders[:10]) # wyświetlenie
