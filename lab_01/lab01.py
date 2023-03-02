#Zadanie 1

int_obiekt1 = -53
int_obiekt2 = int(-0b110101)
print(int_obiekt1, int_obiekt2)

float_obiekt1 = 5
float_obiekt2 = float(0b000101)
print(float_obiekt1, float_obiekt2)


#Zadanie 2

int_bit = [1, 10]
float_isint = [1.5, 10.0]

for x in int_bit:
    if (n := x.bit_count()) > 1: #Python 3.10+
        print("Zmienna z wartością "+str(x)+" ma więcej niż 1 bitm Zmienna ma "+str(n)+" bity.")
for x in float_isint:
    if x.is_integer():
        print("Zmienna z wartością "+str(x)+" może być liczbą całkowitą.")



# Zadanie 3

bit1 = 0b1
bit2 = 0b1000

print(bit1, bit1 << 3)

print(bit2, bit2 >> 4)

print(~bit1, ~~bit2)

print(0b0 & 0b1, 0b1 & 0b1)